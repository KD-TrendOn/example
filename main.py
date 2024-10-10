from langchain_openai import ChatOpenAI
import os
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import asyncio

llm = ChatOpenAI(temperature=1, model="gpt-4o-mini", openai_api_key=os.getenv("OPENAI_API_KEY"), openai_api_base="https://api.proxyapi.ru/openai/v1")
prompt = ChatPromptTemplate.from_messages([
    ("system", "Answer to user question"),
    ("human", "{question}")
])
chain = prompt | llm | StrOutputParser()

async def main():
    for i in range(200):
        await asyncio.sleep(3)
        result = await chain.ainvoke({"question": "Напиши пример программы на C++"})
        print(result)

if __name__ == "__main__":
    asyncio.run(main())
