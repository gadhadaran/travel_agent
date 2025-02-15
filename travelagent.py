!pip install langchain-community google-generativeai langchain-google-genai serpapi python-dotenv

import os
from langchain.tools import Tool
from langchain_google_genai import GoogleGenerativeAI
from langchain.agents import initialize_agent, AgentType
from langchain.utilities import SerpAPIWrapper
from dotenv import load_dotenv


GOOGLE_API_KEY="your_google_api_key"
SERPAPI_KEY="your_serpapi_key"

!export GOOGLE_API_KEY="your_google_api_key"
%env GOOGLE_API_KEY="your_google_api_key"

import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Manually set API key if missing
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    os.environ["GOOGLE_API_KEY"] = "your_google_api_key"

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Verify if the key is loaded
if not os.getenv("GOOGLE_API_KEY"):
    raise ValueError("❌ GOOGLE_API_KEY is still missing! Set it manually.")

import os
print(os.getenv("GOOGLE_API_KEY"))


!export SERPAPI_KEY="your_serpapi_key"
!set SERPAPI_KEY="your_serpapi_key"
%env SERPAPI_KEY="your_serpapi_key"

import os
print(os.getenv("SERPAPI_KEY"))  # Should print your actual key

from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables

SERPAPI_KEY = os.getenv("SERPAPI_KEY")
if not SERPAPI_KEY:
    raise ValueError("Missing SERPAPI_KEY. Set it in your .env file or environment variables.")


# Initialize SerpAPI wrapper
def search_flights(destination, date):
    search = SerpAPIWrapper(serpapi_api_key=SERPAPI_KEY)
    return search.run(f"flights to {destination} on {date}")

def search_hotels(destination, checkin_date, checkout_date):
    search = SerpAPIWrapper(serpapi_api_key=SERPAPI_KEY)
    return search.run(f"hotels in {destination} from {checkin_date} to {checkout_date}")

def get_itinerary(destination, days):
    search = SerpAPIWrapper(serpapi_api_key=SERPAPI_KEY)
    return search.run(f"best itinerary for {days} days in {destination}")

def track_expenses(expenses):
    total = sum(expenses)
    return f"Total expenses so far: ${total}"


# Define tools
flight_tool = Tool(
    name="Flight Search",
    func=search_flights,
    description="Finds flight details for a given destination and date."
)

hotel_tool = Tool(
    name="Hotel Search",
    func=search_hotels,
    description="Finds hotels based on location and check-in/out dates."
)

itinerary_tool = Tool(
    name="Itinerary Planner",
    func=get_itinerary,
    description="Generates a detailed itinerary for a given destination."
)

expense_tool = Tool(
    name="Expense Tracker",
    func=track_expenses,
    description="Tracks travel expenses."
)


# Initialize Google Gemini AI
import google.generativeai as genai
genai.configure(api_key="your_google_api_key")  # Replace with your actual API key
llm = GoogleGenerativeAI(model="gemini-pro")

# Initialize agent
tools = [flight_tool, hotel_tool, itinerary_tool, expense_tool]

agent_executor = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)


# Test the agent
trip_destination = "Paris"
trip_days = 5
trip_date = "2025-06-10"
checkin_date = "2025-06-10"
checkout_date = "2025-06-15"
expenses = [500, 200, 150]



print("\n--- Flight Details ---\n", agent_executor.invoke({
    "input": "Find flights",
    "destination": trip_destination,
    "date": trip_date
}))

print("\n--- Hotel Details ---\n", agent_executor.invoke({
    "input": "Find hotels",
    "destination": trip_destination,
    "checkin_date": checkin_date,
    "checkout_date": checkout_date
}))

print("\n--- Itinerary ---\n", agent_executor.invoke({
    "input": "Generate itinerary",
    "destination": trip_destination,
    "days": trip_days
}))

print("\n--- Expense Tracking ---\n", agent_executor.invoke({
    "input": "Calculate expenses",
    "expenses": expenses
}))
