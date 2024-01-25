import logging
import os
import subprocess
from functools import cached_property
from typing import Any, List

import torch
from transformers import AutoModel, AutoTokenizer

from .input import Example
from .result import ModelResult

logger = logging.getLogger(__name__)


class ModelProcess:
    def __init__(self, model_path: str, inputs: List[Example]):
        self.inputs = inputs
        self.model_path = model_path

    def _run_ggml_model(self, prompt: str, ggml_gpt_path: str) -> str:
        command = [
            ggml_gpt_path,
            "-m",
            self.model_path,
            "-p",
            prompt,
        ]

        try:
            output = subprocess.check_output(command, stderr=subprocess.STDOUT)
            print(output)
            return output.decode("utf-8")
        except subprocess.CalledProcessError as e:
            if "invalid model file" in e.output.decode("utf-8"):
                raise ValueError("Invalid ggml model")
            return ""

    @cached_property
    def device(self) -> Any:
        if torch.cuda.is_available():
            return torch.device("cuda")
        logger.error("CUDA is not available, the model will be running on the CPU")
        return torch.device("cpu")

    def gpu_run(self) -> List[ModelResult]:
        if not os.path.isdir(self.model_path):
            raise ValueError("Expected a path to the model directory")
        model = AutoModel.from_pretrained(self.model_path)
        model.to(self.device)
        tokenizer = AutoTokenizer.from_pretrained(self.model_path)
        results = []
        # TODO fix for new using
        for input_ in self.inputs:
            inputs = tokenizer.encode(input_.text, return_tensors="pt")
            output = model.generate(
                inputs, max_length=len(input_.text) / 2 + 150, num_return_sequences=1
            )
            generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
            results.append(ModelResult.from_model_output(output=generated_text))
        return results

    def cpu_run(self, ggml_gpt_path: str = ".bin/gpt-2-backend") -> List[ModelResult]:
        if not os.path.isfile(self.model_path):
            raise ValueError("Expected a path to the ggml model")

        results = []
        for input_ in self.inputs:
            output = self._run_ggml_model(
                prompt=input_.text, ggml_gpt_path=ggml_gpt_path
            )
            results.append(ModelResult.from_model_output(output=output))
        return results
