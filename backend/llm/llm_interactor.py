from langchain.chains import LLMChain
from llm_base.palm_model import PalmModel
from llm_base.prompt import Prompt

def get_requirement_analysis_result(requirement: str) -> str:
    llm = PalmModel.text_model
    prompt = Prompt.get_requirement_analysis_prompt(requirement)

    chain = LLMChain(llm=llm, prompt=prompt)
    response = chain.run({})

    print(response)
    
# Test
# print(get_requirement_analysis_result("I want to make a mobile app for reading books. The book reading app allows reading pdf and epub text files downloaded to your phone. At the same time, the app also has the function of interacting with other users such as writing book reviews, reading other people's book reviews, commenting on book reviews, following other users,... The database needs to store data about user information, book information, books that users have read, reviews that users have written, and comments from users. I expect that in the first year there will be about 10,000 users and 1,000 books."))

