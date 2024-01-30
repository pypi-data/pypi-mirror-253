import json
import logging
from typing import List

from . import settings, types


class LogConfig:
    def __init__(
        self,
        lib_name: types.LibName,
        log_level: types.LogLevel,
    ):
        self.lib_name = lib_name
        self.log_level: types.LogLevel = log_level


class Loggers:
    def __init__(
        self,
        root_log_level: types.RootLogLevel,
        *log_configs: LogConfig,
        turn_json: bool = settings.log_json,
        add_thread: bool = settings.add_thread,
        add_process: bool = settings.add_thread,
        add_level: bool = settings.add_thread,
        add_filepath: bool = settings.add_thread,
        add_time: bool = settings.add_thread,
    ):
        self.root_log_level = root_log_level
        self.log_configs = log_configs
        self.turn_json = turn_json
        self.add_thread = add_thread
        self.add_process = add_process
        self.add_level = add_level
        self.add_filepath = add_filepath
        self.add_time = add_time

    @property
    def _is_turn_json(self) -> bool:
        return settings.log_json or bool(self.turn_json)

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

        for log_config in self.log_configs:
            loggers = [
                logging.getLogger(name)
                for name in logging.root.manager.loggerDict
                if name.startswith(log_config.lib_name)
            ]
            for logger in loggers:
                logger.setLevel(log_config.log_level)

        root_logger = logging.getLogger("")
        while root_logger.hasHandlers():
            root_logger.removeHandler(root_logger.handlers[0])

        root_logger.setLevel(self.root_log_level)
        ch = logging.StreamHandler()
        ch.setLevel(self.root_log_level)
        if self._is_turn_json:
            formatter = logging.Formatter(self._format_json)
        else:
            formatter = logging.Formatter(self._format_text)
        ch.setFormatter(formatter)
        root_logger.addHandler(ch)
