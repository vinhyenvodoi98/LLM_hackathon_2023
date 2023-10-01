from typing import List

from fastapi import APIRouter

from database import get_all_technology_types
from models.technology_type import APITechnologyType

router = APIRouter()


@router.get(
    "/",
    response_description="Get all technology types",
    response_model=List[APITechnologyType],
    status_code=200
)
def get_technology_types():
    """Get all technology types from database and return."""
    db_technologies = get_all_technology_types()
    return [
        APITechnologyType.from_db(db_technology)
        for db_technology in db_technologies
    ]
