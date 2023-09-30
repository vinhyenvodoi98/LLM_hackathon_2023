import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import GooglePalm
from langchain.llms.loading import load_llm



load_dotenv()

ACTIVELOOP_TOKEN = os.getenv('ACTIVELOOP_TOKEN')
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# llm = GooglePalm(model="models/text-bison-001", temperature="0", google_api_key=GOOGLE_API_KEY)
llm = load_llm("./llm_setup_data/llm.json")
template = """
As a certified public accountant, I need you to explain the definition of a term and give me examples of when this term is used.
What does the term {term} mean?
"""
prompt = PromptTemplate(
    input_variables=["term"],
    template=template,
)

# Input data for the prompt
input_data = {"term": "liquidity"}

# Create LLMChain
chain = LLMChain(llm=llm, prompt=prompt)

# Run the LLMChain to get the AI-generated song title
response = chain.run(input_data)

print("Term:", response)
