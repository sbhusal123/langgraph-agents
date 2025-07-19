# Langgraph Complete Course:

## Prequisits:

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
    - StateGraph
    - Runnable
    - Message

## Sample Agents (Reference):

- [Agent 1](./Samples/Agent1%20-%20L1.ipynb)

    Accepts a list of input and returns a sum through a node.



## Some Reference Codes:

**Display graph as PNG**

```python
from IPython.display import Image, display

display(Image(app.get_graph().draw_mermaid_png()))
```
