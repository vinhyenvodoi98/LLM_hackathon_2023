from langchain.prompts import PromptTemplate, FewShotPromptTemplate
from langchain.chains import LLMChain
import json

from llm.llm_base.palm_model import build_text_model, build_chat_model


class Prompt:

    prompt: PromptTemplate

    def __init__(self) -> None:
        pass

    def get_result_with_text_model(self, temperature: float = 0.5) -> str:
        llm = build_text_model(temperature)
        chain = LLMChain(llm=llm, prompt=self.prompt)
        response = chain.run({})

        return response
    
    def get_result_with_chat_model(self, temperature: float = 0.2) -> str:
        llm = build_chat_model(temperature)
        chain = LLMChain(llm=llm, prompt=self.prompt)
        response = chain.run({})

        return response
        

class FewShotPrompt(Prompt):

    def __init__(self, config, input: str) -> PromptTemplate:
        parsed_config = self.__parse_config(config)

        example_prompt = PromptTemplate(
            input_variables=parsed_config["example_input_variables"],
            template=parsed_config["example_template"]
        )

        few_shot_prompt = FewShotPromptTemplate(
            examples=parsed_config["examples"], 
            example_prompt=example_prompt, 
            prefix="\n".join([ parsed_config["context"], parsed_config["prefix"] ]),
            suffix=parsed_config["suffix"], 
            input_variables=[ parsed_config["actual_input_variable"] ],
        )

        formatted_prompt = few_shot_prompt.format(**{ parsed_config["actual_input_variable"]: input })

        self.prompt = PromptTemplate(template=formatted_prompt, input_variables=[])

    def __parse_config(self, config):
        config["context"] = config["context"].replace("{", "$").replace("}", "&")
        config["examples"] = [ 
            {
                "requirement": example["requirement"],
                "analysis_result": json.dumps(example["analysis_result"]).replace("{", "$").replace("}", "&")
            }
            
            for example in config["examples"] 
        ]

        return config    
    
class SelectingFewShotPrompt(Prompt):

    def __init__(self, config, input: str) -> PromptTemplate:
        parsed_config = self.__parse_config(config)

        example_prompt = PromptTemplate(
            input_variables=parsed_config["example_input_variables"],
            template=parsed_config["example_template"]
        )

        few_shot_prompt = FewShotPromptTemplate(
            examples=parsed_config["examples"], 
            example_prompt=example_prompt, 
            prefix="\n".join([ parsed_config["context"], parsed_config["prefix"] ]),
            suffix=parsed_config["suffix"], 
            input_variables=[ parsed_config["actual_input_variable"] ],
        )

        formatted_prompt = few_shot_prompt.format(**{ parsed_config["actual_input_variable"]: input.replace("{", "$").replace("}", "&").replace("\n", "") })

        self.prompt = PromptTemplate(template=formatted_prompt, input_variables=[])

    def __parse_config(self, config):
        config["examples"] = [ 
            {
                "requirement": example["requirement"].replace("{", "$").replace("}", "&").replace("\n", ""),
                "analysis_result": example["analysis_result"].replace("{", "$").replace("}", "&").replace("\n", "")
            }
            
            for example in config["examples"] 
        ]

        return config   
    
class BasicPrompt(Prompt):

    def __init__(self, config, input: str) -> PromptTemplate:
        prompt = PromptTemplate(
            input_variables=[ config["input_variable"] ],
            template=config["template"]
        )

        formatted_prompt = prompt.format(**{ config["input_variable"]: input })

        self.prompt = PromptTemplate(template=formatted_prompt, input_variables=[])
