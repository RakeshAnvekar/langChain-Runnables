# consider an exaample, user pass the tjoke ttopic to llm, llm will  retuen the explation of the joke. but we cant see the actual joke when we run the 
#sequential runnable chain. because the output of first llm is directly passed to the second prompt.
#To see the intermediate outputs, we can use Passthrough runnable to capture and display the intermediate results.


#             ┌─────────────┐
#             │ User Input  │
#             │ Joke Topic  │
#             └──────┬──────┘
#                    │
#             ┌─────────────┐
#             │   LLM 1     │
#             │ Generate    │
#             │ Joke        │
#             └──────┬──────┘
#                    │
#          RunnablePassthrough
#            (Capture Joke)
#                    │
#         ┌──────────┴──────────┐
#         │                     │
#    Joke Output           ┌─────────────┐
#  (Visible to user)       │   LLM 2     │
#                          │ Explain     │
#                          │ the Joke    │
#                          └──────┬──────┘
#                                 │
#                          Explanation Output

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough
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

passthrough = RunnablePassthrough()

joke_Generator_Chain = RunnableSequence(prompt1, model, parser)

parallelChain=RunnableParallel({

    'joke':RunnablePassthrough(),
    'explanation':RunnableSequence(prompt2, model, parser)
})

finalChain=RunnableSequence(joke_Generator_Chain, parallelChain)

print(finalChain.invoke({"topic": "dogs"}))