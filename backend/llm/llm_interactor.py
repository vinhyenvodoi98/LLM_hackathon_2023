from llm.llm_base.output_parser import OutputParser
from llm.llm_base.prompt import BasicPrompt, FewShotPrompt, SelectingFewShotPrompt
from llm.config.prompt_config import *


def get_requirement_analysis_result(input: str) -> str:
    prompt = FewShotPrompt(requirement_analysis_prompt_config, input)
    analysis_result = prompt.get_result_with_text_model()
    result = OutputParser.json_extract(analysis_result)

    return result

def get_selecting_analysis_result(input: str) -> str:
    prompt = SelectingFewShotPrompt(selecting_prompt_config, input)
    analysis_result = prompt.get_result_with_text_model()
    result = OutputParser.json_array_extract(analysis_result)

    return result

def get_basic_prompt_example_result(input: str) -> str:
    prompt = BasicPrompt(basic_prompt_example_config, input)
    result = prompt.get_result_with_text_model()

    return result

# Test
# response = get_selecting_analysis_result("Databases: Redis, Cloud Memorystore, Firestore\nAspects:\n{\n    \"data_type\": \"Which type of data can this database store?\",\n    \"volume\": \"How suitable is this database for storing a large set of time series data?\",\n    \"read_consistency\": \"How good is this data's read consistency?\",\n    \"respond_time\": \"How good is this database response time?\",\n    \"maturity\": \"How mature is this database?\"\n}")
# print(response)
# print(response[0]["database"])