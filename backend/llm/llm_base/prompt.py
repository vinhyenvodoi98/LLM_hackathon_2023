from langchain.prompts import PromptTemplate, FewShotPromptTemplate
from langchain.chains import LLMChain
from llm_base.palm_model import PalmModel

class Prompt:
    prompt: PromptTemplate

    def __init__(self) -> None:
        pass

    def get_result_with_text_model(self) -> str:
        llm = PalmModel.text_model
        chain = LLMChain(llm=llm, prompt=self.prompt)
        response = chain.run({})

        return response
    
    def get_result_with_chat_model(self) -> str:
        llm = PalmModel.chat_model
        chain = LLMChain(llm=llm, prompt=self.prompt)
        response = chain.run({})

        return response
        

class FewShotPrompt(Prompt):

    def __init__(self, config, input: str) -> PromptTemplate:
        example_prompt = PromptTemplate(
            input_variables=config["example_input_variables"],
            template=config["example_template"]
        )

        few_shot_prompt = FewShotPromptTemplate(
            examples=config["examples"], 
            example_prompt=example_prompt, 
            prefix="\n".join([ config["context"], config["prefix"] ]),
            suffix=config["suffix"], 
            input_variables=[ config["actual_input_variable"] ],
        )

        formatted_prompt = few_shot_prompt.format(**{ config["actual_input_variable"]: input })

        self.prompt = PromptTemplate(template=formatted_prompt, input_variables=[])
    
    
class BasicPrompt(Prompt):

    def __init__(self, config, input: str) -> PromptTemplate:
        prompt = PromptTemplate(
            input_variables=[ config["input_variable"] ],
            template=config["template"]
        )

        formatted_prompt = prompt.format(**{ config["input_variable"]: input })

        self.prompt = PromptTemplate(template=formatted_prompt, input_variables=[])
