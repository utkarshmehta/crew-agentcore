import os
import time
from datetime import datetime
from vacation_planner.crew import VacationPlanner

def run_test(city):
    print(f"\n" + "="*20 + f" TESTING CITY: {city} " + "="*20)
    inputs = {
        'topic': city,
        'current_year': str(datetime.now().year)
    }
    
    # We delete old report to ensure fresh generation
    if os.path.exists("report.md"):
        os.remove("report.md")
        
    try:
        VacationPlanner().crew().kickoff(inputs=inputs)
        
        # Verification
        if os.path.exists("report.md"):
            with open("report.md", "r", encoding="utf-8") as f:
                content = f.read()
                if city.lower() in content.lower():
                    print(f"✅ SUCCESS: Generated report contains {city}")
                else:
                    print(f"❌ FAILURE: Report for {city} does not mention the city name!")
        else:
            print(f"❌ FAILURE: report.md was not generated for {city}")
            
    except Exception as e:
        print(f"❌ ERROR during {city} run: {e}")

if __name__ == "__main__":
    cities = ["Tokyo", "London", "New York"]
    for city in cities:
        run_test(city)
        print("Waiting 5 seconds between runs...")
        time.sleep(5)
    
    print("\n" + "="*50)
    print("THOROUGH TESTING COMPLETE")
    print("="*50)
