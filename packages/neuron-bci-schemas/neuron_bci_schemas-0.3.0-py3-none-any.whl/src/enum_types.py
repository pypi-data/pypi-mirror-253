from enum import Enum


class LabelEnum(str, Enum):
    CONFIDENTIAL = "Confidential"
    NON_CONFIDENTIAL = "Non-Confidential"
    PUBLIC = "Public"
    INTERNAL = "Internal Use"
    STRICTLY_CONFIDENTIAL = "Strictly Confidential"
    UNKNOWN = "Unknown"


class RiskEnum(str, Enum):
    CRITICAL = "Critical"
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"
    UNKNOWN = "Unknown"
