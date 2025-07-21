# Langgraph Complete Course:

## 1. Prequisits:

- [Type Annotations](./Pre%20Reqs/1.%20Type%20Annotations.ipynb)
    - TypedDict
    - Union
    - Optional

- [Lambda, Maps](./Pre%20Reqs/2.%20Lambda,%20Map.ipynb)

- [Lamggraph Elements](./Pre%20Reqs/3.%20Langgraph%20Elements.ipynb)
    - State
    - Node
    - Edges
    - Graph
    - Tool
    - ToolNode
    - [StateGraph](https://langchain-ai.github.io/langgraph/concepts/low_level/#stategraph)
    - Runnable
    - Message

## 2. Sample Agents (Reference):

Sample agents build with different flow. [Langchain Docs...](https://langchain-ai.github.io/langgraph/concepts/low_level/#stategraph)

- [Agent 1](./Samples/Agent%201%20-%20L1.ipynb) 
Accepts a list of input and returns a sum through a node.

- [Agent 2](./Samples/Agent%202%20-%20Sequential%20Flow.ipynb)
Agent with sequential flow.

- [Agent 3](./Samples/Agent%203%20-%20Conditional%20graph.ipynb)
Agent with conditional edges.

- [Agent 4](./Samples/Agent%204%20-%20Merge%20Flow.ipynb)
Agent with multiple conditional edges and merge flow.

- [Agent 5](./Samples/Agent%205%20-%20Looping.ipynb)
Agent with loopings nodes.

## 3. Sample Agents With Tools And LLM:

This section consists of sample agents built with ollama local models.

- [AI Agent 1](./MiniAgents/AI%20Agent%201%20-%20Chatbot.ipynb)
Simple Integration of stategraph with LLM. Simple ChatBot Without Memory

- [AI Agent 2](./MiniAgents/AI%20Agent%202%20-%20Converstational%20Chatbot.ipynb)
Converstational chatbot with memory.

- [AI Agent 3](./MiniAgents/AI%20Agent%203%20-%20React%20Agent.ipynb)
React Agent with toolcall.

## 4. Hows and Concepts:

- [How Toolcalling Works](./Concepts/How%20Toolcall%20Works.ipynb)

## 5. Some Reference Codes:

**Display graph as PNG**

```python
from IPython.display import Image, display

display(Image(app.get_graph().draw_mermaid_png()))
```

```python
from IPython.display import display, Markdown

mermaid_code = agent.get_graph().draw_mermaid()
display(Markdown(f"```mermaid\n{mermaid_code}\n```"))

```
