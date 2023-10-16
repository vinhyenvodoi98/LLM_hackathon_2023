from enum import Enum
from typing import Optional, List

from dataclasses import dataclass
from pydantic import BaseModel


class APIDatabaseAnalysisRequestModel(BaseModel):
    """Project analysis post request."""
    requirement: str

    class Config:
        json_schema_extra = {
            "example": {
                "requirement": f"My project is an IoT project "
                           f"which uses sensors to record the value of outdoor temperature, humidity "
                           f"and then display it on a dashboard. "
                           f"The dashboard should allow data export and graph customization."
            }
        }


class DatabaseAnalysisDataTypeEnum(Enum):
    """Type of database data type."""
    TEXT = "Text"
    NUMBER = "Number"
    DATETIME = "Datetime"
    BOOLEAN = "Boolean"
    BINARY = "Binary"
    JSON = "JSON"
    XML = "XML"


class DatabaseAnalysisDataType(BaseModel):
    question: str = "Which type of data that you want to save into your DB?"
    explanation: Optional[str] = ""
    value: List[DatabaseAnalysisDataTypeEnum]

    class Config:
        json_schema_extra = {
            "question": "Question that the system analyzed",
            "value": ["Text"],
            "explanation": "Explain why does the system suggest this value?"
        }


class DatabaseAnalysisVolumeEnum(Enum):
    """Amount of database data volume."""
    # less than 1M records
    SMALL = "small"
    # more than 1M records, less than 100M records
    MEDIUM = "medium"
    # more than 100M records
    LARGE = "large"


class DatabaseAnalysisVolume(BaseModel):
    question: str = "How much data do you need to store? " \
                    "Less than 1 million records is small. " \
                    "Within 1 million and 100 million is medium. " \
                    "And above 100 million records is large."
    explanation: Optional[str] = ""
    value: List[DatabaseAnalysisVolumeEnum]

    class Config:
        json_schema_extra = {
            "question": "Question that the system analyzed",
            "value": ["small"],
            "explanation": "Explain why does the system suggest this value?"
        }

    @staticmethod
    def get_values(prompt_values) -> List[DatabaseAnalysisVolumeEnum]:
        if prompt_values is None:
            return []
        return prompt_values


class BoolWithDescription(BaseModel):
    question: str
    explanation: Optional[str] = ""
    value: Optional[bool]

    class Config:
        json_schema_extra = {
            "question": "Question that the system analyzed",
            "value": True,
            "explanation": "Explain why does the system suggest this value?"
        }


class DatabaseAnalysisDataModel(BaseModel):
    """Project analysis result for data model."""
    data_type: DatabaseAnalysisDataType
    unstructured_data: BoolWithDescription
    time_series: BoolWithDescription

    class Config:
        json_schema_extra = {
            "data_type": {
                "question": "Question that the system analyzed",
                "value": ["Text", "Number", "Datetime"],
                "explanation": "Explain why does the system suggest this value?"
            },
            "unstructured_data": {
                "question": "Question that the system analyzed",
                "value": True,
                "explanation": "Explain why does the system suggest this value?"
            },
            "time_series": {
                "question": "Question that the system analyzed",
                "value": None,
                "explanation": "Explain why does the system suggest this value?"
            },
        }


class DatabaseAnalysisRequirements(BaseModel):
    """Project analysis result for requirement."""
    volume: DatabaseAnalysisVolume
    fast_response_time: BoolWithDescription
    read_consistency: BoolWithDescription
    high_write_workloads: BoolWithDescription

    class Config:
        json_schema_extra = {
            "example": {
                "volume": {
                    "question": "Question that the system analyzed",
                    "value": ["small", "medium"],
                    "explanation": "Explain why does the system suggest this value?"
                },
                "fast_response_time": {
                    "question": "Question that the system analyzed",
                    "value": True,
                    "explanation": "Explain why does the system suggest this value?"
                },
                "read_consistency": {
                    "question": "Question that the system analyzed",
                    "value": True,
                    "explanation": "Explain why does the system suggest this value?"
                },
                "high_write_workloads": {
                    "question": "Question that the system analyzed",
                    "value": None,
                    "explanation": "Explain why does the system suggest this value?"
                },
            }
        }


class DatabaseAnalysisCost(BaseModel):
    """Project analysis result for cost."""
    commercial_allow: BoolWithDescription

    class Config:
        json_schema_extra = {
            "example": {
                "commercial_allow": {
                    "question": "Question that the system analyzed",
                    "value": True,
                    "explanation": "Explain why does the system suggest this value?"
                },
            }
        }


class APIDatabaseAnalysisResponseModel(BaseModel):
    """Project analysis result for API."""
    data_model: DatabaseAnalysisDataModel
    requirements: DatabaseAnalysisRequirements
    cost: DatabaseAnalysisCost

    class Config:
        json_schema_extra = {
            "example": {
                "data_model": {
                    "data_type": {
                        "question": "Question that the system analyzed",
                        "value": ["text", "number", "datetime"],
                        "explanation": "Explain why does the system suggest this value?"
                    },
                    "unstructured_data": {
                        "question": "Question that the system analyzed",
                        "value": True,
                        "explanation": "Explain why does the system suggest this value?"
                    },
                    "time_series": {
                        "question": "Question that the system analyzed",
                        "value": None,
                        "explanation": "Explain why does the system suggest this value?"
                    },
                },
                "requirements": {
                    "volume": {
                        "question": "Question that the system analyzed",
                        "value": ["small", "medium"],
                        "explanation": "Explain why does the system suggest this value?"
                    },
                    "fast_response_time": {
                        "question": "Question that the system analyzed",
                        "value": True,
                        "explanation": "Explain why does the system suggest this value?"
                    },
                    "read_consistency": {
                        "question": "Question that the system analyzed",
                        "value": True,
                        "explanation": "Explain why does the system suggest this value?"
                    },
                    "high_write_workloads": {
                        "question": "Question that the system analyzed",
                        "value": None,
                        "explanation": "Explain why does the system suggest this value?"
                    },
                },
                "cost": {
                    "commercial_allow": {
                        "question": "Question that the system analyzed",
                        "value": True,
                        "explanation": "Explain why does the system suggest this value?"
                    },
                }
            }
        }
