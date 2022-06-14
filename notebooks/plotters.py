#!/usr/bin/env python3
# -*-coding:utf-8 -*-
'''
@File    :   plotters.py
@Time    :   2022/06/13 18:21:58
@Author  :   Daniel W 
@Version :   1.0
@Contact :   willhelmd@tamu.edu
'''
import os
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


# get basepath
basepath = Path(__file__).parent

def plot_identity(fig, ax, x, y, ls=':', c='k'): 
    def I(x): 
        return x
    p0 = min([min(x), min(y)])
    p1 = max([max(x), max(y)])
    x  = [p0, p1]
    ax.plot(x, I(x), ls=ls, c=c)
    return fig,ax
