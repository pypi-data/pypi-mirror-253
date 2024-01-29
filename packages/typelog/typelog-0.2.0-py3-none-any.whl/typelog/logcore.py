import json
import logging
from copy import deepcopy
from typing import Dict, Optional, Tuple

from . import settings
from .types import LogAttrs, LogType

log_levels_str_to_int: Dict[str, int] = {"": logging.WARN}
log_levels_str_to_int.update(logging._nameToLevel)

default_log_level = log_levels_str_to_int[settings.LOG_LEVEL]


class StructuredMessage:
    def __init__(
        self,
        message: str,
        turn_json: Optional[bool],
        *args: LogType,
    ) -> None:
        self._message = message
        self._turn_json = turn_json
        self._kwargs: LogAttrs = LogAttrs({})
        for add_option in args:
            add_option(self._kwargs)

    def __str__(self) -> str:
        if settings.LOG_JSON or self._turn_json:
            return json.dumps(self.to_dict())

        if len(self._kwargs.keys()) == 0:
            return self._message

        return "%s >>> %s" % (
            self._message,
            " ".join([f"{key}={value}" for key, value in self._kwargs.items()]),
        )

    def to_dict(self) -> Dict:
        return {"message": self._message, **self._kwargs}


sm = StructuredMessage


class Typelog:
    def __init__(self, name: str, turn_json: Optional[bool]):
        """
        pass __file__ into file
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(default_log_level)
        self._with_fields: Tuple[LogType] = tuple()  # type: ignore[assignment]
        self._turn_json = turn_json

    def debug(self, message: str, *args: LogType) -> None:
        self.logger.debug(
            StructuredMessage(message, self._turn_json, *(args + self._with_fields))
        )

    def info(self, message: str, *args: LogType) -> None:
        self.logger.info(
            StructuredMessage(message, self._turn_json, *(args + self._with_fields))
        )

    def warn(self, message: str, *args: LogType) -> None:
        self.logger.warning(
            StructuredMessage(message, self._turn_json, *(args + self._with_fields))
        )

    def error(self, message: str, *args: LogType) -> None:
        self.logger.error(
            StructuredMessage(message, self._turn_json, *(args + self._with_fields))
        )

    def fatal(self, message: str, *args: LogType) -> None:
        self.logger.fatal(
            StructuredMessage(message, self._turn_json, *(args + self._with_fields))
        )

    def with_fields(self, *args: LogType) -> "Typelog":
        logger = deepcopy(self)
        logger._with_fields = args  # type: ignore[assignment]
        return logger


def get_logger(file: str, turn_json: Optional[bool] = None) -> Typelog:
    return Typelog(file, turn_json)
