
import os ,sys 
from utils.model_loader import ModelLoader ,ConfigigLoader
from langgraph.graph import StateGraph ,START ,END ,MessagesState

class GraphBuilder():
    def __init__(self ,model_provider : str = 'groq'):
        self.model_loader = ModelLoader(model_provider=model_provider)
        self.llm = self.model_loader.load_llm()


        self.tools = []
        
    def agent_function(self ,state :MessagesState):
        user_question = self.state['']

    def build_graph(self):
        pass  