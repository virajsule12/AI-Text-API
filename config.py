import os
from dotenv import load_dotenv
import pathlib

dotenv_path = pathlib.Path(__file__).parent / ".env"
load_dotenv(dotenv_path=dotenv_path)  # Reads .env file

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
