import json
from typing import List

from llm.llm_base.output_parser import OutputParser
from llm.llm_base.prompt import BasicPrompt, FewShotPrompt, SelectingFewShotPrompt
from llm.config.prompt_config import *


def get_requirement_analysis_result(project_context: str) -> str:
    prompt = FewShotPrompt(requirement_analysis_prompt_config, project_context)
    analysis_result = prompt.get_result_with_text_model(temperature=0.5)
    result = OutputParser.json_extract(analysis_result)

    return result


def get_selecting_analysis_result(
    database_names: List[str],
    questions: dict
) -> str:
    question_str = json.dumps(questions)
    prompt_input = f"Databases: {', '.join(database_names)}\nAspects:\n{question_str}"
    prompt = SelectingFewShotPrompt(selecting_prompt_config, prompt_input)
    analysis_result = prompt.get_result_with_text_model(temperature=0.2)
    result = OutputParser.json_array_extract(analysis_result)

    return result


def get_basic_prompt_example_result(input: str) -> str:
    prompt = BasicPrompt(basic_prompt_example_config, input)
    result = prompt.get_result_with_text_model()

    return result


# if __name__ == '__main__':
#     response = get_selecting_analysis_result(
#         ["Redis", "Cloud Memorystore", "Firestore"],
#         {
#             "data_type": "Which type of data can this database store?",
#             "volume": "How suitable is this database for storing a large set of time series data?",
#             "read_consistency": "How good is this data's read consistency?",
#             "respond_time": "How good is this database response time?",
#             "maturity": "How mature is this database?"
#         }
#     )
#     print(response)
