# =========================
# INSTALL (run in terminal, NOT in code)
# pip install langchain-nomic langchain_community tiktoken langchainhub chromadb langchain langgraph tavily-python
# =========================

from typing import List, TypedDict
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import GPT4AllEmbeddings
from langchain_community.chat_models import ChatOllama
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain.schema import Document

from langgraph.graph import StateGraph, END
from langchain_community.tools.tavily_search import TavilySearchResults

# =========================
# CONFIG
# =========================
local_llm = "llama3"

llm = ChatOllama(model=local_llm, temperature=0)

# =========================
# INDEX
# =========================
urls = [
    "https://lilianweng.github.io/posts/2023-06-23-agent/",
    "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
    "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
]

docs = [WebBaseLoader(url).load() for url in urls]
docs_list = [item for sublist in docs for item in sublist]

splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=250, chunk_overlap=0
)

doc_splits = splitter.split_documents(docs_list)

vectorstore = Chroma.from_documents(
    documents=doc_splits,
    collection_name="rag-chroma",
    embedding=GPT4AllEmbeddings(),
)

retriever = vectorstore.as_retriever()

# =========================
# RAG CHAIN
# =========================
prompt = PromptTemplate(
    template="""
Use context to answer.

Question: {question}
Context: {context}

Answer concisely:
""",
    input_variables=["question", "context"],
)

rag_chain = prompt | llm | StrOutputParser()

def format_docs(docs):
    return "\n\n".join(d.page_content for d in docs)

# =========================
# SEARCH TOOL
# =========================
web_search_tool = TavilySearchResults(k=3)

# =========================
# STATE
# =========================
class GraphState(TypedDict):
    question: str
    generation: str
    web_search: str
    documents: List[Document]

# =========================
# NODES
# =========================
def retrieve(state):
    question = state["question"]
    docs = retriever.invoke(question)
    return {"documents": docs, "question": question}

def generate(state):
    question = state["question"]
    documents = state["documents"]

    context = format_docs(documents)
    generation = rag_chain.invoke({"question": question, "context": context})

    return {
        "question": question,
        "documents": documents,
        "generation": generation,
    }

def web_search(state):
    question = state["question"]
    docs = state.get("documents", [])

    results = web_search_tool.invoke({"query": question})

    content = "\n".join([d.get("content", "") for d in results])

    docs.append(Document(page_content=content))

    return {"question": question, "documents": docs}

# =========================
# ROUTER (simple version fix)
# =========================
def route_question(state):
    return "vectorstore"

# =========================
# GRAPH
# =========================
workflow = StateGraph(GraphState)

workflow.add_node("retrieve", retrieve)
workflow.add_node("generate", generate)
workflow.add_node("websearch", web_search)

workflow.set_entry_point("retrieve")

workflow.add_edge("retrieve", "generate")
workflow.add_edge("generate", END)

app = workflow.compile()

# =========================
# TEST
# =========================
if __name__ == "__main__":
    inputs = {"question": "What is agent memory?"}

    for output in app.stream(inputs):
        print(output)
