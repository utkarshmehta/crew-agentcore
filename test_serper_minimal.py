import os
os.environ['SERPER_API_KEY'] = '98cc0e456c75e481f9e8ffd6120adb1d456a5a1b'
from crewai_tools import SerperDevTool
tool = SerperDevTool()
try:
    print("Attempting search...")
    result = tool._run(search_query="interesting facts about London")
    print("SUCCESS")
    print(str(result)[:200])
except Exception as e:
    print(f"FAILURE: {str(e)}")
