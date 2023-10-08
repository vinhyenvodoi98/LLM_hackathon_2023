import os
from dotenv import load_dotenv
from langchain.llms import GooglePalm
from config.palm_model_config import * 

load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

class PalmModel:
    text_model = GooglePalm(
                model=text_model["model_name"],
                temperature=text_model["parameters"]["temperature"],
                max_output_tokens=text_model["parameters"]["max_output_tokens"],
                top_k=text_model["parameters"]["top_k"],
                top_p=text_model["parameters"]["top_p"],
                google_api_key=GOOGLE_API_KEY
            )
    
    chat_model = GooglePalm(
                model=chat_model["model_name"],
                temperature=chat_model["parameters"]["temperature"],
                max_output_tokens=chat_model["parameters"]["max_output_tokens"],
                top_k=chat_model["parameters"]["top_k"],
                top_p=chat_model["parameters"]["top_p"],
                google_api_key=GOOGLE_API_KEY
            )
    
    embedding_model = GooglePalm(
            model=embedding_model["model_name"],
            temperature=embedding_model["parameters"]["temperature"],
            max_output_tokens=embedding_model["parameters"]["max_output_tokens"],
            top_k=embedding_model["parameters"]["top_k"],
            top_p=embedding_model["parameters"]["top_p"],
            google_api_key=GOOGLE_API_KEY
        )


        