import os
from dotenv import load_dotenv

load_dotenv()
DEVELOPMENT_MODE = os.getenv('DEVELOPMENT_MODE', 'DEVELOPER')
if DEVELOPMENT_MODE == 'DEVELOPER':
    from .development import *
