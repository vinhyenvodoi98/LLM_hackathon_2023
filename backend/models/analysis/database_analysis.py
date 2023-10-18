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


class DatabaseAnalysisDataTypeValue(BaseModel):
    multi_select: bool = True
    current: List[Optional[DatabaseAnalysisDataTypeEnum]]
    selectable_value: List[str] = ["Text", "Number", "Datetime", "Boolean", "Binary", "JSON", "XML"]

    class Config:
        json_schema_extra = {
            "example": {
                "multi_select": True,
                "current": ["Text", "Number", "Datetime"],
                "selectable_value": ["Text", "Number", "Datetime", "Boolean", "Binary", "JSON", "XML"]
            }
        }


class DatabaseAnalysisDataType(BaseModel):
    question: str = "Which type of data that you want to save into your DB?"
    explanation: Optional[str]
    value: DatabaseAnalysisDataTypeValue

    class Config:
        json_schema_extra = {
            "example": {
                "question": "Which type of data that you want to save into your DB?",
                "value": {
                    "multi_select": True,
                    "current": ["Text", "Number", "Datetime"],
                    "selectable_value": ["Text", "Number", "Datetime", "Boolean", "Binary", "JSON", "XML"]
                },
                "explanation": "Explain why does the system suggest this value?"
            }
        }


class DatabaseAnalysisVolumeEnum(Enum):
    """Amount of database data volume."""
    # less than 1M records
    SMALL = "small"
    # more than 1M records, less than 100M records
    MEDIUM = "medium"
    # more than 100M records
    LARGE = "large"


class DatabaseAnalysisVolumeValue(BaseModel):
    multi_select: bool = False
    current: Optional[DatabaseAnalysisVolumeEnum]
    selectable_value: List[str] = ["small", "medium", "large"]

    class Config:
        json_schema_extra = {
            "example": {
                "multi_select": False,
                "current": "medium",
                "selectable_value": ["small", "medium", "large"]
            }
        }


class DatabaseAnalysisVolume(BaseModel):
    question: str = "How much data do you need to store? " \
                    "Less than 1 million records is small. " \
                    "Within 1 million and 100 million is medium. " \
                    "And above 100 million records is large."
    explanation: Optional[str]
    value: DatabaseAnalysisVolumeValue

    class Config:
        json_schema_extra = {
            "example": {
                "question": "Question that the system analyzed",
                "value": {
                    "multi_select": False,
                    "current": "medium",
                    "selectable_value": ["small", "medium", "large"]
                },
                "explanation": "Explain why does the system suggest this value?"
            }
        }


class BoolValue(BaseModel):
    multi_select: bool = False
    current: Optional[bool]
    selectable_value: List[bool] = [True, False]

    class Config:
        json_schema_extra = {
            "example": {
                "multi_select": False,
                "current": True,
                "selectable_value": [True, False]
            }
        }


class BoolWithDescription(BaseModel):
    question: str
    explanation: Optional[str]
    value: BoolValue

    class Config:
        json_schema_extra = {
            "example": {
                "question": "Question that the system analyzed",
                "value": {
                    "multi_select": False,
                    "current": True,
                    "selectable_value": [True, False]
                },
                "explanation": "Explain why does the system suggest this value?"
            }
        }


