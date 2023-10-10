from fastapi import APIRouter

from models.selecting import APISelectingRequestModel, APISelectingRespondModel, APISelectingDatabaseModel
from technologies_selectors.database_technologies_selector import DatabaseTechnologiesSelector

router = APIRouter()


@router.post(
    "/technology_type/{technology_type}",
    response_description="Select top k best technologies by factors",
    response_model=APISelectingRespondModel,
    status_code=200
)
def analysis_project_requirements(
    technology_type: int,
    post_request: APISelectingRequestModel,
    k: int = 3,
) -> APISelectingRespondModel:
    """Analysis result factors and return top k best technologies."""
    # if technology type is not database
    if technology_type != 1:
        raise NotImplementedError("App only support db analysis for now.")
    selector = DatabaseTechnologiesSelector()
    top_k_technologies = selector.get_top_k_technologies(
        analysis=post_request.analysis,
        k=k
    )
    # TODO: compare those technologies with each other to add reason
    return APISelectingRespondModel(
        results=[
            APISelectingDatabaseModel(
                rank=i+1,
                name=technology["name"],
                website=technology["website"],
                reason="Implement reason here"
            )
            for i, technology in enumerate(top_k_technologies)
        ]
    )
