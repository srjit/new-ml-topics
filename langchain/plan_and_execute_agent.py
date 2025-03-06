import os

from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

from langchain_experimental.plan_and_execute import PlanAndExecute, load_agent_executor, load_chat_planner
from langchain import SerpAPIWrapper, LLMMathChain, WikipediaAPIWrapper
from langchain_core.tools import Tool

# Initialize LLM and Math Chain
llm = OpenAI(temperature=0)
llm_math_chain = LLMMathChain.from_llm(llm=llm, verbose=True)

# Initialize the tools
search = SerpAPIWrapper()
wikipedia = WikipediaAPIWrapper()

tools = [
    Tool(
        name="search",
        func=search.run,
        description="Useful when you need to answer questions on current events"
    ),
    Tool(
        name="Wikipedia",
        func=wikipedia.run,
        description="Useful when you need to answer questions on facts and statistics"
    ),
    Tool(
        name="Calculator",
        func=llm_math_chain.run,
        description="Useful when you need to answer math questions"
    )
]

# Define the prompt
prompt = """
    Where is the next summer olympics going to be hosted? What is the population of that country? What is the population of that country raised to the 0.3 power?
"""

prompt2 = "Who is the founder of SpaceX and what is the square root of the birth year of his first wife?"

# Initialize the model, planner, and executor
model = ChatOpenAI(temperature=0)
planner = load_chat_planner(model)
executor = load_agent_executor(model, tools, verbose=True)

# Set up the agent
agent = PlanAndExecute(planner=planner, executor=executor)

# Run the agent with the prompt
agent.run(prompt2)
