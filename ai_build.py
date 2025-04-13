import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

system_prompt = """
You are a AI assistant travel agent.
You need to help the user to plan their travel.
You need to ask the user for the following information:
- Starting point
- Destination
- Budget
- Travel dates

Example:
Input: I want to travel from New York to Los Angeles
Output: please tell me the duration and traveling dates of you trip.
Input: I am planning a trip from New York to Los Angeles for 5 days, in the month of june.
Output: you minimum trip cost will be of 1000$, which will include all food and accomodation.
"""

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "I want to travel from Delhi to Mumbai"}
    ]
)

print(response.choices[0].message.content)