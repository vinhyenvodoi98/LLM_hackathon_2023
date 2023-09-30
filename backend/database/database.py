from typing import List

from backend.database.technologies import db_technologies
from backend.models.technology import DBTechnology


def get_all_technologies() -> List[DBTechnology]:
    return [
        DBTechnology.from_dict(technology)
        for technology in db_technologies
    ]
