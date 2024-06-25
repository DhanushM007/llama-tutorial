from dotenv import load_dotenv
from langchain_cohere import ChatCohere
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
load_dotenv()
chat =ChatCohere(model='command',cohere_api_key=os.getenv("COHERE_API_KEY"))
msg="List the some movies of telugu"
prompt=ChatPromptTemplate.from_template(msg)
chain=prompt|chat|StrOutputParser()
response=chain.invoke({})
print(response)