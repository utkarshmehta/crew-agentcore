#!/usr/bin/env python
import sys
import warnings
import os
from datetime import datetime
from vacation_planner.crew import VacationPlanner

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    topic = 'Chandigarh'
    
    inputs = {
        'topic': topic,
        'current_year': str(datetime.now().year)
    }
    
    # INDESTRUCTIBLE CACHE: Force the tool to know the topic even if the agent is lazy
    os.makedirs("knowledge", exist_ok=True)
    with open("knowledge/current_topic.txt", "w", encoding="utf-8") as f:
        f.write(topic)
    
    try:
        VacationPlanner().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        VacationPlanner().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        VacationPlanner().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    try:
        VacationPlanner().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
