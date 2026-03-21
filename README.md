How to use this repo
Refer to the Medium article for the whole working process: https://medium.com/@claudia.yao2012/how-to-build-a-custom-agent-using-vertex-ai-and-google-adk-ea15e9443f09

1. Set project root folder as current working folder.
2. Create .venv by running: python -m venv .venv
3. Copy .env file and service account key .json file to the root folder (important).
4. Run the command: .venv/Scripts/activate.ps1 (on mac, run: source .venv/bin/activate)
5. Run the command: pip install -r requirements.txt
6. Run the command: python main.py
the agent will run and result displays in terminal window.

7. (optional) after step 5, run the command: adk web.
Input your prompt, and the agent will run in the Google ADK Web UI.
