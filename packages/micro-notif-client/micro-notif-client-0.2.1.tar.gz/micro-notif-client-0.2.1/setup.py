import sys
from setuptools import setup

if sys.version_info < (3, 9):
    print("micro-notif-client requires Python 3.9 or higher")
    sys.exit(1)

setup()
