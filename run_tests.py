# -*- coding: utf-8 -*-
"""
@Time ： 2026/2/5 13:48
@Auth ： 章豹
@File ：run_tests.py
@IDE ：PyCharm
"""
import subprocess
import sys
import os
from libs.run_edit import run_edit


if __name__ == "__main__":
    run_edit("test")

    # 运行 pytest
    result = subprocess.run([
        sys.executable, "-m", "pytest",
        # "--html=reports/report.html",
        # "--self-contained-html",
        "-v"
    ])
    sys.exit(result.returncode)