class DatabaseAnalysisDataModel(BaseModel):
    """Project analysis result for data model."""
    data_type: DatabaseAnalysisDataType
    unstructured_data: BoolWithDescription
    time_series: BoolWithDescription

    class Config:
        json_schema_extra = {
            "example": {
                "data_type": {
                    "question": "Question that the system analyzed",
                    "value": {
                        "multi_select": True,
                        "current": ["Text", "Number", "Datetime"],
                        "selectable_value": ["Text", "Number", "Datetime", "Boolean", "Binary", "JSON", "XML"]
                    },
                    "explanation": "Explain why does the system suggest this value?"
                },
                "unstructured_data": {
                    "question": "Question that the system analyzed",
                    "value": {
                        "multi_select": False,
                        "current": False,
                        "selectable_value": [True, False]
                    },
                    "explanation": "Explain why does the system suggest this value?"
                },
                "time_series": {
                    "question": "Question that the system analyzed",
                    "value": {
                        "multi_select": False,
                        "current": None,
                        "selectable_value": [True, False]
                    },
                    "explanation": "Explain why does the system suggest this value?"
                }
            }
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
                    "value": {
                        "multi_select": False,
                        "current": "medium",
                        "selectable_value": ["small", "medium", "large"]
                    },
                    "explanation": "Explain why does the system suggest this value?"
                },
                "fast_response_time": {
                    "question": "Question that the system analyzed",
                    "value": {
                        "multi_select": False,
                        "current": False,
                        "selectable_value": [True, False]
                    },
                    "explanation": "Explain why does the system suggest this value?"
                },
                "read_consistency": {
                    "question": "Question that the system analyzed",
                    "value": {
                        "multi_select": False,
                        "current": False,
                        "selectable_value": [True, False]
                    },
                    "explanation": "Explain why does the system suggest this value?"
                },
                "high_write_workloads": {
                    "question": "Question that the system analyzed",
                    "value": {
                        "multi_select": False,
                        "current": None,
                        "selectable_value": [True, False]
                    },
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
                    "value": {
                        "multi_select": False,
                        "current": True,
                        "selectable_value": [True, False]
                    },
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
                        "value": {
                            "multi_select": True,
                            "current": ["Text", "Number", "Datetime"],
                            "selectable_value": ["Text", "Number", "Datetime", "Boolean", "Binary", "JSON", "XML"]
                        },
                        "explanation": "Explain why does the system suggest this value?"
                    },
                    "unstructured_data": {
                        "question": "Question that the system analyzed",
                        "value": {
                            "multi_select": False,
                            "current": False,
                            "selectable_value": [True, False]
                        },
                        "explanation": "Explain why does the system suggest this value?"
                    },
                    "time_series": {
                        "question": "Question that the system analyzed",
                        "value": {
                            "multi_select": False,
                            "current": None,
                            "selectable_value": [True, False]
                        },
                        "explanation": "Explain why does the system suggest this value?"
                    },
                },
                "requirements": {
                    "volume": {
                        "question": "Question that the system analyzed",
                        "value": {
                            "multi_select": False,
                            "current": "medium",
                            "selectable_value": ["small", "medium", "large"]
                        },
                        "explanation": "Explain why does the system suggest this value?"
                    },
                    "fast_response_time": {
                        "question": "Question that the system analyzed",
                        "value": {
                            "multi_select": False,
                            "current": False,
                            "selectable_value": [True, False]
                        },
                        "explanation": "Explain why does the system suggest this value?"
                    },
                    "read_consistency": {
                        "question": "Question that the system analyzed",
                        "value": {
                            "multi_select": False,
                            "current": False,
                            "selectable_value": [True, False]
                        },
                        "explanation": "Explain why does the system suggest this value?"
                    },
                    "high_write_workloads": {
                        "question": "Question that the system analyzed",
                        "value": {
                            "multi_select": False,
                            "current": None,
                            "selectable_value": [True, False]
                        },
                        "explanation": "Explain why does the system suggest this value?"
                    },
                },
                "cost": {
                    "commercial_allow": {
                        "question": "Question that the system analyzed",
                        "value": {
                            "multi_select": False,
                            "current": True,
                            "selectable_value": [True, False]
                        },
                        "explanation": "Explain why does the system suggest this value?"
                    },
                }
            }
        }

    @staticmethod
    def from_analysis_result(analysis_result: dict) -> "APIDatabaseAnalysisResponseModel":
        """."""
        data_model_dict = analysis_result["data_model"]
        data_model = DatabaseAnalysisDataModel(
            data_type=DatabaseAnalysisDataType(
                question="Which type of data that you want to save into your DB?",
                explanation=data_model_dict["data_type"]["reason"],
                value=DatabaseAnalysisDataTypeValue(
                    current=data_model_dict["data_type"]["value"]
                )
            ),
            unstructured_data=BoolWithDescription(
                question="Do your project contain unstructured data?",
                explanation=data_model_dict["unstructured_data"]["reason"],
                value=BoolValue(
                    current=data_model_dict["unstructured_data"]["value"]
                ),
            ),
            time_series=BoolWithDescription(
                question="Time series data is a collection of observations obtained through repeated measurements over time. Is your data time series data?",
                explanation=data_model_dict["time_series"]["reason"],
                value=BoolValue(
                    current=data_model_dict["time_series"]["value"]
                ),
            )
        )
        requirements_dict = analysis_result["requirements"]
        requirements = DatabaseAnalysisRequirements(
            volume=DatabaseAnalysisVolume(
                question="How much data do you need to store? Less than 1 million records is small. Within 1 million and 100 million is medium. And above 100 million records is large.",
                explanation=requirements_dict["volume"]["reason"],
                value=DatabaseAnalysisVolumeValue(
                    current=requirements_dict["volume"]["value"][0]
                ),
            ),
            fast_response_time=BoolWithDescription(
                question="Do your project require microsecond response time from database? For example, leaderboards or session store may requires it.",
                explanation=requirements_dict["fast_response_time"]["reason"],
                value=BoolValue(
                    current=requirements_dict["fast_response_time"]["value"]
                ),
            ),
            read_consistency=BoolWithDescription(
                question="Is read consistency (any read request will return the most recent write) one of the most important requirements?",
                explanation=requirements_dict["read_consistency"]["reason"],
                value=BoolValue(
                    current=requirements_dict["read_consistency"]["value"]
                ),
            ),
            high_write_workloads=BoolWithDescription(
                question="Do you have a high-write workloads?",
                explanation=requirements_dict["high_write_workloads"]["reason"],
                value=BoolValue(
                    current=requirements_dict["high_write_workloads"]["value"]
                ),
            )
        )
        cost_dict = analysis_result["cost"]
        cost = DatabaseAnalysisCost(
            commercial_allow=BoolWithDescription(
                question="Are you willing to use commercial database?",
                explanation=cost_dict["commercial_allow"]["reason"],
                value=BoolValue(
                    current=cost_dict["commercial_allow"]["value"]
                ),
            ),
        )
        return APIDatabaseAnalysisResponseModel(
            data_model=data_model,
            requirements=requirements,
            cost=cost
        )
