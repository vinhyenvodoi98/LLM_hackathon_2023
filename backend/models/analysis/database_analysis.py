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
    # vector database
    Vector = "Vector"
    # SQL, NoSQL database
    StringOrNumber = "StringOrNumber"
    # document search engine
    FullText = "FullText"


class DatabaseAnalysisDataType(BaseModel):
    value: DatabaseAnalysisDataTypeEnum
    description: Optional[str] = ""

    class Config:
        json_schema_extra = {
            "value": "Vector",
            "description": ""
        }


class DatabaseAnalysisVolumeEnum(Enum):
    """Amount of database data volume."""
    # less than 1M records
    SMALL = "SMALL"
    # more than 1M records, less than 100M records
    MEDIUM = "MEDIUM"
    # more than 100M records
    HIGH = "HIGH"


class DatabaseAnalysisVolume(BaseModel):
    value: List[DatabaseAnalysisVolumeEnum]
    description: Optional[str] = ""

    class Config:
        json_schema_extra = {
            "value": ["SMALL"],
            "description": ""
        }


class BoolWithDescription(BaseModel):
    value: Optional[bool]
    description: Optional[str] = ""

    class Config:
        json_schema_extra = {
            "value": True,
            "description": ""
        }


class DatabaseAnalysisDataModel(BaseModel):
    """Project analysis result for data model."""
    data_type: DatabaseAnalysisDataType
    structured_data: BoolWithDescription
    time_series: BoolWithDescription
    relationship_centric: BoolWithDescription

    class Config:
        json_schema_extra = {
            "data_type": {
                "value": "StringOrNumber",
                "description": ""
            },
            "structured_data": {
                "value": True,
                "description": ""
            },
            "time_series": {
                "value": None,
                "description": ""
            },
            "relationship_centric": {
                "value": True,
                "description": ""
            }
        }


class DatabaseAnalysisRequirements(BaseModel):
    """Project analysis result for requirement."""
    volume: DatabaseAnalysisVolume
    query_patterns: BoolWithDescription
    read: BoolWithDescription
    write: BoolWithDescription
    update: BoolWithDescription
    availability: BoolWithDescription

    class Config:
        json_schema_extra = {
            "example": {
                "volume": {
                    "value": ["SMALL"],
                    "description": ""
                },
                "query_patterns": {
                    "value": True,
                    "description": ""
                },
                "read": {
                    "value": False,
                    "description": ""
                },
                "write": {
                    "value": None,
                    "description": ""
                },
                "update": {
                    "value": False,
                    "description": ""
                },
                "availability": {
                    "value": True,
                    "description": ""
                }
            }
        }


class DatabaseAnalysisCost(BaseModel):
    """Project analysis result for cost."""
    commercial_allow: BoolWithDescription

    class Config:
        json_schema_extra = {
            "example": {
                "commercial_allow": {
                    "value": False,
                    "description": ""
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
                        "value": "StringOrNumber",
                        "description": ""
                    },
                    "structured_data": {
                        "value": True,
                        "description": ""
                    },
                    "time_series": {
                        "value": None,
                        "description": ""
                    },
                    "relationship_centric": {
                        "value": True,
                        "description": ""
                    }
                },
                "requirements": {
                    "volume": {
                        "value": ["SMALL", "MEDIUM"],
                        "description": ""
                    },
                    "query_patterns": {
                        "value": True,
                        "description": ""
                    },
                    "read": {
                        "value": False,
                        "description": ""
                    },
                    "write": {
                        "value": None,
                        "description": ""
                    },
                    "update": {
                        "value": True,
                        "description": ""
                    },
                    "availability": {
                        "value": True,
                        "description": ""
                    }
                },
                "cost": {
                    "commercial_allow": {
                        "value": False,
                        "description": ""
                    },
                }
            }
        }
