from loguru import logger
import os
from app.constants import LOG_DIR

os.makedirs(LOG_DIR, exist_ok=True)

logger.add(
    os.path.join(LOG_DIR, 'captcha_solver_{time}.txt'),
    rotation='1 MB',
    retention='7 days',
    compression='zip',
)


__all__ = ['logger']
