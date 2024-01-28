import os
from datetime import timedelta
from loguru import logger
from core.settings.base import *

LOG_FILES_PATH = os.getenv('LOG_FILES_PATH', f'{BASE_DIR}/logs/project')
logger.add(f'{LOG_FILES_PATH}/info.log', level='INFO', rotation='00:00', compression='zip')
