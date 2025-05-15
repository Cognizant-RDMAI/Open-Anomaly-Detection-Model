


# ===============================
# This code reads water quality sensor data (e.g., DO, pH, turbidity) from CSV files and visualizes it in real time using Matplotlib. It calculates anomalies using the IQR method and highlights them on the plot as red points. The animate() function updates the plot frame by frame to simulate live data streaming. The background color changes dynamically based on turbidity values. Finally, the animation is saved as an MP4 video using FFmpeg.
# ===============================


import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ===============================
# Load data from online APIs or CSVs (paths hidden). We use CSV here for demo purpose.
# ===============================
# Read time index from a representative CSV (assumes same for all)
data_index = pd.read_csv('.../DO.csv')  # Hidden path

# Load measurement data from multiple CSV files (paths hidden)
data_DO = pd.read_csv('.../DO.csv')
data_pH = pd.read_csv('.../pH.csv')
data_turb = pd.read_csv('.../turbidity.csv')
data_amm = pd.read_csv('.../ammonia.csv')
data_cond = pd.read_csv('.../conductivity.csv')

# Extract time and sensor values
time_data = data_index['index']  # Time reference for all sensors
value_data_DO = data_DO['value']
value_data_pH = data_pH['value']
value_data_turb = data_turb['value']
value_data_amm = data_amm['value']
value_data_cond = data_cond['value'] * 0.01  # Scale conductivity

# =================================
# Function to detect anomalies
# =================================
def detect_anomalies(values):
    """
    Detect outliers using the IQR method:
    - Below Q1 - 1.5 * IQR or above Q3 + 1.5 * IQR
    - Also flags values below 0.5 as anomalous (specific for DO)
    """
    Q1 = values.quantile(0.25)
    Q3 = values.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    anomalies = (values < lower_bound) | (values > upper_bound) | (values < 0.5)
    return anomalies

# =================================
# Animation setup
# =================================
fig, ax = plt.subplots()

def animate(i):
    """
    Update the plot frame-by-frame.
    Displays real-time sensor data and highlights anomalies.
    """
    ax.clear()

    # Change background color if turbidity exceeds threshold
    if i > 0 and value_data_turb[i - 1] > 10:
        ax.set_facecolor('white')
    else:
        ax.set_facecolor('white')

    # Plot sensor data
    ax.plot(time_data[:i], value_data_DO[:i], color='b', label='Dissolved Oxygen (mg/L)', linewidth=5)
    ax.plot(time_data[:i], value_data_pH[:i], color='peru', label='pH', linewidth=5)
    ax.plot(time_data[:i], value_data_turb[:i], color='lime', label='Turbidity (NTU)', linewidth=5)
    ax.plot(time_data[:i], value_data_amm[:i], color='#118ab2', label='Ammonia (mg/L)', linewidth=5)
    ax.plot(time_data[:i], value_data_cond[:i], color='magenta', label='Conductivity (µS)', linewidth=5)

    # Detect and plot anomalies for each sensor
    anomalies_DO = detect_anomalies(value_data_DO[:i])
    anomalies_pH = detect_anomalies(value_data_pH[:i])
    anomalies_turb = detect_anomalies(value_data_turb[:i])
    anomalies_amm = detect_anomalies(value_data_amm[:i])
    anomalies_cond = detect_anomalies(value_data_cond[:i])

    ax.scatter(time_data[:i][anomalies_DO], value_data_DO[:i][anomalies_DO], color='r', label='Anomaly', s=200)
    ax.scatter(time_data[:i][anomalies_pH], value_data_pH[:i][anomalies_pH], color='r', s=200)
    ax.scatter(time_data[:i][anomalies_turb], value_data_turb[:i][anomalies_turb], color='r', s=200)
    ax.scatter(time_data[:i][anomalies_amm], value_data_amm[:i][anomalies_amm], color='r', s=200)
    ax.scatter(time_data[:i][anomalies_cond], value_data_cond[:i][anomalies_cond], color='r', s=200)

    # Set labels, grid, and formatting
    ax.set_xlabel('Time', fontsize=36)
    ax.set_ylabel('Normalized Values', fontsize=36)
    ax.grid(True)
    ax.legend(fontsize=24)
    ax.tick_params(axis='x', labelsize=24)
    ax.tick_params(axis='y', labelsize=24)
    plt.tight_layout()

# =================================
# Run animation and save video
# =================================
ani = animation.FuncAnimation(fig, animate, frames=len(time_data), interval=10, repeat=False)
plt.tight_layout()
plt.show()

# Set FFmpeg path for saving animation (path hidden)
matplotlib.rcParams['animation.ffmpeg_path'] = '.../ffmpeg.exe'
writer = animation.FFMpegWriter(fps=30, bitrate=1800)

# Save the animation as an MP4 file
ani.save('anomaly_detection_output.mp4', writer=writer)