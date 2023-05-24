import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.agents import load_tools
from langchain.agents import initialize_agent

# temperature - randomness in the output
llm = OpenAI(temperature=0.9)
tools = load_tools(["serpapi", "llm-math"], llm=llm)

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

def basic_agent():
    agent = initialize_agent(tools, llm, "zero-shot-react-description", verbose=True)
    agent.run("Who won the ipl match played on may24 2023")



basic_query()
basic_prompt()
basic_agent()
