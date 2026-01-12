import random
from abc import ABC, abstractmethod


#common interface

class Runnable(ABC):
    @abstractmethod
    def invoke(self, input_data):
        pass


##-------------- Simple dummy LLM component
class DummyLLM(Runnable): 
    def __init__(self):
        print("DummyLLM initialized")

    def invoke(self, prompt: str):
        response_list = [
            "Delhi is the capital of India.",
            "The capital of India is Delhi."
        ]
        return {"response": random.choice(response_list)}
    
    
## we will not remove predict method to maintain the existing functionality for other clients, we just give warning that its going to be deprecated,please use invoke method.
    def predict(self, prompt: str):
        response_list = [
            "Delhi is the capital of India.",
            "The capital of India is Delhi."
        ]
        return {"response": random.choice(response_list)}


##---------------------- Simple Prompt component
class DummyPrompt(Runnable):
    def __init__(self, template, input_variables):
        print("DummyPrompt initialized")
        self.template = template
        self.input_variables = input_variables


    def invoke(self, input_dict):
        return self.template.format(**input_dict)
    
## we will not format predict method to maintain the existing functionality for other clients, we just give warning that its going to be deprecated ,please use invoke method.

    def format(self, input_dict):
        return self.template.format(**input_dict)
    
##---------------------- Chain (with Runnables)
class DummyRunnableConnector(Runnable):
    def __init__(self, runnable_list: Runnable): #[prompt, llm ]
        print("DummyChain initialized")
        self.runnable_list = runnable_list

    def invoke(self, input_dict): 
        for runnable in self.runnable_list:
            input_dict = runnable.invoke(input_dict)
        return input_dict["response"]
    
    #----------------------  string outputr parser

class StringOutputParser(Runnable):
        def __init__(self):
            print("StringOutputParser initialized")

        def invoke(self, input_str):
            return input_str
    # Usage
prompt = DummyPrompt(
        template="What is the capital of {country}?",
        input_variables=["country"]
    )
llm = DummyLLM()

parser= StringOutputParser()

chain = DummyRunnableConnector(runnable_list=[prompt, llm, parser])
chain_output = chain.invoke({"country": "India"})
print(chain_output)

# we can create any kind of chain now with different runnables and different workflows



