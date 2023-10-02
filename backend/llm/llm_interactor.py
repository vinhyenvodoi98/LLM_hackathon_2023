from llm_base.prompt import FewShotPrompt, BasicPrompt
from llm_base.output_parser import OutputParser
from config.prompt_config import *

def get_requirement_analysis_result(input: str) -> str:
    prompt = FewShotPrompt(requirement_analysis_prompt_config, input)
    result = prompt.get_result_with_chat_model()

    return result

def get_basic_prompt_example_result(input: str) -> str:
    prompt = BasicPrompt(basic_prompt_example_config, input)
    result = prompt.get_result_with_chat_model()

    return result
    
# Test
response = get_requirement_analysis_result("I want to make a mobile app for reading books. The book reading app allows reading pdf and epub text files downloaded to your phone. At the same time, the app also has the function of interacting with other users such as writing book reviews, reading other people's book reviews, commenting on book reviews, following other users,... The database needs to store data about user information, book information, books that users have read, reviews that users have written, and comments from users. I expect that in the first year there will be about 10,000 users and 1,000 books.")
json_response = OutputParser.json_extract(response)
print(json_response["data_model"]["data_type"])

# print(get_basic_prompt_example_result("MongoDB"))
