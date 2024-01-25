from datetime import datetime
from typing import List, Optional

from jsonlines import jsonlines
from pydantic import BaseModel, Field, ValidationError


class Example(BaseModel):
    """
    schema of a confidentiality dataset example, used for training/testing/validating models
    """

    # label: Optional[LabelEnum] = 'Unknown' # "General-Score"       "label"
    label: Optional[str] = "Unknown"  # "General-Score"       "label"
    id: Optional[
        str
    ] = None  # "Example"                             (UID may be sufficient)
    created_on: Optional[datetime] = None
    created_by: Optional[str] = None
    text: str = None  # "Before"              "text"
    label_rationale: Optional[str] = None  # "rationale"
    rewrite: Optional[str] = None  # "After"
    rewrite_rationale: Optional[str] = None  # "Reasoning"
    domain: Optional[str] = None  # "domain"        (Finance, Legal, HR)
    example_type: Optional[
        str
    ] = None  # "example type"  (Sensitive Info, Temporal, Adversarial)
    generator_llm_tag: Optional[str] = None  # "model"
    generator_prompt_tag: Optional[str] = None
    version: str = "0.1"
    topics: List[str] = Field(
        default_factory=list
    )  # "src"     "L0/L1 topics"  (Contracts/Penalties, Compensation/Salary)
    risk_level: Optional[str] = "Unknown"  # "Risk-Based-Score"


def read_jsonl(file_path: str) -> List[Example]:
    data = []
    with jsonlines.open(file_path, "r") as file:
        for line in file:
            try:
                example = Example(
                    id=line.get("Example"),
                    text=line.get("Before"),
                    label=line.get("General-Score"),
                    label_rationale=line.get("Rationale"),
                    risk_level=line.get("Risk-Based-Score"),
                    rewrite=line.get("After"),
                    rewrite_rationale=line.get("Reasoning"),
                )
                data.append(example)
            except (KeyError, ValidationError) as e:
                print(e)
                continue
    return data
