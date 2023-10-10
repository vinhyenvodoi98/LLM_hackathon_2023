from typing import List

from database import get_all_database_type_technologies
from models.selecting import APIAnalysisRequestModel


class DatabaseTechnologiesSelector:
    # TODO: create base class

    def __init__(self):
        self.all_databases = get_all_database_type_technologies()
        self.score_fields = [
            "time_series",
            "relationship_centric",
            "read_consistency",
            "complex_query_patterns",
            "high_write_workloads",
            "high_availability"
        ]

    def get_top_k_technologies(
        self, analysis: APIAnalysisRequestModel, k=3
    ) -> List[dict]:
        """Get top k highest score technologies.

        Args:
            requirements: requirement send from user to api to get the most suitable technologies
            k: number of technologies to take

        Return:
            List of technologies
        """
        satisfied_databases = self.filter_unsatisfied_technologies(analysis, self.all_databases)
        databases_score = self.calculate_scores(analysis, satisfied_databases)
        databases_score = sorted(databases_score, key=lambda database_score: database_score["score"], reverse=True)
        top_k_databases_score = databases_score[:k]
        top_k_databases_indexes = [database_score["index"] for database_score in top_k_databases_score]
        top_k_databases = []
        for database in satisfied_databases:
            if database["index"] not in top_k_databases_indexes:
                continue
            score = [
                database_score["score"]
                for database_score in top_k_databases_score
                if database_score["index"] == database["index"]
            ][0]
            top_k_databases.append({
                **database,
                "score": score
            })
        return top_k_databases

    @staticmethod
    def filter_unsatisfied_technologies(
        analysis: APIAnalysisRequestModel, databases: List[dict]
    ) -> List[dict]:
        """."""
        # FIXME: hardcode
        # filter databases that contains all required data types
        required_data_types = analysis.data_type
        dt_databases = []
        if required_data_types is None:
            satisfied_databases = databases
        else:
            for database in databases:
                if all(
                    data_types.value in database["data_type"]
                    for data_types in required_data_types
                ):
                    dt_databases.append(database)
        # filter by target data volume
        required_data_volume = analysis.volume
        satisfied_databases = []
        if required_data_types is not None:
            for database in dt_databases:
                if all(
                    volume.value in database["volume"]
                    for volume in required_data_volume
                ):
                    satisfied_databases.append(database)

        # filter databases by unstructured data compatibility
        if analysis.unstructured_data:
            satisfied_databases = [
                database
                for database in satisfied_databases
                if database["unstructured_data"]
            ]
        # filter by high_availability, open_source, commercial
        if analysis.high_availability:
            satisfied_databases = [
                database
                for database in satisfied_databases
                if database["high_availability"]
            ]
        # filter by open source only
        if not analysis.commercial_allow and analysis.commercial_allow is not None:
            satisfied_databases = [
                database
                for database in satisfied_databases
                if database["open_source"]
            ]

        return satisfied_databases

    def calculate_scores(self, analysis: APIAnalysisRequestModel, databases: List[dict]):
        """Calculate score for each database for ranking."""
        # scores = [ {index: int, score: float} ]
        # TODO: dataclass
        scores = []
        for database in databases:
            score = 0
            for field in self.score_fields:
                analysis_value = analysis.get_value_from_field(field)
                if analysis_value:
                    score += database[field]
            scores.append(
                {
                    "index": database["index"],
                    "score": score
                }
            )
        return scores
