
# ==============================
# This code animates real-time plotting of ammonia concentration from a CSV file. It uses the IQR method to detect outliers and marks anomalies in red. Data is logged frame-by-frame into a list and saved to a CSV when the plot window is closed. The background color changes based on current values to visually flag threshold crossings. The animation runs through the dataset frame by frame with no repeat.
# ==============================

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.animation as animation
from matplotlib.animation import writers

# ==============================
# Load sensor data as API or CSV. We use CSV at the point for simplicity. (paths hidden)
# ==============================
# Time reference
data_index = pd.read_csv('.../do.csv')  # Hidden path

# Ammonia sensor readings
data_complete = pd.read_csv('.../ammonia.csv')  # Hidden path
data = data_complete[0:1500]  # Limit to 1500 samples

# Extract time and values
time_data = data_index['index']
value_data = data['value']

# ==============================
# Function to detect anomalies using IQR
# ==============================
def detect_anomalies(values):
    """
    Uses IQR (Interquartile Range) to detect anomalies.
    Flags values outside Q1 - 1.5*IQR or Q3 + 1.5*IQR or above 30.
    """
    Q1 = values.quantile(0.25)
    Q3 = values.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    anomalies = (values < lower_bound) | (values > upper_bound) | (values > 30)
    return anomalies

# ==============================
# Set up the animated plot
# ==============================
fig, ax = plt.subplots()
default_facecolor = plt.rcParams['axes.facecolor']  # Default background

# For logging results
logged_data = []

# Animation frame update function
def animate(i):
    ax.clear()

    # Background color based on threshold
    if i > 0 and value_data[i - 1] > 10:
        ax.set_facecolor('white')
    else:
        ax.set_facecolor('white')

    # Plot line chart of values up to current index
    ax.plot(time_data[:i], value_data[:i], color='darkorange', label='Ammonia', linewidth=5)

    # Detect and plot anomalies
    anomalies = detect_anomalies(value_data[:i])
    ax.scatter(time_data[:i][anomalies], value_data[:i][anomalies], color='r', label='Anomaly', s=200)

    # Labeling
    ax.set_xlabel('t', fontsize=36)
    ax.set_ylabel('mg/L', fontsize=36)
    ax.grid(True)
    ax.legend(fontsize=36)
    ax.tick_params(axis='x', labelsize=24)
    ax.tick_params(axis='y', labelsize=24)
    plt.tight_layout()

    # Store each frame's data
    logged_data.append({
        'time': time_data[i],
        'value': value_data[i],
        'is_anomaly': int((i - 1) in anomalies) if i > 0 else 0
    })

# ==============================
# Save data on plot close
# ==============================
def on_close(event):
    df = pd.DataFrame(logged_data)
    df.to_csv('anomaly_logged_data_EC.csv', index=False)
    print("Logged data saved to 'anomaly_logged_data_EC.csv'")

# Connect close event
fig.canvas.mpl_connect('close_event', on_close)

# Run animation
ani = animation.FuncAnimation(fig, animate, frames=len(time_data), interval=0, repeat=False)
plt.tight_layout()
plt.show()

# ==============================
# (Optional) Save animation to MP4 using ffmpeg — currently commented
# ==============================
# matplotlib.rcParams['animation.ffmpeg_path'] = '.../ffmpeg.exe'
# writer = animation.FFMpegWriter(fps=30, bitrate=1800)
# ani.save("Turbidity.mp4", writer=writer)