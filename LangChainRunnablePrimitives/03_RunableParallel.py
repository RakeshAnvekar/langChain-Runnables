#                 ┌─────────────┐
#                 │   Input     │
#                 │  Topic: AI  │
#                 └──────┬──────┘
#                        │
#                 RunnableParallel
#                        │
#         ┌──────────────┴──────────────┐
#         │                             │
# ┌───────────────┐               ┌───────────────┐
# │     LLM 1     │               │     LLM 2     │
# │ Generate      │               │ Generate      │
# │ AI Tweet      │               │ LinkedIn Post │
# └───────────────┘               └───────────────┘

#    Output 1                          Output 2
#  (Tweet)                       (LinkedIn Post)
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence,RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
prompt_tweet=PromptTemplate(
    template="Write a short and catchy tweet about {topic} in less than 280 characters.",
    input_variables=["topic"]
)
prompt_linkedin=PromptTemplate(
    template="Write a LinkedIn post about {topic} in less than 280 characters.",
    input_variables=["topic"]
)
model = ChatOpenAI()
parser = StrOutputParser()

chain_tweet = RunnableSequence(prompt_tweet, model, parser)
chain_linkedin = RunnableSequence(prompt_linkedin, model, parser)

parallel_chain = RunnableParallel(
    {
        "tweet": chain_tweet,
        "linkedin_post": chain_linkedin
    }
)

print(parallel_chain.invoke({"topic": "AI"}))