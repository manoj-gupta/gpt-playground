# https://python.langchain.com/docs/get_started/introduction

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOpenAI()

# print(llm.invoke("how can langsmith help with testing?"))

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are world class technical documentation writer."),
    ("user", "{input}")
])

# chain = prompt | llm
# chain.invoke({"input": "how can langsmith help with testing?"})

output_parser = StrOutputParser()

chain = prompt | llm | output_parser
print(chain.invoke({"input": "how can langsmith help with testing?"}))
