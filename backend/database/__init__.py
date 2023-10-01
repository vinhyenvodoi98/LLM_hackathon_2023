from typing import List

from database.technologies import db_technology_types
from models.technology_type import DBTechnologyType


def get_all_technology_types() -> List[DBTechnologyType]:
    return [
        DBTechnologyType.from_dict(technology)
        for technology in db_technology_types
    ]
