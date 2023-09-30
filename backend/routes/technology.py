from typing import List

from fastapi import APIRouter

from database.database import get_all_technologies
from models.technology import Technology

router = APIRouter()


@router.get(
    "/",
    response_description="Get all technologies",
    response_model=List[Technology],
    status_code=200
)
def get_technologies():
    db_technologies = get_all_technologies()
    return [
        Technology.from_db(db_technology)
        for db_technology in db_technologies
    ]
