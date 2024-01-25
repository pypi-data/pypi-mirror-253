# Copyright (C) 2023-2024 Indoc Systems
#
# Contact Indoc Systems for any questions regarding the use of this source code.

import datetime as dt
import json
import logging
import logging.config
from typing import Union


class JsonFormatter(logging.Formatter):
    """Convert LogRecord to json string."""

    def format(self, record: logging.LogRecord) -> str:
        asctime = dt.datetime.fromtimestamp(record.created, tz=dt.timezone.utc).isoformat()
        level = record.levelname
        logger = record.name
        message = record.getMessage()
        exc_info = None
        if record.exc_info:
            exc_info = self.formatException(record.exc_info)

        return json.dumps(
            {
                'asctime': asctime,
                'level': level,
                'logger': logger,
                'message': message,
                'exc_info': exc_info,
            }
        )


def configure_logging(level: int, formatter: str = 'json', namespaces: Union[list[str], None] = None) -> None:
    """Configure python logging system using a config dictionary."""

    formatters = {
        'default': {
            'format': '%(asctime)s\t%(levelname)s\t[%(name)s]\t%(message)s',
        },
        'json': {
            '()': JsonFormatter,
        },
    }
    if formatter not in formatters:
        formatter = next(iter(formatters))

    if namespaces is None:
        namespaces = ['pilot', 'asyncio', 'uvicorn']

    config = {
        'handlers': ['stdout'],
        'level': level,
    }
    loggers = dict.fromkeys(namespaces, config)

    logging_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': formatters,
        'handlers': {
            'stdout': {
                'formatter': formatter,
                'class': 'logging.StreamHandler',
                'stream': 'ext://sys.stdout',
            },
        },
        'loggers': loggers,
    }

    logging.config.dictConfig(logging_config)
