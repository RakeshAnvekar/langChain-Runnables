from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()


prompt1=PromptTemplate(
    template="Write a joke about {topic}?",
    input_variables=["topic"]
)
prompt2=PromptTemplate(
    template="explain me the following joke {joke} in a simple way",
    input_variables=["joke"]
)

model = ChatOpenAI()

parser = StrOutputParser()


chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

print(chain.invoke({"topic": "dogs"}))