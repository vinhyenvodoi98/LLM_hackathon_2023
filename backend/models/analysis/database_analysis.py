from enum import Enum
from typing import Optional, List

from dataclasses import dataclass
from pydantic import BaseModel


class APIDatabaseAnalysisRequestModel(BaseModel):
    """Project analysis post request."""
    context: str

    class Config:
        json_schema_extra = {
            "example": {
                "context": f"My project is an IoT project "
                           f"which uses sensors to record the value of outdoor temperature, humidity "
                           f"and then display it on a dashboard. "
                           f"The dashboard should allow data export and graph customization."
            }
        }


class DatabaseAnalysisDataTypeEnum(Enum):
    """Type of database data type."""
    TEXT = "text"
    NUMBER = "number"
    DATETIME = "datetime"
    BOOLEAN = "boolean"
    BINARY = "binary"
    JSON = "json"
    XML = "xml"


class DatabaseAnalysisDataType(BaseModel):
    question: str = "How much data do you need to store? " \
                    "Less than 1 million records is small. " \
                    "Within 1 million and 100 million is medium. " \
                    "And above 100 million records is large."
    explanation: Optional[str] = ""
    value: List[DatabaseAnalysisDataTypeEnum]

    class Config:
        json_schema_extra = {
            "question": "Question that the system analyzed",
            "value": ["text"],
            "explanation": "Explain why does the system suggest this value?"
        }


class DatabaseAnalysisVolumeEnum(Enum):
    """Amount of database data volume."""
    # less than 1M records
    SMALL = "small"
    # more than 1M records, less than 100M records
    MEDIUM = "medium"
    # more than 100M records
    HIGH = "high"


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


class CustomBaseModel(BaseModel):
    """Base model with custom function."""
    def get_value_from_field(self, field: str):
        """Get value."""
        for key, value_obj in self.__dict__.items():
            if field == key:
                return value_obj.value
        return None


class DatabaseAnalysisDataModel(CustomBaseModel):
    """Project analysis result for data model."""
    data_type: DatabaseAnalysisDataType
    unstructured_data: BoolWithDescription
    time_series: BoolWithDescription
    relationship_centric: BoolWithDescription

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
            "relationship_centric": {
                "question": "Question that the system analyzed",
                "value": False,
                "explanation": "Explain why does the system suggest this value?"
            }
        }


class DatabaseAnalysisRequirements(CustomBaseModel):
    """Project analysis result for requirement."""
    volume: DatabaseAnalysisVolume
    complex_query_patterns: BoolWithDescription
    read_consistency: BoolWithDescription
    high_write_workloads: BoolWithDescription
    high_availability: BoolWithDescription

    class Config:
        json_schema_extra = {
            "example": {
                "volume": {
                    "question": "Question that the system analyzed",
                    "value": ["small", "medium"],
                    "explanation": "Explain why does the system suggest this value?"
                },
                "complex_query_patterns": {
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
                "high_availability": {
                    "question": "Question that the system analyzed",
                    "value": True,
                    "explanation": "Explain why does the system suggest this value?"
                },
            }
        }


class DatabaseAnalysisCost(CustomBaseModel):
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

    def get_value_from_field(self, field: str):
        """Get value."""
        value = self.data_model.get_value_from_field(field)
        if value is not None:
            return value
        value = self.requirements.get_value_from_field(field)
        if value is not None:
            return value
        value = self.cost.get_value_from_field(field)
        return value

    class Config:
        json_schema_extra = {
            "example": {
                "data_model": {
                    "data_type": {
                        "question": "Question that the system analyzed",
                        "value": ["text", "number", "datetime"],
                        "explanation": "Explain why does the system suggest this value?"
                    },
                    "structured_data": {
                        "question": "Question that the system analyzed",
                        "value": True,
                        "explanation": "Explain why does the system suggest this value?"
                    },
                    "time_series": {
                        "question": "Question that the system analyzed",
                        "value": None,
                        "explanation": "Explain why does the system suggest this value?"
                    },
                    "relationship_centric": {
                        "question": "Question that the system analyzed",
                        "value": False,
                        "explanation": "Explain why does the system suggest this value?"
                    }
                },
                "requirements": {
                    "volume": {
                        "question": "Question that the system analyzed",
                        "value": ["small", "medium"],
                        "explanation": "Explain why does the system suggest this value?"
                    },
                    "complex_query_patterns": {
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
                    "high_availability": {
                        "question": "Question that the system analyzed",
                        "value": True,
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
