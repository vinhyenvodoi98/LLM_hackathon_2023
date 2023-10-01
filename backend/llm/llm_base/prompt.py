from langchain.prompts import PromptTemplate, FewShotPromptTemplate
from .config.prompt_config import *

class Prompt:
    
    @staticmethod
    def get_requirement_analysis_prompt(requirement: str) -> PromptTemplate:
        example_prompt = PromptTemplate(
            input_variables=["requirement", "analysis_result"], 
            template=requirement_analysis_prompt_config["template"]
        )

        few_shot_prompt = FewShotPromptTemplate(
            examples=requirement_analysis_prompt_config["examples"], 
            example_prompt=example_prompt, 
            prefix=requirement_analysis_prompt_config["prefix"],
            suffix=requirement_analysis_prompt_config["suffix"], 
            input_variables=["requirement"],
        )

        formatted_prompt = few_shot_prompt.format(requirement=requirement)

        return PromptTemplate(template=formatted_prompt, input_variables=[])

