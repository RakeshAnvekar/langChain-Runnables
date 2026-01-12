# use case: think we  got email  fro user,
# based on the email content ,if it is a query email we need to send it to support team,
# if it is a feedback email we need to send it to feedback team,   etc

#example: we will take the topic from user , we ask llm to generate the report based on the topic,
#if the generated report length is more than 500 words we will summarize the report using  llm call.
#else less the 500 words we will directly send the report to user.

#             ┌─────────────┐
#             │ User Input  │
#             │   Topic     │
#             └──────┬──────┘
#                    │
#             ┌─────────────┐
#             │   LLM 1     │
#             │ Generate    │
#             │ Report      │
#             └──────┬──────┘
#                    │
#         ┌────────────────────┐
#         │ Length Check Logic │
#         │ (Word Count > 500?)│
#         └──────┬─────────────┘
#                │
#       ┌────────┴─────────┐
#       │                  │
#    YES (>500)          NO (≤500)
#       │                  │
# ┌─────────────┐     ┌─────────────┐
# │   LLM 2     │     │ Direct       │
# │ Summarize   │     │ Output       │
# │ Report      │     │ to User      │
# └──────┬──────┘     └─────────────┘
#        │
# ┌─────────────┐
# │ Final       │
# │ Output      │
# └─────────────┘

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence,RunnableLambda,RunnableBranch,RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

promot1=PromptTemplate(
    template="Write a detailed report about {topic}.",
    input_variables=["topic"]
)

promot2=PromptTemplate(
    template="Summarize the following report in less than 300 words: {report}",
    input_variables=["report"]
)

model = ChatOpenAI()
parser = StrOutputParser()



report_Genaration_Chain = RunnableSequence(
    promot1,
    model,
    parser
)

branch_Chain=RunnableBranch(
    (lambda x: len(x.split()) > 500 ,RunnableSequence(promot2, model, parser)),  # Condition to check if word count > 500
    RunnablePassthrough()  # If not, pass the report directly
)

final_Chain=RunnableSequence(
    report_Genaration_Chain,branch_Chain)

print(final_Chain.invoke({"topic": "Artificial Intelligence"}))