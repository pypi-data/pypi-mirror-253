import re
from typing import Optional, List, Iterable, Type

from pydantic import Field, BaseModel


class ModelResult(BaseModel):
    initial: Optional[str] = None
    predicted_label: Optional[str] = None
    predicted_label_rationale: Optional[str] = None
    predicted_risk_level: Optional[str] = None
    predicted_rewrite: Optional[str] = None
    predicted_rewrite_rationale: Optional[str] = None
    predictor_llm_tag: Optional[str] = None
    predictor_prompt_tag: Optional[str] = None
    probability_confidential: Optional[float] = Field(min=0.0, max=1.0, default=None)
    confidence: Optional[int] = Field(min=0, max=100, default=None)
    predicted_topics: List[str] = Field(default_factory=list)

    __ATTR_MAPPING__ = {
        "initial": "Input",
        "predicted_label": "General",
        "predicted_label_rationale": "LabelRationale",
        "predicted_risk_level": "Risk",
        "predicted_rewrite": "Result",
        "predicted_rewrite_rationale": "Reasoning",
        "predictor_llm_tag": "LlmTag",
        "predictor_prompt_tag": "PromptTag",
        "probability_confidential": "ProbabilityConfidential",
        "confidence": "Confidence",
        "predicted_topics": "src",
    }

    @classmethod
    def from_model_output(cls: Type["ModelResult"], output: str) -> "ModelResult":
        result = ModelResult()
        for attr_name, tag in cls.__ATTR_MAPPING__.items():
            pattern = f"<{tag}>(.*?)<{tag}Ends>"
            attr_value = re.findall(pattern, output)
            if not attr_value:
                continue
            if isinstance(getattr(result, attr_name), Iterable):
                prepared_value = [i.strip() for i in attr_value]
            else:
                prepared_value = attr_value[0].strip()
            setattr(result, attr_name, prepared_value)
        return result
