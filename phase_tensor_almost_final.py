# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 07:49:02 2024

@author: AKKALAPOTHU VENKATESH

Code : 
"""



import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches

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


# phase tensor
dot_x= list(map(lambda a,b,c,d:(a*d-b*c), ZXXR,ZXYR,ZYXR,ZYYR))
inverse_x= np.reciprocal(dot_x)
pi_xx = list(map(lambda v,x,y,z,w:v*(x*y-z*w),  inverse_x,ZYYR,ZXXI,ZXYR,ZYXI ))
pi_xy = list(map(lambda v,x,y,z,w:v*(x*y-z*w),  inverse_x,ZYYR,ZXYI,ZXYR,ZYYI ))
pi_yx = list(map(lambda v,x,y,z,w:v*(x*y-z*w),  inverse_x,ZXXR,ZYXI,ZYXR,ZXXI ))
pi_yy = list(map(lambda v,x,y,z,w:v*(x*y-z*w),  inverse_x,ZXXR,ZYYI,ZYXR,ZXYI ))





# feom caldiver paper

# phase 

# trace of phase
trace_phase = list(map(lambda x,y:x+y, pi_xx,pi_yy))


# skew of phase
skew = list(map(lambda x,y:x+y, pi_xy,pi_yx))


# determinent
det_phase = list(map(lambda a,b,c,d:(a*b-c*d), pi_xx,pi_yy,pi_xy,pi_yx))


# phase -1

phase_1 = list(map(lambda x:x/2, trace_phase))

# phase-2
phase_2 = list(map(lambda x:math.sqrt(x), det_phase))

# phase-3
phase_3 = list(map(lambda x:x/2, skew ))


# phase - minimum
phase_min = list(map(lambda x,y,z:(math.sqrt((x**2)+(z**2)))-(math.sqrt((x**2)+(z**2)-(y**2))), phase_1,phase_2,phase_3))


# phase_maximum
phase_max = list(map(lambda x,y,z:(math.sqrt((x**2)+(z**2)))+(math.sqrt((x**2)+(z**2)-(y**2))), phase_1,phase_2,phase_3))



# skew angle
skew_angle_radians= list(map(lambda x,y,z,w,:math.atan((y-z)/(x+w))/2,   pi_xx,pi_xy,pi_yx,pi_yy))
skew_angle_Degrees=list(map(lambda x:(x*180/math.pi), skew_angle_radians))


# strike Angle
strike_angle_radians= list(map(lambda x,y,z,w,:math.atan((y+z)/(x-w))/2,   pi_xx,pi_xy,pi_yx,pi_yy))
strike_angle_Degrees=list(map(lambda x:(x*180/math.pi), strike_angle_radians))


# substracting phase maximum and minimum
phase_max_min = list(map(lambda x,y:x-y, phase_max,phase_min))


# 



# Create a figure and an axes
fig, ax = plt.subplots()

# Define ellipse parameters
center = (0.5, 0.5)
width = 0.1
height = 0.05
angle =  strike_angle_Degrees # Rotation angle in degrees

# Create an ellipse patch
ellipse = patches.Ellipse(center, width, height, angle=angle, edgecolor='black', facecolor='red')

# Add the ellipse to the plot
ax.add_patch(ellipse)

# Set limits and aspect ratio
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')

# Show the plot
plt.show()
