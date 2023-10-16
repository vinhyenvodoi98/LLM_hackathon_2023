import logging
import os
import time
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
    logging.info("Database analysis process start")
    start_time = time.perf_counter()
    if os.environ.get('BACKEND_DATA') == "MOCK":
        result = APIDatabaseAnalysisResponseModel(
            data_model=DatabaseAnalysisDataModel(
                data_type=DatabaseAnalysisDataType(
                    question="Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...",
                    explanation="Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...",
                    value=[
                        DatabaseAnalysisDataTypeEnum.DATETIME,
                        DatabaseAnalysisDataTypeEnum.TEXT
                    ],
                ),
                unstructured_data=BoolWithDescription(
                    question="Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...",
                    explanation="Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...",
                    value=True,
                ),
                time_series=BoolWithDescription(
                    question="Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...",
                    explanation="Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...",
                    value=True,
                )
            ),
            requirements=DatabaseAnalysisRequirements(
                volume=DatabaseAnalysisVolume(
                    question="Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...",
                    explanation="Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...",
                    value=[DatabaseAnalysisVolumeEnum.SMALL],
                ),
                fast_response_time=BoolWithDescription(
                    question="Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...",
                    explanation="Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...",
                    value=False,
                ),
                read_consistency=BoolWithDescription(
                    question="Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...",
                    explanation="Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...",
                    value=None,
                ),
                high_write_workloads=BoolWithDescription(
                    question="Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...",
                    explanation="Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...",
                    value=False,
                ),
            ),
            cost=DatabaseAnalysisCost(
                commercial_allow=BoolWithDescription(
                    question="Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...",
                    explanation="Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...",
                    value=False,
                ),
            )
        )
    else:
        analysis_result = get_requirement_analysis_result(post_request.requirement)
        result = APIDatabaseAnalysisResponseModel(
            data_model=DatabaseAnalysisDataModel(
                data_type=DatabaseAnalysisDataType(
                    question="Which type of data that you want to save into your DB?",
                    explanation=analysis_result["data_model"]["data_type"]["reason"],
                    value=analysis_result["data_model"]["data_type"]["value"]
                ),
                unstructured_data=BoolWithDescription(
                    question="Do your project contain unstructured data?",
                    explanation=analysis_result["data_model"]["unstructured_data"]["reason"],
                    value=analysis_result["data_model"]["unstructured_data"]["value"],
                ),
                time_series=BoolWithDescription(
                    question="Time series data is a collection of observations obtained through repeated measurements over time. Is your data time series data?",
                    explanation=analysis_result["data_model"]["time_series"]["reason"],
                    value=analysis_result["data_model"]["time_series"]["value"],
                )
            ),
            requirements=DatabaseAnalysisRequirements(
                volume=DatabaseAnalysisVolume(
                    question="How much data do you need to store? Less than 1 million records is small. Within 1 million and 100 million is medium. And above 100 million records is large.",
                    explanation=analysis_result["requirements"]["volume"]["reason"],
                    value=DatabaseAnalysisVolume.get_values(analysis_result["requirements"]["volume"]["value"]),
                ),
                fast_response_time=BoolWithDescription(
                    question="Do your project require microsecond response time from database? For example, leaderboards or session store may requires it.",
                    explanation=analysis_result["requirements"]["fast_response_time"]["reason"],
                    value=analysis_result["requirements"]["fast_response_time"]["value"],
                ),
                read_consistency=BoolWithDescription(
                    question="Is read consistency (any read request will return the most recent write) one of the most important requirements?",
                    explanation=analysis_result["requirements"]["read_consistency"]["reason"],
                    value=analysis_result["requirements"]["read_consistency"]["value"],
                ),
                high_write_workloads=BoolWithDescription(
                    question="Do you have a high-write workloads?",
                    explanation=analysis_result["requirements"]["high_write_workloads"]["reason"],
                    value=analysis_result["requirements"]["high_write_workloads"]["value"],
                ),
            ),
            cost=DatabaseAnalysisCost(
                commercial_allow=BoolWithDescription(
                    question="Are you willing to use commercial database?",
                    explanation=analysis_result["cost"]["commercial_allow"]["reason"],
                    value=analysis_result["cost"]["commercial_allow"]["value"],
                ),
            )
        )

    end_time = time.perf_counter()
    logging.info(
        "Database analysis process end after {0:.2f}s".format(end_time-start_time)
    )
    return result
