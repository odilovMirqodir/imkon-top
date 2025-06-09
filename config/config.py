from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
ALLOWED_ADMIN_ID = os.getenv("ALLOWED_ADMIN_ID")