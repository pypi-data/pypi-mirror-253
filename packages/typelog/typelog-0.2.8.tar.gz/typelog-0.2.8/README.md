# Typelog - Static typed structured logging

## Description

This project araised from the need to log backend applications, aws lambdas and other stuff in modern cloud ecosystem. Logging systems today are able easily parsing JSON format out of the box.
Static typing approach brings here consistent way to define key values to final msg, as well as easier following Domain Driven Design, where logs consistently describe what they log. Static typed logging brings easy refactoring to any present logs.

## Features

- Accepts static typed components as optional params
  - it will not accept `any` options
  - has shortcut WithFields, to make clone of the logger with default logging fields
- Easy to turn on/off parameters by environment variables
  - Ability to define different log levels for different created loggers
- Easier turning complex objects into structured logging
  - accepts maps and structs as its params. It will parse them on their own.
[See folder for up to date examples](./examples)

## Alternative Versions

- [Version in golang](https://github.com/darklab8/go-typelog)

## Python specifics

- In order to function with python extra well, recommendation to turn on
  - [strict mypy](<https://careers.wolt.com/en/blog/tech/professional-grade-mypy-configuration>)
  - or pyright in one of [its mods](<https://github.com/microsoft/pyright/blob/main/docs/configuration.md>)
- [Published at pypi](https://pypi.org/project/typelog/)

## How to use

install with `pip install typelog`

examples/types.py
```py
from dataclasses import dataclass
from typing import NewType

TaskID = NewType("TaskID", int)


@dataclass(frozen=True)
class Task:
    smth: str
    b: int
```

examples/logtypes.py
```py
from typing import Any, Dict

from typelog import LogType

from . import types


def TaskID(value: types.TaskID) -> LogType:
    def wrapper(params: Dict[str, Any]) -> None:
        params["task_id"] = str(value)

    return wrapper


def Task(value: types.Task) -> LogType:
    def wrapper(params: Dict[str, Any]) -> None:
        params.update(value.__dict__)

    return wrapper
```

examples/test_examples.py
```py
import logging
import unittest

import typelog
from typelog import LogConfig, Loggers, get_logger
from typelog.types import LibName, LogLevel, RootLogLevel

from . import logtypes, types

logger = get_logger(__name__)


class TestExamples(unittest.TestCase):
    def setUp(self) -> None:
        Loggers(
            RootLogLevel(logging.DEBUG),
            LogConfig(LibName("examples"), LogLevel(logging.DEBUG)),
            add_time=True,
        ).configure()

    def test_basic(self) -> None:
        logger.warn("Writing something", logtypes.TaskID(types.TaskID(123)))

    def test_another_one(self) -> None:
        task = types.Task(smth="abc", b=4)
        logger.warn("Writing something", logtypes.Task(task))

    def test_with_fields(self) -> None:
        logger2 = logger.with_fields(logtypes.Task(types.Task(smth="aaa", b=1)))
        logger3 = logger.with_fields(
            typelog.String("smth", "asd"), typelog.Int("number", 2)
        )

        logger.info("logger printed")
        logger2.info("logger2 printed")
        logger3.info("logger3 printed")
```
