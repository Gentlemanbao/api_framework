# -*- coding: utf-8 -*-
"""
@Time ： 2026/2/5 13:49
@Auth ： 章豹
@File ：logger.py
@IDE ：PyCharm
"""
from loguru import logger
from config.settings import LOG_DIR
import sys

logger.remove()

logger.add(
    sys.stdout,
    level="INFO",
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
)

logger.add(
    LOG_DIR / "api_auto_{time:YYYY-MM-DD}.log",
    rotation="1 day",
    retention="7 days",
    level="DEBUG",
    encoding="utf-8"
)