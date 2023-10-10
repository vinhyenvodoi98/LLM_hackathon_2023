from typing import List, Optional

from pydantic import BaseModel

from models.analysis.database_analysis import (
    DatabaseAnalysisVolumeEnum,
    DatabaseAnalysisDataTypeEnum
)


class APIAnalysisRequestModel(BaseModel):
    data_type: List[DatabaseAnalysisDataTypeEnum]
    unstructured_data: Optional[bool]
    time_series: Optional[bool]
    relationship_centric: Optional[bool]
    volume: List[DatabaseAnalysisVolumeEnum]
    complex_query_patterns: Optional[bool]
    read_consistency: Optional[bool]
    high_write_workloads: Optional[bool]
    high_availability: Optional[bool]
    commercial_allow: Optional[bool]

    def get_value_from_field(self, field: str):
        """Get value."""
        for key, value in self.__dict__.items():
            if field != key:
                continue
            return value
        return None

    class Config:
        json_schema_extra = {
            "data_type": ["Text", "Number"],
            "unstructured_data": True,
            "time_series": False,
            "relationship_centric": True,
            "volume": ["small"],
            "complex_query_patterns": False,
            "read_consistency": True,
            "high_write_workloads": True,
            "high_availability": True,
            "commercial_allow": True
        }


class APISelectingRequestModel(BaseModel):
    context: str
    analysis: APIAnalysisRequestModel

    class Config:
        json_schema_extra = {
            "example": {
                "context": f"My project is an IoT project "
                           f"which uses sensors to record the value of outdoor temperature, humidity "
                           f"and then display it on a dashboard. "
                           f"The dashboard should allow data export and graph customization.",
                "analysis": {
                    "data_type": ["Text", "Number"],
                    "unstructured_data": True,
                    "time_series": False,
                    "relationship_centric": True,
                    "volume": ["small"],
                    "complex_query_patterns": False,
                    "read_consistency": True,
                    "high_write_workloads": True,
                    "high_availability": True,
                    "commercial_allow": True
                }
            }
        }


class APISelectingDatabaseModel(BaseModel):
    rank: int
    name: str
    website: str
    # TODO: do we need to display other factor
    reason: str

    class Config:
        json_schema_extra = {
            "example": {
                "rank": 1,
                "name": "MySQL",
                "website": "https://www.mysql.com",
                "reason": "This database is suitable for commercial need of accounting service, ..."
            }
        }


class APISelectingRespondModel(BaseModel):
    # FIXME: need to be more abstract
    results: Optional[List[APISelectingDatabaseModel]]

    class Config:
        json_schema_extra = {
            "example": {
                "results": [
                    {
                        "rank": 1,
                        "name": "MySQL",
                        "website": "https://www.mysql.com",
                        "reason": "This database is suitable for commercial need of accounting service, ..."
                    },
                    {
                        "rank": 2,
                        "name": "MySQL",
                        "website": "https://www.mysql.com",
                        "reason": "This database is suitable for commercial need of accounting service, ..."
                    },
                    {
                        "rank": 3,
                        "name": "MySQL",
                        "website": "https://www.mysql.com",
                        "reason": "This database is suitable for commercial need of accounting service, ..."
                    },
                ]
            }
        }
