import asyncio
from autogen_core.models import UserMessage
from autogen_ext.models.ollama import OllamaChatCompletionClient
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console

# # Assuming your Ollama server is running locally on port 11434.
# model_client = OllamaChatCompletionClient(model="gemma3:1b")

# # Define a simple function tool that the agent can use.
# # For this example, we use a fake weather tool for demonstration purposes.
# async def get_weather(city: str) -> str:
#     """Get the weather for a given city."""
#     return f"The weather in {city} is 73 degrees and Sunny."


# # Define an AssistantAgent with the model, tool, system message, and reflection enabled.
# # The system message instructs the agent via natural language.
# agent = AssistantAgent(
#     name="weather_agent",
#     model_client=model_client,
#     tools=[get_weather],
#     system_message="You are a helpful assistant.",
#     reflect_on_tool_use=True,
#     model_client_stream=True,  # Enable streaming tokens from the model client.
# )


# # Run the agent and stream the messages to the console.
# async def main() -> None:
#     await Console(agent.run_stream(task="What is the weather in New York?"))
#     # Close the connection to the model client.
#     await model_client.close()


# # NOTE: if running this inside a Python script you'll need to use asyncio.run(main()).
# # asyncio.run(main())

async def main() -> None:
    ollama_model_client = OllamaChatCompletionClient(model="gemma3:1b", model_info={
      "vision": False,
      "function_calling": True,
      "json_output": False,
      "family": "unknown"
    })
    
    response = await ollama_model_client.create([UserMessage(content="What is the capital of France?", source="user")])
    print(response)
    await ollama_model_client.close()

if __name__ == "__main__":
    asyncio.run(main())