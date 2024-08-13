from tavily import TavilyClient, MissingAPIKeyError, InvalidAPIKeyError, UsageLimitExceededError
import os
from dotenv import load_dotenv

load_dotenv()

TAVILY_API_KEY = os.getenv('TAVILY_API_KEY')

# Step 1. Instantiating your TavilyClient

try:
    tavily_client = TavilyClient(api_key=TAVILY_API_KEY)
except MissingAPIKeyError:
    print("API key is missing. Please provide a valid API key.")

# Step 2. Executing a search query
try:
    response = tavily_client.search(
        "How to forecast potential fishing zones?",
        max_results=70,
        topic="general",
        include_domains=["https://link.springer.com"]
    )
except InvalidAPIKeyError:
    print("Invalid API key provided. Please check your API key.")
except UsageLimitExceededError:
    print("Usage limit exceeded. Please check your plan's usage limits or consider upgrading.")


# Step 3. That's it! You've done a Tavily Search!
print(response)