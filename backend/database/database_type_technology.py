import json
import os
from typing import List

from database.database_type_technologies import all_data as all_database_type_technologies


def remove_question_key(raw_db_attributes: dict) -> dict:
    """Remove question key"""
    db_attributes = {}
    for key, attr in raw_db_attributes.items():
        if not isinstance(attr, dict):
            db_attributes[key] = attr
        else:
            db_attributes[key] = attr["answer"]
    return db_attributes


def load_database_type_technologies() -> List[dict]:
    # TODO: make dataclasses ???
    technologies = [
        remove_question_key(database_type_technology)
        for database_type_technology in all_database_type_technologies
    ]
    technologies.sort(key=lambda tech: tech["index"])
    return technologies


db_database_type_technologies = load_database_type_technologies()
