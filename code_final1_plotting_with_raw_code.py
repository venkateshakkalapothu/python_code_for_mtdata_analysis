# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 22:39:22 2024

@author: MT_field_1
"""

import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Function to process each file

phase_max, phase_min, strike_angle_degrees, skew_angle_degrees,indu_vect_real_leng, indu_vect_real_angle_degrees=0,0,0,0,0,0

def process_file(file_path):
    global phase_max, phase_min, strike_angle_degrees, skew_angle_degrees,indu_vect_real_leng, indu_vect_real_angle_degrees
    with open(file_path, 'r') as file:
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
        elif line.startswith('>TXR'):
            section='TXR'
        elif line.startswith('>TXI'):
            section='TXI'
        elif line.startswith('>TXVAR.EXP'):
            section='TX_VAR'
        elif line.startswith('>TYR.EXP'):
            section='TYR'
        elif line.startswith('>TYI.EXP'):
            section='TYI'
        elif line.startswith('>TYVAR.EXP'):
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

    # Phase tensor calculations using numpy
    dot_x = ZXXR * ZYYR - ZXYR * ZYXR
    inverse_x = np.reciprocal(dot_x)
    pi_xx = inverse_x * (ZYYR * ZXXI - ZXYR * ZYXI)
    pi_xy = inverse_x * (ZYYR * ZXYI - ZXYR * ZYYI)
    pi_yx = inverse_x * (ZXXR * ZYXI - ZYXR * ZXXI)
    pi_yy = inverse_x * (ZXXR * ZYYI - ZYXR * ZXYI)

    # Phase tensor parameters
    trace_phase = pi_xx + pi_yy
    skew = pi_xy + pi_yx
    det_phase = pi_xx * pi_yy - pi_xy * pi_yx

    # Calculate phase tensor attributes
    phase_1 = trace_phase / 2
    phase_2 = np.sqrt(np.abs(det_phase))  # Use np.abs to ensure no negative values inside sqrt
    phase_3 = skew / 2

    # Phase - Minimum
    term1 = np.sqrt(np.maximum((phase_1**2) + (phase_3**2) - np.maximum((phase_1**2) + (phase_3**2) - (phase_2**2), 0), 0))
    term2 = np.sqrt(np.maximum((phase_1**2) + (phase_3**2), 0))
    phase_min = term1 - term2

    # Phase - Maximum
    term1 = np.sqrt(np.maximum((phase_1**2) + (phase_3**2) - np.maximum((phase_1**2) + (phase_3**2) - (phase_2**2), 0), 0))
    term2 = np.sqrt(np.maximum((phase_1**2) + (phase_3**2), 0))
    phase_max = term1 + term2

    # Skew angle
    skew_angle_radians = np.arctan2(pi_xy - pi_yx, pi_xx + pi_yy) / 2
    skew_angle_degrees = np.degrees(skew_angle_radians)

    # Strike angle
    strike_angle_radians = np.arctan2(pi_xy + pi_yx, pi_xx - pi_yy) / 2
    strike_angle_degrees = np.degrees(strike_angle_radians)

    # Subtracting phase maximum and minimum
    phase_max_min = phase_max - phase_min

    indu_vect_real_angle = np.arctan2(TYR, TXR)
    indu_vect_real_angle_degrees = np.degrees(indu_vect_real_angle)

    indu_vect_imag_angle = np.arctan2(TYI, TXI)
    indu_vect_imag_angle_degrees = np.degrees(indu_vect_imag_angle)

    indu_vect_real_leng = np.sqrt(TXR**2 + TYR**2)
    indu_vect_img_leng = np.sqrt(TXI**2 + TYI**2)

    # Print results for debugging
    plot_index = int(input('Select Index : '))

    #getting index values : 
    print(frequencies[plot_index])
    print(phase_min[plot_index])
    print(phase_max[plot_index])
    print(skew_angle_degrees[plot_index])
    print(strike_angle_degrees[plot_index])
    print(indu_vect_real_angle_degrees[plot_index])
    print(indu_vect_imag_angle_degrees[plot_index])
    print( indu_vect_real_leng[plot_index])
    print(indu_vect_img_leng[plot_index])
    
    
import os
# Directory containing the files
folder_path = input("Enter the path of the folder:").strip().strip("'").strip('"')

# Iterate through each file in the directory
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        process_file(file_path)

import numpy as np
import os

# Function to parse latitude and longitude from a line
def parse_lat_lon(line):
    parts = line.split('=')
    if len(parts) == 2:
        key, value = parts
        if key.strip() == 'LAT':
            return value.strip(), 'LAT'
        elif key.strip() == 'LONG':
            return value.strip(), 'LONG'
    return None, None

# List to store latitudes and longitudes
latitudes = []
longitudes = []

# Directory containing the files
folder_path = folder_path

# Iterate over each file in the folder
for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)

    # Extract latitudes and longitudes
    with open(file_path, 'r') as file:
        lines = file.readlines()
        inside_head = False
        for line in lines:
            line = line.strip()
            if line.startswith('>HEAD'):
                inside_head = True
            elif inside_head and line.startswith('>'):
                inside_head = False

            if inside_head:
                value, key = parse_lat_lon(line)
                if value and key:
                    # Convert from D:M:S to decimal degrees
                    parts = value.split(':')
                    if len(parts) == 3:
                        degrees = float(parts[0])
                        minutes = float(parts[1]) / 60
                        seconds = float(parts[2]) / 3600
                        decimal_value = degrees + minutes + seconds
                        if key == 'LAT':
                            latitudes.append(decimal_value)
                        elif key == 'LONG':
                            longitudes.append(decimal_value)

# Convert lists to numpy arrays
latitudes = np.array(latitudes)
longitudes = np.array(longitudes)

print("Latitudes:", latitudes)
print("Longitudes:", longitudes)



# Define the plotting function
def plot_data(latitudes, longitudes, phase_max, phase_min, strike_angle_degrees, skew_angle_degrees, indu_vect_real_leng, indu_vect_real_angle_degrees):
    fig, ax = plt.subplots()

    # Plot the data points
    scatter = ax.scatter(longitudes, latitudes, color='white', label='Data Points')

    # Normalize skew angle degrees for color mapping
    norm = plt.Normalize(skew_angle_degrees.min(), skew_angle_degrees.max())
    cmap = plt.get_cmap('viridis')

    # Add ellipses to the plot
    for (x, y, major, minor, angle, skew) in zip(longitudes, latitudes, phase_max, phase_min, strike_angle_degrees, skew_angle_degrees):
        ellipse = patches.Ellipse(
            (x, y),                  # center of the ellipse
            width=major *0.004,         # major axis length
            height=minor *0.004 ,        # minor axis length
            angle=angle,             # angle of rotation (degrees)
            edgecolor='black',
            facecolor=cmap(norm(skew))  # Color based on skew angle
        )
        ax.add_patch(ellipse)

    # Draw arrows
    for (x, y, length, angle) in zip(longitudes, latitudes, indu_vect_real_leng, indu_vect_real_angle_degrees):
        dx = length * np.cos(np.deg2rad(angle))
        dy = length * np.sin(np.deg2rad(angle))
        ax.arrow(x, y, dx, dy, head_width=0.005, head_length=0.0025, fc='red', ec='red')

    # Set labels and title
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.set_title('Phase Tensor')

    # Set aspect ratio to equal for proper ellipse representation
    ax.set_aspect('equal', 'box')

    # Add a color bar for skew angle degrees
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    cbar = plt.colorbar(sm, ax=ax)
    cbar.set_label('Skew Angle Degrees')

    # Optionally, set the limits to make sure everything fits well
    ax.set_xlim(longitudes.min() - 0.1, longitudes.max() + 0.1)
    ax.set_ylim(latitudes.min() - 0.1, latitudes.max() + 0.1)

    # Show grid for better visibility
    ax.grid(True)

    # Show the plot
    plt.show()

# Example usage (assuming the lists are populated as in your script)
plot_data(latitudes, longitudes, phase_max, phase_min, strike_angle_degrees, skew_angle_degrees, indu_vect_real_leng, indu_vect_real_angle_degrees)
