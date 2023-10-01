from enum import Enum
from typing import Optional, List

from pydantic import BaseModel


class APIAnalysisPostRequest(BaseModel):
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


class DatabaseAnalysisDataType(Enum):
    """Type of database data type."""
    Vector = "Vector"
    StringOrNumber = "StringOrNumber"
    FullText = "FullText"


class DatabaseAnalysisVolume(Enum):
    """Amount of database data volume."""
    # less than 1M records
    SMALL = "SMALL"
    # more than 1M records, less than 100M records
    MEDIUM = "MEDIUM"
    # more than 100M records
    HIGH = "HIGH"


class DatabaseAnalysisDataModel(BaseModel):
    """Project analysis result for data model."""
    data_type: DatabaseAnalysisDataType
    structured_data: Optional[bool]
    time_series: Optional[bool]
    relationship_centric: Optional[bool]

    class Config:
        json_schema_extra = {
            "example": {
                "data_type": "StringOrNumber",
                "structured_data": True,
                "time_series": None,
                "relationship_centric": True
            }
        }


class DatabaseAnalysisRequirements(BaseModel):
    """Project analysis result for requirement."""
    volume: List[DatabaseAnalysisVolume]
    query_patterns: Optional[bool]
    read: Optional[bool]
    write: Optional[bool]
    update: Optional[bool]
    availability: Optional[bool]

    class Config:
        json_schema_extra = {
            "example": {
                "volume": ["SMALL", "MEDIUM"],
                "query_patterns": True,
                "read": False,
                "write": None,
                "update": True,
                "availability": True
            }
        }


class DatabaseAnalysisCost(BaseModel):
    """Project analysis result for cost."""
    commercial_allow: Optional[bool] = False

    class Config:
        json_schema_extra = {
            "example": {
                "commercial_allow": False,
            }
        }


class APIDatabaseAnalysisResult(BaseModel):
    """Project analysis result for API."""
    data_model: DatabaseAnalysisDataModel
    requirements: DatabaseAnalysisRequirements
    cost: DatabaseAnalysisCost

    class Config:
        json_schema_extra = {
            "example": {
                "data_model": {
                    "data_type": "StringOrNumber",
                    "structured_data": True,
                    "time_series": None,
                    "relationship_centric": True
                },
                "requirements": {
                    "volume": ["SMALL", "MEDIUM"],
                    "query_patterns": True,
                    "read": False,
                    "write": None,
                    "update": True,
                    "availability": True
                },
                "cost": {
                    "commercial_allow": False,
                }
            }
        }
