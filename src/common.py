# src/common.py

import sys
import os
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import plotly.express as px
from pathlib import Path

def check_env():
    print("Python:", sys.version)
    print("Pandas:", pd.__version__)
