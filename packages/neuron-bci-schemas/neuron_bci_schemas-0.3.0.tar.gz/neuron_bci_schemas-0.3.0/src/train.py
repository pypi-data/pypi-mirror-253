import json
import logging
import os.path
import random
import shutil
from functools import cached_property
from pathlib import Path
from typing import List, Dict, Tuple

import numpy as np
import pandas as pd
import torch
from datasets import load_dataset, DatasetDict
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
from sklearn.model_selection import train_test_split
from torch.utils.data import Dataset
from transformers import (
    AutoTokenizer,
    TrainingArguments,
    AutoModelForSequenceClassification,
    Trainer,
    TrainerCallback,
)
from trl import SFTTrainer

from config import Config
from input import Example

logger = logging.getLogger(__name__)


class CMLLoggingCallback(TrainerCallback):
    def __init__(self, report_filename):
        super().__init__()
        self.report_filename = report_filename

    def on_log(self, args, state, control, logs=None, **kwargs):
        with open(self.report_filename, "a") as report_file:
            print(f"Step {state.global_step}", file=report_file)
            for key, value in logs.items():
                print(f"{key}: {value}", file=report_file)
            print("\n", file=report_file)


class ModelTrain:
    def __init__(
        self,
        inputs: List[Example],
        model_name: str,
        tokenizer: str,
        result_path: Path,
        num_train_epochs: int = 10,
    ):
        self._inputs = inputs
        self._model_name = model_name
        self.num_train_epochs = num_train_epochs
        self._dataset_path = Path(
            os.path.join(Config.ROOT_PATH, "dataset")
        )
        self.result_path = result_path
        self._dataset_path.mkdir(parents=True, exist_ok=True)
        self.result_path.mkdir(parents=True, exist_ok=True)
        self.tokenizer = AutoTokenizer.from_pretrained(tokenizer)
        self.tokenizer.pad_token = self.tokenizer.eos_token

    def _wrap_tag(self, tag: str, text: str) -> str:
        return f"<{tag.capitalize()}>{text}<{tag.capitalize()}Ends>"

    @cached_property
    def preprocessed_data(self) -> List[Dict[str, str]]:
        processed_data = []
        bad_ones = 0
        for i, item in enumerate(self._inputs):
            # Check if all required keys are present and 'After' does not contain '[' or ']'
            if all((item.text, item.rewrite, item.rewrite_rationale)):
                if "[" not in item.rewrite and "]" not in item.rewrite:
                    text = f"""
                        {self._wrap_tag(tag='Before', text=item.text)}
                        {self._wrap_tag(tag='After', text=item.rewrite)}
                        {self._wrap_tag(tag='Reasoning', text=item.rewrite_rationale)}
                        {self.tokenizer.eos_token}
                    """
                    processed_data.append({"text": text})

                    if i % 2 == 0:
                        text2 = f"""
                            {self._wrap_tag(tag='Before', text=item.rewrite)}
                            {self._wrap_tag(tag='After', text=item.rewrite)}
                            {self._wrap_tag(tag='Reasoning', text="No BCI")}
                            {self.tokenizer.eos_token}
                        """
                        processed_data.append({"text": text2})
                else:
                    bad_ones += 1
            else:
                bad_ones += 1
        logger.info(f"bad_ones: {bad_ones}")
        return processed_data

    def tokenize(self, examples):
        return self.tokenizer(examples["text"], padding="max_length", truncation=True)

    def _prepare_dataset(self) -> Tuple[DatasetDict, DatasetDict]:
        random.shuffle(self.preprocessed_data)
        # Split the data into training and validation sets
        train_data = self.preprocessed_data[: int(len(self.preprocessed_data) * 0.8)]
        val_data = self.preprocessed_data[int(len(self.preprocessed_data) * 0.8) :]

        # Save the split data into separate files
        with open(os.path.join(self._dataset_path, "train_data.json"), "w") as f:
            json.dump(train_data, f)
        with open(os.path.join(self._dataset_path, "val_data.json"), "w") as f:
            json.dump(val_data, f)

        tokenized_train_data = load_dataset(
            "json",
            data_files={"train": os.path.join(self._dataset_path, "train_data.json")},
        ).map(self.tokenize, batched=True)
        tokenized_val_data = load_dataset(
            "json",
            data_files={
                "validation": os.path.join(self._dataset_path, "val_data.json")
            },
        ).map(self.tokenize, batched=True)
        return tokenized_train_data, tokenized_val_data

    def train(self) -> None:
        tokenized_train_data, tokenized_val_data = self._prepare_dataset()
        training_args = TrainingArguments(
            output_dir="./results",
            num_train_epochs=self.num_train_epochs,
            weight_decay=0.01,
            logging_dir="./logs",
            logging_strategy="epoch",
            fp16=True,
            optim="adamw_8bit",
            learning_rate=1e-5,
            evaluation_strategy="epoch",
            eval_steps=None,
        )

        # Initialize the Trainer
        trainer = SFTTrainer(
            self._model_name,
            train_dataset=tokenized_train_data["train"],
            eval_dataset=tokenized_val_data["validation"],
            dataset_text_field="text",
            args=training_args,
            neftune_noise_alpha=5,
            callbacks=[
                CMLLoggingCallback(
                    os.path.join(Config.ROOT_PATH.parent, "train_report.md")
                )
            ],
        )

        # Train the model
        trainer.train()

        # Save the model
        trainer.save_model(str(self.result_path))
        self.tokenizer.save_pretrained(str(self.result_path))

        trainer.evaluate(
            eval_dataset=tokenized_val_data["validation"], metric_key_prefix="eval"
        )
        shutil.rmtree(self._dataset_path)


