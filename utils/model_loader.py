import os ,sys 
from pydantic import BaseModel ,Field
from typing import Literal ,Annotated ,Optional  ,Any
from utils.config_loader import load_config
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq


class ConfigLoader:
    def __init__(self):
        print('Loading config')
        self.config = load_config()
        print('config loaded successfully')


    def __getitem__(self, key):
        return self.config[key] 


class ModelLoader(BaseModel):
    model_provider : Literal['openai' ,'groq'] = 'groq' 
    config : Optional[ConfigLoader] = Field(default=None , exclude=True)

    def model_post_init(self, __context: Any):
        if self.config is None:         
            self.config = ConfigLoader()   


    def load_llm(self):
        """Load and return LLM model"""
        print('LLM is loading')
        print(f'LLM provider is {self.model_provider}')


        if self.model_provider == 'openai':
            openai_api_key = os.getenv('OPENAI_API_KEY')
            model_name = self.config["llm"]['openai']['model_name']
            llm = ChatOpenAI(model=model_name ,api_key=openai_api_key)


        elif self.model_provider == 'groq':
            grok_api_key = os.getenv('GROK_API_KEY')
            model_name = self.config["llm"]['openai']['model_name']
            llm = ChatGroq(model=model_name ,api_key=grok_api_key)

        print('LLM Loaded')

        return llm

