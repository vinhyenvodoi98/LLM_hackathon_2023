import logging
import os
import time

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
    response_description="Analysis project requirements and return result template",
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
    if os.getenv('BACKEND_DATA') == "MOCK":
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
                ),
                relationship_centric=BoolWithDescription(
                    question="Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...",
                    explanation="Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...",
                    value=True,
                ),
            ),
            requirements=DatabaseAnalysisRequirements(
                volume=DatabaseAnalysisVolume(
                    question="Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...",
                    explanation="Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...",
                    value=[DatabaseAnalysisVolumeEnum.SMALL],
                ),
                complex_query_patterns=BoolWithDescription(
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
                high_availability=BoolWithDescription(
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
        # TODO: implement analysis here
        raise NotImplementedError()
    end_time = time.perf_counter()
    logging.info(
        "Database analysis process end after {0:.2f}s".format(end_time-start_time)
    )
    return result
