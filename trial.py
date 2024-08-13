from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

TAVILY_API_KEY = os.getenv('TAVILY_API_KEY')

# Step 1. Instantiating your TavilyClient
tavily_client = TavilyClient(api_key=TAVILY_API_KEY)

# Step 2. Executing a simple search query
response = tavily_client.search(
  "How to forecast potential fishing zones?",
  max_results=50,
  topic="general",
  include_domains=["https://link.springer.com"]
)

# Step 3. That's it! You've done a Tavily Search!
print(response)