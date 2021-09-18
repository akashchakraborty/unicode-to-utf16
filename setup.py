import os
import sys
import time
import pyperclip as cp
from distutils.core import setup # Need this to handle modules
import py2exe 

setup(console=['UnicodeUTF.py']) # Calls setup function to indicate that we're dealing with a single console application