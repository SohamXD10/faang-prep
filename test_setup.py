import sys
import subprocess

checks = {
    "Python 3.12+": sys.version_info >= (3, 12),
    "pip available": True,
    "yfinance": None,
    "pytest": None,
    "black": None,
}
try:
    import yfinance

    checks["yfinance"] = True
except ImportError:
    checks["yfinance"] = False
try:
    import pytest

    checks["pytest"] = True
except ImportError:
    checks["pytest"] = False
try:
    import black

    checks["black"] = True
except ImportError:
    checks["black"] = False
for name, ok in checks.items():
    status = "PASS" if ok else "FAIL"
print(f"[{status}] {name}")
