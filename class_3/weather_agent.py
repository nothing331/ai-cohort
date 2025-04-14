from dotenv import load_dotenv
import os
import json
from openai import OpenAI

load_dotenv()

client = OpenAI()

def get_weather(city):
    return "31 degree celsius"

system_prompt = """
You are an helpful AI agent who is specialized in resolving the user's queries.
you work on start, plan, action, observe mode.
For the given user query, and available tools and based on the tool selection you perform an action to create a plan.
Wait for the observation and based on the observation from the tool call and resolve the user query.

Rules:
1. You have to give the output in the form of a json object.
2. Always perform one step at a time and wait for the next input.
3. carefully analuse the user query.

Output JSON format:
{
    "step": "string",
    "content": "string",
    "function": "The name of the function if the step is action",
    "input": "The input parameter required for the function if the step is action"
}

Example:
User Query : What's the weather in Tokyo?
Output: {"step": "plan", "content": "User is interesed in weather data of Tokyo"}
Output: {"step": "plan", "content": "From the avaliable tools I should call get_weather"}
Output: {"step": "action", "function": "get_weather", "input": "Tokyo"}
Output: {"step": "Output", "content": "The weather in Tokyo is sunny with a temperature of 25 degrees Celsius"}
"""

messages = [
    {"role": "system", "content": system_prompt}
]

query = input("> ")
messages.append({"role": "user", "content": query})

while True:
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        response_format={"type": "json_object"}
    )

    parsed_response = json.loads(response.choices[0].message.content)
    messages.append({"role": "assistant", "content": response.choices[0].message.content})

    if parsed_response["step"] == "action":
        # Execute the function if it's an action step
        if parsed_response["function"] == "get_weather":
            weather_result = get_weather(parsed_response["input"])
            messages.append({"role": "user", "content": f"The weather result is: {weather_result}"})
            continue

    if parsed_response["step"] == "Output":
        print(f"AI: {parsed_response['content']}")
        break

    print(f"AI: {parsed_response['content']}")
    query = input("> ")
    messages.append({"role": "user", "content": query})
