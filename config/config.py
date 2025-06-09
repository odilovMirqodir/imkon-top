from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")
IMKON_TOP_DATABASE = os.getenv("IMKON_TOP_DATABASE")
IMKON_TOP_CHECK = os.getenv("IMKON_TOP_CHECK")
ALLOWED_ADMIN_ID = os.getenv("ALLOWED_ADMIN_ID")