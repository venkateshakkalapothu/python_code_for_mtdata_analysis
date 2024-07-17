# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 16:21:27 2024

@author: MTS
"""

import numpy as np
import matplotlib.pyplot as plt

def read_data(file_name):
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

    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()

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
                section = 'TXR'
            elif line.startswith('TXI.EXP'):
                section = 'TXI'
            elif line.startswith('TXVAR.EXP'):
                section = 'TX_VAR'
            elif line.startswith('TYR.EXP'):
                section = 'TYR'
            elif line.startswith('TYI.EXP'):
                section = 'TYI'
            elif line.startswith('TYVAR.EXP'):
                section = 'TY_VAR'
            elif line.startswith('>'):
                section = None
            elif section:
                values = [float(val) for val in line.split()]
                data[section].extend(values)

    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found. Please enter correct Path")
        return None

    return data

if __name__ == '__main__':
    file_name = input("Enter Path of the file:")
    data = read_data(file_name)

    if data:
        frequencies = np.array(data['frequencies'])
        time_periods = np.reciprocal(frequencies)
        ZXX = np.array(data['ZXXR']) + 1j * np.array(data['ZXXI'])
        ZXY = np.array(data['ZXYR']) + 1j * np.array(data['ZXYI'])
        ZYX = np.array(data['ZYXR']) + 1j * np.array(data['ZYXI'])
        ZYY = np.array(data['ZYYR']) + 1j * np.array(data['ZYYI'])
        
        
        
        
        
'''
def plot_impedance(frequencies, ZXX, ZXY, ZYX, ZYY, time_periods):
    fig = plt.figure(figsize=(12, 8))
    gs = GridSpec(2, 2, figure=fig)

    ax1 = fig.add_subplot(gs[0, 0])
    ax1.plot(frequencies, np.abs(ZXX), label='|ZXX|')
    ax1.plot(frequencies, np.abs(ZXY), label='|ZXY|')
    ax1.set_xscale('log')
    ax1.set_yscale('log')
    ax1.set_xlabel('Frequency (Hz)')
    ax1.set_ylabel('Magnitude')
    ax1.set_title('Impedance Magnitude')
    ax1.legend()

    ax2 = fig.add_subplot(gs[0, 1])
    ax2.plot(frequencies, np.angle(ZXX, deg=True), label='Phase ZXX')
    ax2.plot(frequencies, np.angle(ZXY, deg=True), label='Phase ZXY')
    ax2.set_xscale('log')
    ax2.set_xlabel('Frequency (Hz)')
    ax2.set_ylabel('Phase (degrees)')
    ax2.set_title('Impedance Phase')
    ax2.legend()

    ax3 = fig.add_subplot(gs[1, :])
    ax3.plot(time_periods, ZYX.real, label='ZYX (Real part)')
    ax3.plot(time_periods, ZYX.imag, label='ZYX (Imaginary part)')
    ax3.set_xlabel('Time Period (s)')
    ax3.set_ylabel('Impedance')
    ax3.set_title('Impedance Over Time')
    ax3.legend()

    plt.tight_layout()
    plt.show()
'''

       # plot_impedance(frequencies, ZXX, ZXY, ZYX, ZYY, time_periods)
