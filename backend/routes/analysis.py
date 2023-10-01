import logging
import time

from fastapi import APIRouter

from models.analysis.database_analysis import (
    APIDatabaseAnalysisResult,
    APIAnalysisPostRequest,
    DatabaseAnalysisCost,
    DatabaseAnalysisDataModel,
    DatabaseAnalysisDataType,
    DatabaseAnalysisRequirements,
    DatabaseAnalysisVolume,
)

router = APIRouter()


@router.post(
    "/technology_type/{technology_type}",
    response_description="Analysis project requirements and return result template",
    response_model=APIDatabaseAnalysisResult,
    status_code=200
)
def analysis_project_requirements(
    technology_type: int,
    post_request: APIAnalysisPostRequest
) -> APIDatabaseAnalysisResult:
    """Analysis project requirements and return result template."""
    # if technology type is not database
    if technology_type != 1:
        raise NotImplementedError("App only support db analysis for now.")
    logging.info("Database analysis process start")
    start_time = time.perf_counter()
    # TODO: implement analysis here
    result = APIDatabaseAnalysisResult(
        data_model=DatabaseAnalysisDataModel(
            data_type=DatabaseAnalysisDataType.StringOrNumber,
            structured_data=True,
            time_series=True,
            relationship_centric=True,
        ),
        requirements=DatabaseAnalysisRequirements(
            volume=[DatabaseAnalysisVolume.SMALL],
            query_patterns=True,
            read=True,
            write=True,
            update=True,
            availability=True,
        ),
        cost=DatabaseAnalysisCost(
            commercial_allow=True,
        )
    )
    end_time = time.perf_counter()
    logging.info(
        "Database analysis process end after {0:.2f}s".format(end_time-start_time)
    )
    return result
