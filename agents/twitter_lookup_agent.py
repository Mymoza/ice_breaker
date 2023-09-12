from langchain import PromptTemplate
from langchain.chat_models import AzureChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType
from tools.tools import get_profile_url

def lookup(name: str) -> str:
    print('name is : ', name)
    llm = AzureChatOpenAI(temperature=0, model_name="gpt-35-turbo", deployment_name="gpt-35-turbo")
    template = """given the full name of {name_of_person} I want you to get me a link to their Twitter username.
                In your final answer only the person's username"""

    tools_for_agent = [Tool(name="Crawl Google for Twitter profile page",
                            func=get_profile_url,
                            description="useful for when you need to get a Twitter page url")]

    agent = initialize_agent(tools=tools_for_agent, llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

    prompt_template = PromptTemplate(template=template, input_variables=["name_of_person"])

    twitter_username = agent.run(prompt_template.format_prompt(name_of_person=name))
    return twitter_username