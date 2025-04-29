from langchain_openai import ChatOpenAI
from langgraph.graph import START, END, StateGraph
from typing import TypedDict

## Original implementation
# rowwise_graph.py
async def complaints_log(state):
   llm = ChatOpenAI()
   await llm.ainvoke("Hey")

async def complaints_log1(state):
   llm = ChatOpenAI()
   await llm.ainvoke("Hey")

async def complaints_log2(state):
   llm = ChatOpenAI()
   await llm.ainvoke("Hey")

async def complaints_log3(state):
   llm = ChatOpenAI()
   await llm.ainvoke("Hey")

class State1(TypedDict):
   data: dict


graph1 = StateGraph(State1)
graph1.add_node(complaints_log)
graph1.add_node(complaints_log1)
graph1.add_node(complaints_log2)
graph1.add_node(complaints_log3)
graph1.add_edge(START, "complaints_log")
graph1.add_edge(START, "complaints_log1")
graph1.add_edge(START, "complaints_log2")
graph1.add_edge(START, "complaints_log3")
graph1 = graph1.compile()


async def process_rows(state):
    rows = [{"data": r} for r in state['rows']]
    await graph1.abatch(rows, config={"max_concurrency": 30})

class State2(TypedDict):
   rows: list


graph2 = StateGraph(State2)
graph2.add_node(process_rows)
graph2.add_edge(START, "process_rows")
graph2.add_edge("process_rows", END)
agent = graph2.compile()
