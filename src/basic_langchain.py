import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

# temperature - randomness in the output
llm = OpenAI(temperature=0.9)

# basic query example
def basic_query():
    # query
    query_text = "what is the temperature in bangalore like"
    print(llm(query_text))


def basic_prompt():
    prompt = PromptTemplate(
        input_variables=['city'],
        template="what is the weather like in {city}")

    print(llm(prompt.format(city="bangalore")))


basic_query()
basic_prompt()
