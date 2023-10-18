import os

from fastapi import APIRouter

from database.database_type_technologies import amazon_aurora, cloud_sql, microsoft_sql_server
from database.database_type_technology import load_database_type_technologies
from llm.llm_interactor import get_selecting_analysis_result
from models.selecting import APIAnalysisRequestModel, APISelectingRespondModel
from technologies_selectors.database_technologies_selector import DatabaseTechnologiesSelector

router = APIRouter()


def _generate_comparison_questions(analysis: APIAnalysisRequestModel) -> dict:
    """."""
    data_type = "SQL"
    if analysis.time_series:
        data_type = "time series"
    elif analysis.unstructured_data:
        data_type = "NoSQL"

    return {
        "data_type": "Which type of data can this database store?",
        "volume": f"How suitable is this database for storing a {analysis.volume.value} set of {data_type} data?",
        "read_consistency": "How good is this data's read consistency?",
        "respond_time": "How good is this database response time?",
        "maturity": "How mature is this database?"
    }


@router.post(
    "/technology_type/{technology_type}",
    response_description="Select top k best technologies by factors",
    response_model=APISelectingRespondModel,
    status_code=200
)
def analysis_project_requirements(
    technology_type: int,
    post_request: APIAnalysisRequestModel,
    k: int = 3,
) -> APISelectingRespondModel:
    """Analysis result factors and return top k best technologies."""
    # if technology type is not database
    if technology_type != 1:
        raise NotImplementedError("App only support db analysis for now.")
    # TODO: add perf_counter logging
    if os.environ.get('BACKEND_DATA') == "MOCK":
        top_k_databases = load_database_type_technologies(
            [cloud_sql, microsoft_sql_server, amazon_aurora]
        )
        comparison_results = [
            {
                "database": "Cloud SQL",
                "website": "...",
                "data_type": "Numeric data, String data, Date and time data, Binary data, JSON data.",
                "volume": "Cloud SQL is suitable for storing a large set of time series data. It is a fully managed service that offers scalability, reliability, and security.",
                "read_consistency": "Cloud SQL offers strong read consistency. This means that reads are always guaranteed to return the most recent committed data.",
                "respond_time": "Cloud SQL offers good response time. The latency for reads and writes is typically in the range of milliseconds.",
                "maturity": "Cloud SQL is a mature service. It has been available since 2011 and is used by many large organizations.",
            },
            {
                "database": "Microsoft SQL Server",
                "website": "...",
                "data_type": "Numeric data, String data, Date and time data, Binary data, JSON data.",
                "volume": "Microsoft SQL Server is suitable for storing a large set of time series data. It is a powerful and scalable database that can handle large amounts of data.",
                "read_consistency": "Microsoft SQL Server offers strong read consistency. This means that reads are always guaranteed to return the most recent committed data.",
                "respond_time": "Microsoft SQL Server offers good response time. The latency for reads and writes is typically in the range of milliseconds.",
                "maturity": "Microsoft SQL Server is a mature database. It has been available since 1989 and is used by many large organizations.",
            },
            {
                "database": "Amazon Aurora",
                "website": "...",
                "data_type": "Numeric data, String data, Date and time data, Binary data, JSON data.",
                "volume": "Amazon Aurora is suitable for storing a large set of time series data. It is a fully managed service that offers scalability, reliability, and security.",
                "read_consistency": "Amazon Aurora offers strong read consistency. This means that reads are always guaranteed to return the most recent committed data.",
                "respond_time": "Amazon Aurora offers good response time. The latency for reads and writes is typically in the range of milliseconds.",
                "maturity": "Amazon Aurora is a mature service. It has been available since 2014 and is used by many large organizations.",
            }
        ]
    else:
        # TODO: implement
        selector = DatabaseTechnologiesSelector()
        top_k_databases = selector.get_top_k_technologies(
            analysis=post_request,
            k=k
        )
        database_names = [
            database["name"]
            for database in top_k_databases
        ]
        questions = _generate_comparison_questions(post_request)
        comparison_results = get_selecting_analysis_result(database_names, questions)

    return APISelectingRespondModel.from_database_and_comparison(
        top_k_databases, comparison_results
    )
