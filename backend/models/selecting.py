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
    volume: DatabaseAnalysisVolumeEnum
    fast_response_time: Optional[bool]
    read_consistency: Optional[bool]
    high_write_workloads: Optional[bool]
    commercial_allow: Optional[bool]

    class Config:
        json_schema_extra = {
            "example": {
                "data_type": ["Text", "Number"],
                "unstructured_data": True,
                "time_series": False,
                "volume": "small",
                "fast_response_time": False,
                "read_consistency": True,
                "high_write_workloads": True,
                "commercial_allow": True
            }
        }


class APISelectingDatabaseModel(BaseModel):
    database: str
    website: str
    data_type: str
    volume: str
    read_consistency: str
    respond_time: str
    maturity: str
    open_source: str
    commercial: str

    class Config:
        json_schema_extra = {
            "example": {
                "database": "Cloud SQL",
                "website": "...",
                "data_type": "Numeric data, String data, Date and time data, Binary data, JSON data.",
                "volume": "Cloud SQL is suitable for storing a large set of time series data. It is a fully managed service that offers scalability, reliability, and security.",
                "read_consistency": "Cloud SQL offers strong read consistency. This means that reads are always guaranteed to return the most recent committed data.",
                "respond_time": "Cloud SQL offers good response time. The latency for reads and writes is typically in the range of milliseconds.",
                "maturity": "Cloud SQL is a mature service. It has been available since 2011 and is used by many large organizations.",
                "open_source": "Cloud SQL does not have open source version.",
                "commercial": "Cloud SQL has commercial version."
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
                        "database": "Cloud SQL",
                        "website": "...",
                        "data_type": "Numeric data, String data, Date and time data, Binary data, JSON data.",
                        "volume": "Cloud SQL is suitable for storing a large set of time series data. It is a fully managed service that offers scalability, reliability, and security.",
                        "read_consistency": "Cloud SQL offers strong read consistency. This means that reads are always guaranteed to return the most recent committed data.",
                        "respond_time": "Cloud SQL offers good response time. The latency for reads and writes is typically in the range of milliseconds.",
                        "maturity": "Cloud SQL is a mature service. It has been available since 2011 and is used by many large organizations.",
                        "open_source": "Cloud SQL does not have open source version.",
                        "commercial": "Cloud SQL has commercial version."
                    },
                    {
                        "database": "Microsoft SQL Server",
                        "website": "...",
                        "data_type": "Numeric data, String data, Date and time data, Binary data, JSON data.",
                        "volume": "Microsoft SQL Server is suitable for storing a large set of time series data. It is a powerful and scalable database that can handle large amounts of data.",
                        "read_consistency": "Microsoft SQL Server offers strong read consistency. This means that reads are always guaranteed to return the most recent committed data.",
                        "respond_time": "Microsoft SQL Server offers good response time. The latency for reads and writes is typically in the range of milliseconds.",
                        "maturity": "Microsoft SQL Server is a mature database. It has been available since 1989 and is used by many large organizations.",
                        "open_source": "Microsoft SQL Server does not have open source version.",
                        "commercial": "Microsoft SQL Server has commercial version."
                    },
                    {
                        "database": "Amazon Aurora",
                        "website": "...",
                        "data_type": "Numeric data, String data, Date and time data, Binary data, JSON data.",
                        "volume": "Amazon Aurora is suitable for storing a large set of time series data. It is a fully managed service that offers scalability, reliability, and security.",
                        "read_consistency": "Amazon Aurora offers strong read consistency. This means that reads are always guaranteed to return the most recent committed data.",
                        "respond_time": "Amazon Aurora offers good response time. The latency for reads and writes is typically in the range of milliseconds.",
                        "maturity": "Amazon Aurora is a mature service. It has been available since 2014 and is used by many large organizations.",
                        "open_source": "Amazon Aurora does not have open source version.",
                        "commercial": "Amazon Aurora has commercial version."
                    }
                ]
            }
        }

    @staticmethod
    def from_database_and_comparison(
        top_k_databases: List[dict],
        comparison_results: List[dict]
    ) -> "APISelectingRespondModel":
        """."""
        results = []
        for comparison_result in comparison_results:
            database_metadata = [
                database for database in top_k_databases
                if database["name"] == comparison_result["database"]
            ][0]
            if database_metadata["open_source"]:
                open_source = f"{database_metadata['name']} has open source version."
            else:
                open_source = f"{database_metadata['name']} does not have open source version."
            if database_metadata["commercial"]:
                commercial = f"{database_metadata['name']} has commercial version."
            else:
                commercial = f"{database_metadata['name']} does not have commercial version."
            results.append(
                APISelectingDatabaseModel(
                    database=database_metadata["name"],
                    website=database_metadata["website"],
                    data_type=comparison_result["data_type"],
                    volume=comparison_result["volume"],
                    read_consistency=comparison_result["read_consistency"],
                    respond_time=comparison_result["respond_time"],
                    maturity=comparison_result["maturity"],
                    open_source=open_source,
                    commercial=commercial
                )
            )
        return APISelectingRespondModel(results=results)
