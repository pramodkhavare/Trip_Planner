
import os ,sys 
from utils.model_loader import ModelLoader ,ConfigigLoader
from langgraph.graph import StateGraph ,START ,END ,MessagesState
from langgraph.prebuilt import ToolNode ,tools_condition

from prompt_library.prompt import SYSTEM_PROMPT


class GraphBuilder():
    def __init__(self ,model_provider : str = 'groq'):
        self.model_loader = ModelLoader(model_provider=model_provider)
        self.llm = self.model_loader.load_llm()

        self.tools = []


        self.llm_with_tools = self.llm.bind_tools(tools=self.tools)

        self.graph = None 

        self.system_prompt = SYSTEM_PROMPT

        
    def agent_function(self ,state :MessagesState):
        user_question = self.state['messages']
        input_question = self.system_prompt + user_question
        responce = self.llm_with_tools.invoke(input_question)

        return {'messages' : [responce]}

    
    def build_graph(self):
        graph_builder = StateGraph(state_schema=MessagesState) 

        graph_builder.add_node('agent_function' ,self.agent_function)
        graph_builder.add_node('tools' ,ToolNode(tools=self.tools))


        graph_builder.add_edge(START ,'agent_function')
        graph_builder.add_conditional_edges('agent_function' ,tools_condition)
        graph_builder.add_edge('tools' ,'agent_function')
        graph_builder.add_edge('agent_function' ,END)

        self.graph = graph_builder.compile()

        return self.graph

    def __call__(self, *args, **kwds):
        return self.build_graph() 