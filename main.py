
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
import logging
from google.genai import types
import asyncio
import config 
from agents import agent



logger = logging.getLogger(__name__)

APP_NAME = "StoryGenerationApp"
USER_ID = "user_123"
SESSION_ID = "session_abc"


# --- Setup Runner and Session ---
async def setup_session_and_runner():
    session_service = InMemorySessionService()
    session = await session_service.create_session(app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID)
    logger.info(f"Initial session state: {session.state}")
    runner = Runner(
        agent=agent.root_agent, # Pass the custom orchestrator agent
        app_name=APP_NAME,
        session_service=session_service
    )
    return session_service, runner

# --- Function to Interact with the Agent ---
async def call_agent_async(user_input_topic: str):
    """
    Sends a new topic to the agent (overwriting the initial one if needed)
    and runs the workflow.
    """

    session_service, runner = await setup_session_and_runner()

    current_session = session_service.sessions[APP_NAME][USER_ID][SESSION_ID]
    current_session.state["topic"] = user_input_topic
    logger.info(f"Updated session state topic to: {user_input_topic}")

    content = types.Content(role='user', parts=[types.Part(text=f"Generate a story about the preset topic.")])
    events = runner.run_async(user_id=USER_ID, session_id=SESSION_ID, new_message=content)

    final_response = "No final response captured."
    async for event in events:
        if event.is_final_response() and event.content and event.content.parts:
            print(f"Final response from [{event.author}]: {event.content.parts[0].text}")
            final_response = event.content.parts[0].text
        else:
            print(f"Received event of type [{event.type}] from [{event.author}] with content: {event.content}")   

    print("\n--- Agent Interaction Result ---")
    print("Agent Final Response: ", final_response)

    final_session = await session_service.get_session(app_name=APP_NAME, 
                                                user_id=USER_ID, 
                                                session_id=SESSION_ID)
    print("Final Session State:")
    import json
    print(json.dumps(final_session.state, indent=2))
    print("-------------------------------\n")

# --- Run the Agent ---

if __name__ == "__main__":
    try:
        asyncio.run(call_agent_async("a lonely robot finding a friend in a junkyard"))
    except Exception as e:
        print(f"An error occurred: {e}")
