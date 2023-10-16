from enum import Enum
from typing import List, Optional

from dataclasses import dataclass

from database.database_type_technology import general_purpose_sql_database_technologies, \
    general_purpose_no_sql_database_technologies, time_series_database_technologies, in_memory_database_technologies
from models.analysis.database_analysis import DatabaseAnalysisVolumeEnum, DatabaseAnalysisDataTypeEnum
from models.selecting import APIAnalysisRequestModel


class DatabaseTypeEnum(Enum):
    """Type of database data type."""
    GENERAL_SQL = 0
    GENERAL_NOSQL = 1
    TIME_SERIES = 2
    IN_MEMORY = 3


@dataclass(frozen=True)
class DatabaseType:
    """Wrapper for technology data from database."""
    primary_type: DatabaseTypeEnum
    sql: bool

    def get_primary_type(self) -> DatabaseTypeEnum:
        return self.primary_type

    def get_secondary_type(self) -> Optional[DatabaseTypeEnum]:
        if self.primary_type == DatabaseTypeEnum.GENERAL_SQL or self.primary_type == DatabaseTypeEnum.GENERAL_NOSQL:
            return None
        if self.primary_type == DatabaseTypeEnum.IN_MEMORY:
            return DatabaseTypeEnum.GENERAL_NOSQL
        # time series
        return DatabaseTypeEnum.GENERAL_SQL if self.sql else DatabaseTypeEnum.GENERAL_NOSQL

    def get_primary_database_list(self):
        return DatabaseType.get_database_List(self.primary_type)

    def get_secondary_database_list(self):
        return DatabaseType.get_database_List(self.get_secondary_type())

    @staticmethod
    def get_database_List(database_type_enum: DatabaseTypeEnum) -> List[dict]:
        if database_type_enum == DatabaseTypeEnum.GENERAL_SQL:
            return general_purpose_sql_database_technologies
        if database_type_enum == DatabaseTypeEnum.GENERAL_NOSQL:
            return general_purpose_no_sql_database_technologies
        if database_type_enum == DatabaseTypeEnum.TIME_SERIES:
            return time_series_database_technologies
        if database_type_enum == DatabaseTypeEnum.IN_MEMORY:
            return in_memory_database_technologies


class DatabaseTechnologiesSelector:
    # TODO: create base class

    def get_top_k_technologies(
        self, analysis: APIAnalysisRequestModel, k=3
    ) -> List[dict]:
        """Get top k highest score technologies.

        Args:
            analysis: requirement send from user to api to get the most suitable technologies
            k: number of technologies to take

        Return:
            List of technologies
        """
        database_type = self.get_database_type(analysis)
        # primary
        primary_db_list = database_type.get_primary_database_list()
        primary_db_list = self.remove_unsatisfied_technologies(analysis, primary_db_list)
        primary_db_score = self.calculate_scores(analysis, primary_db_list)
        primary_db_score = sorted(primary_db_score, key=lambda database_score: database_score["score"], reverse=True)
        print(f"primary_db_score: {primary_db_score}")
        # secondary
        secondary_db_list = database_type.get_secondary_database_list()
        if secondary_db_list is None:
            return []
        secondary_db_list = self.remove_unsatisfied_technologies(analysis, secondary_db_list)
        secondary_db_score = self.calculate_scores(analysis, secondary_db_list)
        secondary_db_score = sorted(secondary_db_score, key=lambda database_score: database_score["score"], reverse=True)
        print(f"secondary_db_score: {secondary_db_score}")
        return []

    def get_database_type(self, analysis: APIAnalysisRequestModel) -> DatabaseType:
        """Get the most suitable database type."""
        # FIXME: hardcode
        is_sql = False if analysis.unstructured_data else True
        is_in_memory = analysis.fast_response_time if analysis.fast_response_time else False
        is_time_series = analysis.time_series if analysis.time_series else False
        if is_in_memory:
            return DatabaseType(
                primary_type=DatabaseTypeEnum.IN_MEMORY,
                sql=is_sql
            )
        if is_time_series:
            return DatabaseType(
                primary_type=DatabaseTypeEnum.TIME_SERIES,
                sql=is_sql
            )
        if is_sql:
            return DatabaseType(
                primary_type=DatabaseTypeEnum.GENERAL_SQL,
                sql=is_sql
            )
        return DatabaseType(
            primary_type=DatabaseTypeEnum.GENERAL_NOSQL,
            sql=is_sql
        )

    @staticmethod
    def remove_unsatisfied_technologies(
        analysis: APIAnalysisRequestModel, databases: List[dict]
    ) -> List[dict]:
        """."""
        # FIXME: hardcode
        # filter databases that contains all required data types
        required_data_types = analysis.data_type
        satisfied_databases = []
        if required_data_types is None:
            satisfied_databases = databases
        else:
            for database in databases:
                if all(
                    data_types.value in database["data_type"]
                    for data_types in required_data_types
                ):
                    satisfied_databases.append(database)

        # filter by open source only
        if not analysis.commercial_allow and analysis.commercial_allow is not None:
            satisfied_databases = [
                database
                for database in satisfied_databases
                if database["open_source"]
            ]

        return satisfied_databases

    @staticmethod
    def calculate_scores(analysis: APIAnalysisRequestModel, databases: List[dict]):
        """Calculate score for each database for ranking."""
        # scores = [ {index: int, score: float} ]
        is_time_series = analysis.time_series if analysis.time_series else False
        volume_key = "time_series" if is_time_series else "sql"
        scores = []
        # FIXME: hard code
        for database in databases:
            score = 0
            score += database["read_consistency"] if analysis.read_consistency else (database["read_consistency"] * 0.5)
            score += database["high_write_workloads"] if analysis.high_write_workloads else (database["high_write_workloads"] * 0.5)
            for target_volume in analysis.volume:
                if target_volume == DatabaseAnalysisVolumeEnum.SMALL:
                    score += database["small_volume"][volume_key]
                if target_volume == DatabaseAnalysisVolumeEnum.MEDIUM:
                    score += database["small_volume"][volume_key]
                if target_volume == DatabaseAnalysisVolumeEnum.HIGH:
                    score += database["large_volume"][volume_key]
            score *= (database["maturity"] / 10)
            scores.append(
                {
                    "index": database["index"],
                    "name": database["name"],
                    "score": score
                }
            )
        return scores


if __name__ == '__main__':
    selector = DatabaseTechnologiesSelector()
    analysis = APIAnalysisRequestModel(
        data_type=[
            DatabaseAnalysisDataTypeEnum.DATETIME,
            DatabaseAnalysisDataTypeEnum.TEXT,
            DatabaseAnalysisDataTypeEnum.NUMBER
        ],
        unstructured_data=True,
        time_series=True,
        volume=[DatabaseAnalysisVolumeEnum.MEDIUM, DatabaseAnalysisVolumeEnum.HIGH],
        fast_response_time=False,
        read_consistency=True,
        high_write_workloads=True,
        commercial_allow=False
    )
    selector.get_top_k_technologies(analysis)
