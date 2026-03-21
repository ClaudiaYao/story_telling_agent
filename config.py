import os, sys
from dotenv import load_dotenv
from pathlib import Path 

BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.append(str(BASE_DIR))

# Load environment variables from .env file
load_dotenv()

GENIMI_MODEL = "gemini-2.5-flash-lite"

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(BASE_DIR / "my-project-admin.json")
