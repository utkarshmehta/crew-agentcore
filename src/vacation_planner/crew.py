import os
os.environ['SERPER_API_KEY'] = "98cc0e456c75e481f9e8ffd6120adb1d456a5a1b"

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from crewai.tools import tool
from typing import Any, Optional
from crewai import LLM

# Initialize the underlying Serper tool
serper_tool = SerperDevTool()

@tool("internet_search")
def internet_search(search_query: Optional[str] = None) -> str:
    """Search the internet for up-to-date information about travel destinations. 
    Pass a specific search query string.
    """
    query = search_query
    
    # INDESTRUCTIBLE SELF-HEALING LOGIC:
    # If the agent is lazy/Bedrock fails to pass the string, we grab the topic from the cache
    if not query or query == "{}" or not isinstance(query, str):
        try:
            with open("knowledge/current_topic.txt", "r", encoding="utf-8") as f:
                topic = f.read().strip()
            query = f"15 unique and interesting facts about {topic}"
            print(f"DEBUG: Agent provided no query. Self-healing search for: {query}")
        except:
            query = "top things to do in the destination"

    print(f"DEBUG: Serper API call triggered for: {query}")
    try:
        return str(serper_tool._run(search_query=query))
    except Exception as e:
        return f"Search result: {str(e)}"

llm = LLM(model="bedrock/us.amazon.nova-pro-v1:0")

@CrewBase
class VacationPlanner():
    """VacationPlanner crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def vacation_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['vacation_researcher'],
            verbose=True,
            tools=[internet_search],
            llm=llm,
            max_iter=3 # Efficiency cap
        )

    @agent
    def itinerary_planner(self) -> Agent:
        return Agent(
            config=self.agents_config['itinerary_planner'],
            verbose=True,
            llm=llm
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'],
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
