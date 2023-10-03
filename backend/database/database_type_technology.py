import json
import os
from pprint import pprint


def remove_question_key(raw_db_attributes: dict) -> dict:
    """Remove question key"""
    db_attributes = {}
    for key, attr in raw_db_attributes.items():
        if not isinstance(attr, dict):
            db_attributes[key] = attr
        else:
            db_attributes[key] = attr["answer"]
    return db_attributes


def load_database_type_technologies():
    database_type_technologies_dir = "database_type_technologies/"
    technologies = []
    for file_name in os.listdir(database_type_technologies_dir):
        file_path = os.path.join(database_type_technologies_dir, file_name)
        with open(file_path) as f:
            technologies.append(remove_question_key(json.load(f)))
    technologies.sort(key=lambda tech: tech["index"])
    return technologies


db_database_type_technologies = load_database_type_technologies()
