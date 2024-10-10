from langchain_openai import ChatOpenAI
import os
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import ChatPromptTemplate
import time
llm = ChatOpenAI(temperature=1, model="gpt-4o-mini", openai_api_key=os.getenv("OPENAI_API_KEY"), openai_api_base="https://api.proxyapi.ru/openai/v1")
prompt = ChatPromptTemplate.from_messages([
    ("system", "Answer to user question"),
    ("human", "{question}")
])
chain = prompt | llm | StrOutputParser()
for i in range(200):
    time.sleep(3)
    print(chain.ainvoke({"question":"Напиши пример программы на C++"}))