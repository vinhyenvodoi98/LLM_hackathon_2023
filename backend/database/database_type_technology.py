from typing import List

from database.database_type_technologies import all_data, general_purpose_sql, time_series, in_memory, \
    general_purpose_no_sql


def remove_question_key(raw_db_attributes: dict) -> dict:
    """Remove question key"""
    db_attributes = {}
    for key, attr in raw_db_attributes.items():
        if not isinstance(attr, dict):
            db_attributes[key] = attr
            continue
        if "answer" in attr:
            db_attributes[key] = attr["answer"]
        else:
            db_attributes[key] = remove_question_key(attr)
    return db_attributes


def load_database_type_technologies(all_technologies) -> List[dict]:
    # TODO: make dataclasses ???
    technologies = [
        remove_question_key(database_type_technology)
        for database_type_technology in all_technologies
    ]
    technologies.sort(key=lambda tech: tech["index"])
    return technologies


all_database_technologies = load_database_type_technologies(all_data)
general_purpose_sql_database_technologies = load_database_type_technologies(general_purpose_sql)
general_purpose_no_sql_database_technologies = load_database_type_technologies(general_purpose_no_sql)
time_series_database_technologies = load_database_type_technologies(time_series)
in_memory_database_technologies = load_database_type_technologies(in_memory)
