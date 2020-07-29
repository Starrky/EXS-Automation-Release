"""Keys and translations changed Prod/ Staging """
# !/usr/bin/python3.7.2
# coding=utf-8
import os
import sys
import time
from urllib.parse import urljoin
import pandas as pd
import psutil
from playsound import playsound
import platform


# Grab text from launcher
currentdir = os.getcwd()
data = pd.read_excel(f"{currentdir}/List.xlsx")

Keys = data["key"].tolist()
Domains = data["Domain"].tolist()
Old_pl = data["old pl"].tolist()
Old_en = data["old en"].tolist()
New_pl = data["new pl"].tolist()
New_en = data["new en"].tolist()
