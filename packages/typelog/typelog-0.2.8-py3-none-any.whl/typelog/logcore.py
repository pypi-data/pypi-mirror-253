import json
import logging
from copy import deepcopy
from typing import Dict, Optional, Tuple

from . import settings
from .types import LogAttrs, LogType

log_levels_str_to_int: Dict[str, int] = {"": logging.WARN}
log_levels_str_to_int.update(logging._nameToLevel)

default_log_level: int = log_levels_str_to_int[settings.log_level]


class StructuredMessage:
    def __init__(
        self,
        message: str,
        *args: LogType,
        turn_json: Optional[bool] = None,
    ) -> None:
        self._message = message
        self._turn_json = turn_json
        self._kwargs: LogAttrs = {}
        for add_option in args:
            add_option(self._kwargs)

    def __str__(self) -> str:
        if settings.log_json or self._turn_json:
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
        self._logger = logging.getLogger(name)
        self._logger.setLevel(default_log_level)
        self._with_fields: Tuple[LogType] = tuple()  # type: ignore[assignment]
        self._turn_json = turn_json

    def debug(self, message: str, *args: LogType) -> None:
        self._logger.debug(
            StructuredMessage(
                message, *(args + self._with_fields), turn_json=self._turn_json
            )
        )

    def info(self, message: str, *args: LogType) -> None:
        self._logger.info(
            StructuredMessage(
                message, *(args + self._with_fields), turn_json=self._turn_json
            )
        )

    def warn(self, message: str, *args: LogType) -> None:
        self._logger.warning(
            StructuredMessage(
                message, *(args + self._with_fields), turn_json=self._turn_json
            )
        )

    def error(self, message: str, *args: LogType) -> None:
        self._logger.error(
            StructuredMessage(
                message, *(args + self._with_fields), turn_json=self._turn_json
            )
        )

    def fatal(self, message: str, *args: LogType) -> None:
        self._logger.fatal(
            StructuredMessage(
                message, *(args + self._with_fields), turn_json=self._turn_json
            )
        )

    def with_fields(self, *args: LogType) -> "Typelog":
        logger = deepcopy(self)
        logger._with_fields = args  # type: ignore[assignment]
        return logger


def get_logger(file: str, turn_json: Optional[bool] = None) -> Typelog:
    return Typelog(file, turn_json)
