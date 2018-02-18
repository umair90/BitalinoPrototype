#!/usr/bin/env python2
# -*- coding: utf-8 -*-


import numpy as np
from scipy import signal

def procACC(newWin,lux_data,send_threshold = 2000):
    smoothacc = signal.savgol_filter(newWin-np.mean(newWin),15,0)
    abs_sum = np.sum(abs(smoothacc))
    print(abs_sum)
    if lux_data < 10:
        shareFlag_change = abs_sum > send_threshold
    return shareFlag_change