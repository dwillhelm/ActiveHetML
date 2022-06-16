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

def fs(x=6.4, y=4.8): 
    return np.array([x,y])

def plot_identity(fig, ax, x, y, ls=':', c='k'): 
    def I(x): 
        return x
    p0 = min([min(x), min(y)])
    p1 = max([max(x), max(y)])
    x  = [p0, p1]
    ax.plot(x, I(x), ls=ls, c=c)
    return fig,ax

def myax(ax, xlabel, ylabel): 
    ax.grid(True, alpha=0.2)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)


def plot_parity(fig, ax, y_pred, pool, color): 
    y_true = y[y.index.isin(y_pred.index)]

    ax.scatter(y_true, y_pred,ec='k',alpha=0.3,c=color)
    plot_identity(fig, ax, y_true, y_pred)
    ax.set_ybound(y.min()-1, y.max()+0.5)
    ax.set_xbound(y.min()-1, y.max()+0.5)
    ax.grid(True,alpha=0.1)
    ax.set_xlabel('True')
    ax.set_ylabel('Predicted')   
