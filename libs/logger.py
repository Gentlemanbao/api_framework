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
from functools import wraps


class LoggerConfig:
    """日志配置管理器"""

    _initialized = False

    @classmethod
    def setup_logger(cls):
        """初始化日志配置"""
        if cls._initialized:
            return logger

        # 移除默认处理器
        logger.remove()

        # 控制台输出配置（保持原有格式）
        logger.add(
            sys.stdout,
            level="INFO",
            format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
        )

        # 文件输出配置（保持原有配置）
        logger.add(
            LOG_DIR / "api_auto_{time:YYYY-MM-DD}.log",
            rotation="1 day",
            retention="7 days",
            level="DEBUG",
            encoding="utf-8"
        )

        cls._initialized = True
        return logger

    @classmethod
    def get_logger(cls):
        """获取已配置的logger实例"""
        if not cls._initialized:
            cls.setup_logger()
        return logger

# 确保模块导入时自动初始化
logger = LoggerConfig.setup_logger()
