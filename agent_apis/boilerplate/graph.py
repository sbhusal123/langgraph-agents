from langchain_ollama import ChatOllama, OllamaEmbeddings

llm_model = 'llama3.1:latest'
embeding_model = 'nomic-embed-text:latest'

llm = ChatOllama(model=llm_model)
embeding_model = OllamaEmbeddings(model=embeding_model)

from typing import TypedDict, List
from langchain_core.messages import BaseMessage

class AgentState(TypedDict):
    messages: List[BaseMessage]
    user_message: str
    response: str



from langgraph.graph import StateGraph, END

graph = StateGraph(AgentState)

def call_llm(state: AgentState) -> AgentState:
    return state

graph.add_node('llm', call_llm)

# passthrough
graph.add_node('should_continue', lambda s: s)

graph.add_edge('llm', 'should_continue')



def should_continue(state: AgentState):
    exit = True
    if exit:
        return 'no'
    else:
        return 'yes'

graph.add_node('check_user_query', lambda s: s)

graph.add_conditional_edges(
    'should_continue',
    should_continue,
    {
        'yes': 'check_user_query',
        'no': END
    }
)

def decide_tool_or_rag(state: AgentState):
    is_rag = True
    is_tool = False

    if is_rag:
        return 'answer_from_document'
    elif is_tool:
        return 'tool_call'
    else:
        return 'general_query'

graph.add_node('tool', lambda s: s)
graph.add_node('rag', lambda s: s)

graph.add_conditional_edges(
    'check_user_query',
    decide_tool_or_rag,
    {
        'answer_from_document': 'rag',
        'tool_call': 'tool',
        'general_query': 'llm'
    }
)

graph.add_edge('tool', 'llm')
graph.add_edge('rag', 'llm')


graph.set_entry_point('llm')


if __name__ == "__main__":
    agent = graph.compile()


    with open('graph.png', 'wb+') as f:
        f.write(agent.get_graph().draw_mermaid_png())
