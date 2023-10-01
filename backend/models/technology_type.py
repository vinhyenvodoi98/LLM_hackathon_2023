from dataclasses import dataclass

from pydantic import BaseModel


@dataclass(frozen=True)
class DBTechnologyType:
    """Wrapper for technology data from database."""
    index: int
    name: str
    enable: bool

    @staticmethod
    def from_dict(dict_value) -> "DBTechnologyType":
        return DBTechnologyType(
            index=dict_value["index"],
            name=dict_value["name"],
            enable=dict_value["enable"],
        )


class APITechnologyType(BaseModel):
    """Technology data type for API response."""
    index: int
    name: str
    enable: bool

    @staticmethod
    def from_db(db_value: DBTechnologyType) -> "APITechnologyType":
        return APITechnologyType(
            index=db_value.index,
            name=db_value.name,
            enable=db_value.enable,
        )

    class Config:
        json_schema_extra = {
            "example": {
                "index": 1,
                "name": "Database",
                "enable": True
            }
        }
