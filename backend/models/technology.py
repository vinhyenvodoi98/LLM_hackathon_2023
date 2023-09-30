from dataclasses import dataclass

from pydantic import BaseModel


@dataclass(frozen=True)
class DBTechnology:
    index: int
    name: str
    enable: bool

    @staticmethod
    def from_dict(dict_value) -> "DBTechnology":
        return DBTechnology(
            index=dict_value["index"],
            name=dict_value["name"],
            enable=dict_value["enable"],
        )


class Technology(BaseModel):
    index: int
    name: str
    enable: bool

    @staticmethod
    def from_db(db_value: DBTechnology) -> "Technology":
        return Technology(
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
