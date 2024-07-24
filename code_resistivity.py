# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 10:34:17 2024

@author: python_revision


a= "hello"
b= "happy"
c= a+b
print(c)

a= "hello"
print(a*5)
a='''string
hello every 
one 
wellcome'''
print(a)
a= ["hello",1,2.6]
b= [1,2.6,"venkat"]
print(a+b)
print(a*2)
a=[1,2,3]
b=[5,6,7]
c= zip(a,b)
print(list(c))
a= [2.345,1.367,2.987]
b= [4.67,2.356,9.571]
print(zip(a,b))

a=(1,2,3)
b=[5,6,7]
d=[]
for x,y in zip(a,b):
    c=x*y
    d.append(c)
    print(d)

for i in a:
    b=i*2
    d.append(b)
print(d)
a={1:"venkat",
   2:"bujjodu",
   3:"amma"} 
print(a[3])
set2 = {'James', 3,'Python'}
print(set2)

a= 1
b= 4
c=a+b
print(f"1st value {a} and 2nd value together {b} is {c}")

l1=[1,2,3,4,5,6]
l2=[10,20,30,40,50]
venky= list(map(lambda x,y:x**y, l1,l2))
print(venky)
d=[]
for x,y in zip(l1,l2):
    z= x*y
    d.append(z)
print(d)

l1=[1,2,3,4,5,6]
l2=[10,20,30,40,50]
def venkat(l1,l2):
    d=[]
    for x,y in zip(l1,l2):
        z= x*y
        d.append(z)
    return d    
venkatesh= venkat(l1,l2)
print(venkatesh)

l1=[1,2,3,4,5,6]
l2=[10,20,30,40,50]
class heaven:
    def venk(self,l1,l2):
        venky= list(map(lambda x,y:x*y, l1,l2))
        return venky
venkatesh1=heaven()
v1=venkatesh1.venk(l1,l2)
print(v1)

       


def venkat(l1,l2,):
    for x,y in zip(l1,l2):
        z=x*y
        return l4.append(z)

print(venkat)
   
"""
'''
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

# Calculate |ZXY| and apparent resistivity
ZXY = ZXYR + 1j * ZXYI
mod_zxy = np.abs(ZXY)
mod_loop_XY = mod_zxy**2
uo_loop_XY = frequencies * 2 * math.pi
resistivity_xy = mod_loop_XY / uo_loop_XY

# calculate |ZYX|
ZYX = ZYXR + 1j * ZYXI
mod_zyx = np.abs(ZYX)
mod_loop_YX = mod_zyx**2
uo_loop_YX = frequencies * 2 * math.pi
resistivity_yx = mod_loop_YX / uo_loop_YX
# Plotting
plt.figure(figsize=(10, 6))
plt.plot(frequencies, resistivity_xy, resistivity_yx, marker='o',   linestyle='-', color='b', label='Apparent Resistivity')
plt.xscale('log')  # Set logarithmic scale for x-axis
plt.yscale('log')  # Set logarithmic scale for y-axis
plt.xlabel('Frequency (Hz)')
plt.ylabel('Apparent Resistivity (Ohm.m)')
plt.title('Frequency vs Apparent Resistivity')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
'''
import numpy as np
import math
import matplotlib.pyplot as plt

# Function to parse the data from the file
def parse_data(file_name):
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
        'ZYX_VAR': [],
        'ZYYR': [],
        'ZYYI': [],
        'ZYY_VAR': [],
        'TXR': [],
        'TXI': [],
        'TX_VAR': [],
        'TYR': [],
        'TYI': [],
        'TY_VAR': []
    }

    section = None
    with open(file_name, 'r') as file:
        lines = file.readlines()

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

    return data

# Function to calculate resistivity from impedance components
def calculate_resistivity(Z_real, Z_imag, frequencies):
    Z_complex = Z_real + 1j * Z_imag
    mod_Z = np.abs(Z_complex)
    mod_squared = mod_Z**2
    uo = frequencies * 2 * math.pi
    resistivity = mod_squared / uo
    return resistivity
# functions to calculate phase
# Function to plot resistivity curves

def plot_resistivity(frequencies, resistivity_xy, resistivity_yx):
    plt.figure(figsize=(10, 6))
    plt.plot(-frequencies, resistivity_xy, marker='o', linestyle='-', color='g', label=' XY')
    plt.plot(-frequencies, resistivity_yx, marker='o', linestyle='-', color='b', label=' YX')
    plt.xscale('log')  # Set logarithmic scale for x-axis
    plt.yscale('log')  # Set logarithmic scale for y-axis
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Apparent Resistivity (Ohm.m)')
    plt.title('Frequency vs Resistivity')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


# Main program
if __name__ == "__main__":
    file_name = input("Enter Path of the file: ")
    data = parse_data(file_name)

    # Extract data from dictionary
    frequencies = np.array(data['frequencies'])
    ZXYR = np.array(data['ZXYR'])
    ZXYI = np.array(data['ZXYI'])
    ZYXR = np.array(data['ZYXR'])
    ZYXI = np.array(data['ZYXI'])

    # Calculate resistivity for XY and YX configurations
    resistivity_xy = calculate_resistivity(ZXYR, ZXYI, frequencies)
    resistivity_yx = calculate_resistivity(ZYXR, ZYXI, frequencies)

    # Plotting resistivity curves
    plot_resistivity(frequencies, resistivity_xy, resistivity_yx)

 