class BCIClassificationTrain:
    def __init__(
        self,
        inputs: List[Example],
        model_path: str,
        max_steps: int = 50000,
        fp16: bool = torch.cuda.is_available(),
        neftune_alpha: float = 5,
    ):
        self._inputs = inputs
        self._max_steps = max_steps
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForSequenceClassification.from_pretrained(
            model_path, num_labels=2
        )
        self.data = pd.DataFrame(i.model_dump() for i in inputs)
        self.fp16 = fp16
        self.neftune_alpha = neftune_alpha

    def compute_metrics(self, p):
        pred, labels = p
        pred = np.argmax(pred, axis=1)

        accuracy = accuracy_score(y_true=labels, y_pred=pred)
        recall = recall_score(y_true=labels, y_pred=pred)
        precision = precision_score(y_true=labels, y_pred=pred)
        f1 = f1_score(y_true=labels, y_pred=pred)

        return {
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall,
            "f1": f1,
        }

    def train(self) -> None:
        X_before = list(self.data["text"].astype(str)) + list(
            self.data["rewrite"].astype(str)
        )
        y_before = [1 for _ in list(self.data["text"].astype(str))] + [
            0 for _ in list(self.data["rewrite"].astype(str))
        ]

        # Combine "Before" and "After" texts for training
        X = X_before
        y = y_before

        # Preprocess data
        X_train, X_val, y_train, y_val = train_test_split(
            X, y, shuffle=True, random_state=42, test_size=0.2
        )
        X_train_tokenized = self.tokenizer(
            X_train, padding=True, truncation=True, max_length=512
        )
        X_val_tokenized = self.tokenizer(
            X_val, padding=True, truncation=True, max_length=512
        )
        train_dataset = BCIClassificationDataset(X_train_tokenized, y_train)
        val_dataset = BCIClassificationDataset(X_val_tokenized, y_val)

        # Define Trainer
        args = TrainingArguments(
            output_dir="output",
            evaluation_strategy="steps",
            eval_steps=int(self._max_steps * 0.02),
            max_steps=self._max_steps,
            save_steps=1000,
            warmup_steps=int(self._max_steps * 0.005),
            weight_decay=0.01,
            neftune_noise_alpha=self.neftune_alpha,
            #  per_device_train_batch_size=8,
            #  per_device_eval_batch_size=8,
            num_train_epochs=3,
            seed=0,
            fp16=self.fp16,
            learning_rate=1e-5,
            load_best_model_at_end=True,
        )
        trainer = Trainer(
            model=self.model,
            args=args,
            train_dataset=train_dataset,
            eval_dataset=val_dataset,
            compute_metrics=self.compute_metrics,
            # callbacks=[EarlyStoppingCallback(early_stopping_patience=3)],
        )

        # Train pre-trained model
        trainer.train()

        trainer.save_model("./classifier/")
        self.tokenizer.save_pretrained("./classifier/")


# Create torch dataset
class BCIClassificationDataset(Dataset):
    def __init__(self, encodings, labels=None):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        if self.labels:
            item["labels"] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.encodings["input_ids"])
