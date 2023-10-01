import logging
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
    # TODO: implement analysis here
    result = APIDatabaseAnalysisResponseModel(
        data_model=DatabaseAnalysisDataModel(
            data_type=DatabaseAnalysisDataType(
                value=DatabaseAnalysisDataTypeEnum.StringOrNumber,
            ),
            structured_data=BoolWithDescription(
                value=True,
            ),
            time_series=BoolWithDescription(
                value=True,
            ),
            relationship_centric=BoolWithDescription(
                value=True,
            ),
        ),
        requirements=DatabaseAnalysisRequirements(
            volume=DatabaseAnalysisVolume(
                value=[DatabaseAnalysisVolumeEnum.SMALL],
            ),
            query_patterns=BoolWithDescription(
                value=False,
            ),
            read=BoolWithDescription(
                value=None,
            ),
            write=BoolWithDescription(
                value=False,
            ),
            update=BoolWithDescription(
                value=False,
            ),
            availability=BoolWithDescription(
                value=False,
            ),
        ),
        cost=DatabaseAnalysisCost(
            commercial_allow=BoolWithDescription(
                value=False,
            ),
        )
    )
    end_time = time.perf_counter()
    logging.info(
        "Database analysis process end after {0:.2f}s".format(end_time-start_time)
    )
    return result
