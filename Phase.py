# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 22:49:18 2024

@author: AKKALAPOTHU VENKATESH

Code : phase

"""

import numpy as np
import math
import matplotlib.pyplot as plt

# Reading the file content
file_name = input("Enter Path of the file:")
with open(file_name, 'r') as file:
    lines = file.readlines()

data = {
    'frequencies': [],
    'ZXXR': [],
    'ZXXI': [],
    'ZXX_VAR': [],
    'ZXYR': [],
    'ZXYI': [],
    'ZXY_VAR': [],
    'ZYXR': [],
    'ZYXI': [],
    'ZYX_VAR':[],
    'ZYYR': [],
    'ZYYI': [],
    'ZYY_VAR':[],
    'TXR':[],
    'TXI':[],
    'TX_VAR':[],
    'TYR':[],
    'TYI':[],
    'TY_VAR':[]
}

section = None
for line in lines:
    line = line.strip()
    if line.startswith('>FREQ'):
        section = 'frequencies'
    elif line.startswith('>ZXXR'):
        section = 'ZXXR'
    elif line.startswith('>ZXXI'):
        section = 'ZXXI'
    elif line.startswith('>ZXX.VAR'):
        section = 'ZXX_VAR'
    elif line.startswith('>ZXYR'):
        section = 'ZXYR'
    elif line.startswith('>ZXYI'):
        section = 'ZXYI'
    elif line.startswith('>ZXY.VAR'):
        section = 'ZXY_VAR'
    elif line.startswith('>ZYXR'):
        section = 'ZYXR'
    elif line.startswith('>ZYXI'):
        section = 'ZYXI'
    elif line.startswith('>ZYX.VAR'):
        section = 'ZYX_VAR'
    elif line.startswith('>ZYYR'):
        section = 'ZYYR'
    elif line.startswith('>ZYYI'):
        section = 'ZYYI'
    elif line.startswith('>ZYY.VAR'):
        section = 'ZYY_VAR'
    elif line.startswith('TXR.EXP'):
        section='TXR'
    elif line.startswith('TXI.EXP'):
        section='TXI'
    elif line.startswith('TXVAR.EXP'):
        section='TX_VAR'
    elif line.startswith('TYR.EXP'):
        section='TYR'
    elif line.startswith('TYI.EXP'):
        section='TYI'
    elif line.startswith('TYVAR.EXP'):
        section='TY_VAR'
    elif line.startswith('>'):
        section = None
    elif section:
        values = [float(val) for val in line.split()]
        data[section].extend(values)

# Convert lists to numpy arrays
frequencies = np.array(data['frequencies'])
timeperiod = np.reciprocal(frequencies)
ZXXR = np.array(data['ZXXR'])
ZXXI = np.array(data['ZXXI'])
ZXX_VAR = np.array(data['ZXX_VAR'])
ZXYR = np.array(data['ZXYR'])
ZXYI = np.array(data['ZXYI'])
ZXY_VAR = np.array(data['ZXY_VAR'])
ZYXR = np.array(data['ZYXR'])
ZYXI = np.array(data['ZYXI'])
ZYX_VAR = np.array(data['ZYX_VAR'])
ZYYR = np.array(data['ZYYR'])
ZYYI = np.array(data['ZYYI'])
ZYY_VAR = np.array(data['ZYY_VAR'])
TXR = np.array(data['TXR'])
TXI = np.array(data['TXI'])
TX_VAR = np.array(data['TX_VAR'])
TYR = np.array(data['TYR'])
TYI = np.array(data['TYI'])
TY_VAR = np.array(data['TY_VAR'])
ZXY = ZXYR + 1j * ZXYI
ZYX = ZYXR + 1j * ZYXI
ZXX = ZXXR + 1j * ZXXI
ZYY = ZYYR + 1j * ZYYI

# calculating phase_xy
phase_xy= list(map(lambda x,y:np.degrees(np.arctan(x/y)), ZXYI,ZXYR ))

# calculating phase_yx
phase_yx= list(map(lambda x,y:np.degrees(np.arctan(x/y)), ZYXI,ZYXR ))


# Plotting of Skin Depth
plt.figure(figsize=(10, 8))
plt.plot(frequencies, phase_xy, marker='o',   linestyle='-', color='b', label='XY')
plt.plot(frequencies, phase_yx, marker='o',   linestyle='-', color='g', label='YX')
plt.xscale('log')  # Set logarithmic scale for x-axis
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase(Degrees)')
plt.title('Frequency vs Phase')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
