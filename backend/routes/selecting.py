from fastapi import APIRouter

from models.selecting import APISelectingRequestModel

router = APIRouter()

@router.post(
    "/technology_type/{technology_type}",
    response_description="Select top k best technologies by factors",
    response_model=,
    status_code=200
)
def analysis_project_requirements(
    technology_type: int,
    top_k: int = 3,
    post_request: APISelectingRequestModel
) -> :
    """Analysis result factors and return top k best technologies."""
    # if technology type is not database
    if technology_type != 1:
        raise NotImplementedError("App only support db analysis for now.")