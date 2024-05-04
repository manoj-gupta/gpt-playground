from fastapi import FastAPI
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langserve import add_routes
import uvicorn

# model
llm = Ollama(model="llama2")

# prompt
template = PromptTemplate.from_template("Tell me a joke about {topic}.")

# output parser
output_parser = StrOutputParser()

# chain
chain = template | llm | output_parser

# app server
app = FastAPI(title="LangChain", version="1.0", description="The first server")
add_routes(app, chain, path="/chain")


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=9001)
