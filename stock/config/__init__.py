import os
import logging
from dotenv import load_dotenv
from stock.config.key_vault import KeyvaultCache
from .config import Config

logger = logging.getLogger(__name__)

if ( os.getenv('PROFILE') == None ):
    logger.info("Loading environment variables from .env file")
    load_dotenv(".env")

g_config = Config()
keyvault_cache = KeyvaultCache(g_config)