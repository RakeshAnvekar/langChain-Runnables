import random

##-------------- Simple dummy LLM component
class DummyLLM:
    def __init__(self):
        print("DummyLLM initialized")

    def predict(self, prompt: str):
        response_list = [
            "Delhi is the capital of India.",
            "The capital of India is Delhi."
        ]
        return {"response": random.choice(response_list)}


##---------------------- Simple Prompt component
class DummyPrompt:
    def __init__(self, template, input_variables):
        print("DummyPrompt initialized")
        self.template = template
        self.input_variables = input_variables

    def format(self, input_dict):
        return self.template.format(**input_dict)


##---------------------- Chain (without Runnables)
class DummyChain:
    def __init__(self, llm, prompt):
        print("DummyChain initialized")
        self.llm = llm
        self.prompt = prompt

    def run(self, input_dict):
        formatted_prompt = self.prompt.format(input_dict)
        llm_response = self.llm.predict(formatted_prompt)
        return llm_response["response"]


# Usage
prompt = DummyPrompt(
    template="What is the capital of {country}?",
    input_variables=["country"]
)

llm = DummyLLM()
chain = DummyChain(llm=llm, prompt=prompt)

output = chain.run({"country": "India"})
print(output)

## this chain class is not flexible , we canot make call two times with different inputs, it means this is not flexible like runnables
#with this approch we cant create  all kind of workflows.
# because  we can communicate with DummyLLM with predict method only. and DummyPrompt with format method only.
#We need to standardize the interface to make it more flexible and reusable.
#we can make use of abstract base classes or interfaces to define standard methods for LLMs, Prompts, and Chains.
