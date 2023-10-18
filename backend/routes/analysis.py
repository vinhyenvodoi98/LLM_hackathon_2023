import os
from llm.llm_interactor import get_requirement_analysis_result

from fastapi import APIRouter

from models.analysis.database_analysis import (
    APIDatabaseAnalysisResponseModel,
    APIDatabaseAnalysisRequestModel,
    DatabaseAnalysisCost,
    DatabaseAnalysisDataModel,
    DatabaseAnalysisDataType,
    DatabaseAnalysisRequirements,
    DatabaseAnalysisVolume, DatabaseAnalysisDataTypeEnum, BoolWithDescription, DatabaseAnalysisVolumeEnum,
)

router = APIRouter()


@router.post(
    "/technology_type/{technology_type}",
    response_description="Analysis project requirements and return result factor by template",
    response_model=APIDatabaseAnalysisResponseModel,
    status_code=200
)
def analysis_project_requirements(
    technology_type: int,
    post_request: APIDatabaseAnalysisRequestModel
) -> APIDatabaseAnalysisResponseModel:
    """Analysis project requirements and return result template."""
    # if technology type is not database
    if technology_type != 1:
        raise NotImplementedError("App only support db analysis for now.")
    # TODO: add perf_counter logging
    if os.environ.get('BACKEND_DATA') == "MOCK":
        analysis_result = {
            "data_model": {
                "data_type": {
                    "value": [
                        "Text",
                        "Number",
                    ],
                    "reason": "Foo bar"
                },
                "unstructured_data": {
                    "value": True,
                    "reason": "Foo bar"
                },
                "time_series": {
                    "value": False,
                    "reason": "Foo bar"
                },
            },
            "requirements": {
                "volume":  {
                    "value": ["medium"],
                    "reason": "Foo bar",
                },
                "fast_response_time": {
                    "value": None,
                    "reason": "Foo bar"
                },
                "read_consistency": {
                    "value": False,
                    "reason": "Foo bar"
                },
                "high_write_workloads": {
                    "value": True,
                    "reason": "Foo bar"
                }
            },
            "cost": {
                "commercial_allow": {
                    "value": False,
                    "reason": "Foo bar"
                }
            }
        }
    else:
        # FIXME: volume is a list but only return one value
        analysis_result = get_requirement_analysis_result(post_request.requirement)

    return APIDatabaseAnalysisResponseModel.from_analysis_result(analysis_result)
