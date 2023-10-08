from typing import List

from pydantic import BaseModel

from models.analysis.database_analysis import APIDatabaseAnalysisResponseModel


class APISelectingRequestModel(BaseModel):
    project_context: str
    analysis_result: APIDatabaseAnalysisResponseModel

    class Config:
        json_schema_extra = {
            "example": {
                "project_context": f"My project is an IoT project "
                                   f"which uses sensors to record the value of outdoor temperature, humidity "
                                   f"and then display it on a dashboard. "
                                   f"The dashboard should allow data export and graph customization.",
                "analysis_result": {
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
        }


class APISelectingRespondModel(BaseModel):
    results: List[dict]

    class Config:
        json_schema_extra = {
            "example": {
                "context": f"My project is an IoT project "
                           f"which uses sensors to record the value of outdoor temperature, humidity "
                           f"and then display it on a dashboard. "
                           f"The dashboard should allow data export and graph customization."
            }
        }