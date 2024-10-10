from langchain_openai import ChatOpenAI
import os
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import asyncio
import logging
from logging.handlers import RotatingFileHandler
import os
import time
import httpx
async_client = httpx.AsyncClient(proxies={'http://':os.getenv("PROXY_LINK_WEB")})
def setup_logger(name):
    log_dir = 'logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logger = logging.getLogger(name)
    logger.setLevel(logging.NOTSET)

    # Создаем обработчик для записи логов в файл
    file_handler = RotatingFileHandler(
        os.path.join(log_dir, f'{name}.log'),
        maxBytes=10*1024*1024,  # 10MB
        backupCount=5
    )
    file_handler.setLevel(logging.NOTSET)

    # Создаем обработчик для вывода логов в консоль
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.NOTSET)

    # Создаем форматтер
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Добавляем обработчики к логгеру
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

logger = setup_logger(__name__)

llm = ChatOpenAI(temperature=1, model="gpt-4o-mini", openai_api_key=os.getenv("OPENAI_API_KEY"), openai_api_base=os.getenv("BASE_PROVIDER"), http_async_client=async_client)
prompt = ChatPromptTemplate.from_messages([
    ("system", "Answer to user question"),
    ("human", "{question}")
])
chain = prompt | llm | StrOutputParser()

async def main():
    for i in range(200):
        await asyncio.sleep(3)
        print(i)
        result = await chain.ainvoke({"question": "Напиши пример программы на C++"})
        print(result)
        print(i)

if __name__ == "__main__":
    asyncio.run(main())
