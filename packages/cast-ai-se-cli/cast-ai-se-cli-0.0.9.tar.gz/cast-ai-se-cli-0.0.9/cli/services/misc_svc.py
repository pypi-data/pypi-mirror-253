import os
import platform
import sys

from docopt import ParsedOptions

from cli.constants import LOG_DIR, LOG_FILE
from cli.models.config import ConfigObject
import logging


def init(parsed_options: ParsedOptions) -> ConfigObject:
    cfg = ConfigObject(parsed_options)

    log_level = logging.DEBUG if cfg.app_inputs["debug"] else logging.WARNING
    os.makedirs(LOG_DIR, exist_ok=True)
    logging.basicConfig(filename=os.path.join(LOG_DIR, LOG_FILE),
                        format='%(asctime)s - %(levelname)s:%(name)s - %(message)s',
                        level=log_level)

    logger = logging.getLogger(__name__)

    logger.info(f"{'=' * 200}")
    logger.info(f"Starting executing SE CLI Command Sequencer with the following inputs: {sys.argv[1:]}")
    logger.debug(f"{get_system_info()}")
    return cfg


def get_system_info():
    return {'OS': platform.system(), 'OS Version': platform.version(), 'Machine': platform.machine()}
