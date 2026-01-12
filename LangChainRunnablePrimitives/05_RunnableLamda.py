# use case: think you have the customer review in data base, you want to sed the reviews to llm model to get the sentiment analysis of each review and finally you want to get the overall sentiment of all reviews.
# but the review in db have some special characters and html tags, so you want to clean the reviews first before sending to llm model. or emoji's are there in the reviews, so you want to remove the emojis first.
# we can create the function to clean the reviews and then use that function in the runnable sequence before sending to llm model.


        # ┌──────────────────┐
        # │   Reviews DB     │
        # │ (Raw Reviews)    │
        # └────────┬─────────┘
        #          │
        # ┌──────────────────┐
        # │ Clean Reviews     │
        # │ (Custom Function) │
        # │ - Remove HTML     │
        # │ - Remove Emojis   │
        # │ - Normalize text  │
        # └────────┬─────────┘
        #          │
        # ┌──────────────────┐
        # │   LLM Model       │
        # │ Sentiment per     │
        # │ Review            │
        # └────────┬─────────┘
        #          │
        # ┌──────────────────┐
        # │ Aggregate Results │
        # │ Overall Sentiment │
        # └──────────────────┘

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence,RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
def clean_review(input: dict) -> dict:
    import re

    review = input["review"]

    # Remove HTML tags
    review = re.sub(r'<.*?>', '', review)

    # Remove Emojis
    review = review.encode('ascii', 'ignore').decode('ascii')

    # Normalize whitespace
    review = ' '.join(review.split())

    return {"review": review}

prompt=PromptTemplate(
    template="Analyze the sentiment of the following review and respond with Positive, Negative, or Neutral:\n\n{review}",
    input_variables=["review"])

model = ChatOpenAI()
parser = StrOutputParser()

runable_review_cleaner = RunnableLambda(clean_review)
chain = RunnableSequence(
    runable_review_cleaner,
    prompt,
    model,
    parser
)

print(chain.invoke({"review": "<p>I love this product! 😊 It's fantastic.</p>"}))

