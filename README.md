# Langgraph Complete Course:


## 1. Prequisits:

- [Type Annotations](./Pre%20Reqs/1.%20Typing.ipynb)
    - TypedDict
    - Union
    - Optional
    - Annotated
    - Sequence
    - How langgraph uses annotated, sequence and add_message reducer.
        - BaseMessage types
        - Usage with and without reducer

- [Lambda, Maps](./Pre%20Reqs/2.%20Lambda,%20Map.ipynb)

- [Langgraph Elements](./Pre%20Reqs/3.%20Langgraph%20Elements.ipynb)
    - State
    - Node
    - Edges
    - Graph
    - Tool
    - ToolNode
    - [StateGraph](https://langchain-ai.github.io/langgraph/concepts/low_level/#stategraph)
    - Runnable
    - Message

**Below is the curated reference to langchain basic before getting started.**

- [1. Chat And Text Completion Model](https://github.com/sbhusal123/langchain-curated/blob/main/Docs/1.%20Langchain%20Basics/1.%20Chat%20and%20text%20completion%20model.md)
    - ChatOllama
    - OllamaLLM

- [2. Prompt Types](https://github.com/sbhusal123/langchain-curated/blob/main/Docs/1.%20Langchain%20Basics/2.%20Prompts.md)
    - String Prompt Template / PromptTemplate
    - ChatPromptTemplate
    - Usage Example


- [3. LCEL (LangChain Expression Language)](https://github.com/sbhusal123/langchain-curated/blob/main/Docs/1.%20Langchain%20Basics/3.%20LCEL.md)
    - PromptTemplate
    - ChatPromptTemplate

- [4. Structured Output Parsing](https://github.com/sbhusal123/langchain-curated/blob/main/Docs/1.%20Langchain%20Basics/4.%20Output%20Structure%20and%20Parsing.md)
    - Structured Output with PyDantic
    - Sample Output Parsing Example

- [5. Basic Embeding Retrival Chain](https://github.com/sbhusal123/langchain-curated/blob/main/Docs/2.%20Similarity%20Search%20And%20Context/1.%20Basic%20Rag.md)
    - FAISS Example
    - Example Retrival Chain

- [6. Simple RAG - Embeding And Querying From Text File](https://github.com/sbhusal123/langchain-curated/blob/main/Docs/3.%20RAG%20Applications/1.%20Docs%20Embeding.md)
    - `langchain_community.document_loaders`
    - `langchain_text_splitters`

- [7. RAG Chain Covering PromptTemplates](https://github.com/sbhusal123/langchain-curated/blob/main/Docs/3.%20RAG%20Applications/2.%20RAG%20Chain.md)
    - ChatPromptTemplate
    - HumanMessagePromptTemplate
    - SystemMessagePromptTemplate

- [8. Agent With History and Docs QNA Chain](https://github.com/sbhusal123/langchain-curated/blob/main/Docs/3.%20RAG%20Applications/3.%20Agent%20With%20History%20an%20Docs%20QNA%20Chain.md)

- [9. Dealing With Multiple RAG Source And Retrivers](https://github.com/sbhusal123/langchain-curated/blob/main/Docs/5.%20Multiple%20Source%20Retriver/1.%20Multiple%20Retrivers.md)

    > Use Case: we have multiple source text document containing a info about a service, product. Here, we deal with multiple retrivers with other components reused.

    - Structured Output -> Used as a Flag for Retriver
    - Two retrivers -> Used based on Structured Flag

- [10. Dealing With Multiple Source](https://github.com/sbhusal123/langchain-curated/blob/main/Docs/5.%20Multiple%20Source%20Retriver/2.%20Multiple%20Data%20Source.md)
    > Very similar to RAG 9.
    - Query analyzer to figure out retriver.
    - Custom Chain to execute a RAG chain.
    - [WIP...]()


## 2. Graph Based Architecture Intro (Reference):

Sample agents build with different flow. [Langgraph StateGrapg Docs...](https://langchain-ai.github.io/langgraph/concepts/low_level/#stategraph)

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

- [Agent 6](./Samples/Agent%206%20-%20Parallel%20Execution.ipynb) Parallel execution nodes and merge.

## 3. Sample Agents With Tools And LLM: (AI Agents)

This section consists of sample agents built with ollama local models.

- [AI Agent 1](./MiniAgents/AI%20Agent%201%20-%20Chatbot.ipynb)
Simple Integration of stategraph with LLM. Simple ChatBot Without Memory

- [AI Agent 2](./MiniAgents/AI%20Agent%202%20-%20Converstational%20Chatbot.ipynb)
Converstational chatbot with memory.

- [AI Agent 3](./MiniAgents/AI%20Agent%203%20-%20React%20Agent.ipynb)
React Agent with toolcall.

- [AI Agent 4](./MiniAgents/AI%20Agent%204%20-%20Email%20Drafter.ipynb)
Email drafter helper.

- [AI Agent 5](./MiniAgents/AI%20Agent%205%20-%20RAG%20Agent.ipynb) RAG based agent, question answering from pdf document.

## 4. Hows and Concepts:

- [How Toolcalling Works](./Concepts/How%20Toolcall%20Works.ipynb)


## 5. Insights And Architecture:

- [Agenic Workflow](./Architecture,%20Insights/Agentic%20Workflow.ipynb)

## 6. Some Reference Codes:

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

**Pretty Print Dictionary:**
```python
from pprint import pprint

pprint(result)
```
