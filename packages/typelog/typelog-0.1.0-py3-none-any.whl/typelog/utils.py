import json
import logging
import os
from dataclasses import dataclass, field
from typing import Dict, List, NewType

from . import settings

LibName = NewType("LibName", str)
LogLevel = NewType("LogLevel", int)

is_configured: bool = False


@dataclass
class Loggers:
    root_log_level: int
    log_levels: Dict[LibName, LogLevel] = field(default_factory=dict)
    turn_json: bool = False

    add_thread: bool = os.environ.get("TYPELOG_ADD_THREAD") == "true"
    add_process: bool = os.environ.get("TYPELOG_ADD_PROCESS") == "true"
    add_level: bool = os.environ.get("TYPELOG_ADD_LEVEL") == "true"
    add_filepath: bool = os.environ.get("TYPELOG_ADD_FILEPATH") == "true"
    add_time: bool = os.environ.get("TYPELOG_ADD_TIME") == "true"

    @property
    def _is_turn_json(self) -> bool:
        return settings.LOG_JSON or self.turn_json

    @property
    def _format_json(self) -> str:
        message_format = "%(message)s"
        format = {"content": "TARGET_REPLACE"}
        if self.add_process:
            format["process"] = "%(process)d"
        if self.add_thread:
            format["thread"] = "%(thread)d"
        if self.add_time:
            format["time"] = "%(asctime)s"
        if self.add_filepath:
            format["filepath"] = "%(name)s"
        if self.add_level:
            format["level"] = "%(levelname)s"

        return json.dumps(format).replace('"TARGET_REPLACE"', message_format)

    @property
    def _format_text(self) -> str:
        formats: List[str] = []
        if self.add_process:
            formats.append("%(process)d")
        if self.add_thread:
            formats.append("%(thread)d")
        if self.add_time:
            formats.append("%(asctime)s")
        if self.add_filepath:
            formats.append("%(name)s")
        if self.add_level:
            formats.append("%(levelname)s")

        formats.append(" %(message)s")
        return ":".join(formats)

    def configure(self) -> None:
        """
        * third party libs are noisy and having bad default log levels
        * for better logging purposes we should disable all other loggining to Warning level
        * and turn on our app logging Debug level.
        * it helps to be better aware about warnings and critical errors across libraries
        * And at the same having very comfortable development environment which
            makes very easy to investigate throughly our app debugging log records
            and to fix from third party libs warnings only
        """
        print("Configured debugging logging")

        global is_configured

        if is_configured:
            return

        for lib_name, log_level in self.log_levels.items():
            loggers = [
                logging.getLogger(name)
                for name in logging.root.manager.loggerDict
                if name.startswith(lib_name)
            ]
            for logger in loggers:
                logger.setLevel(log_level)

        root_logger = logging.getLogger("")
        root_logger.setLevel(self.root_log_level)
        ch = logging.StreamHandler()
        ch.setLevel(self.root_log_level)
        if self._is_turn_json:
            formatter = logging.Formatter(self._format_json)
        else:
            formatter = logging.Formatter(self._format_text)
        ch.setFormatter(formatter)
        root_logger.addHandler(ch)

        is_configured = True
