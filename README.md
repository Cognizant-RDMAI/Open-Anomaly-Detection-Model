# BB3AB-Real-Time-Multiparameter-Anomaly-Identification-and-Detection-
Real-Time Anomalies Detection and Classification 

Multiparameter Water Quality Anomaly Detection 

This project visualizes and detects anomalies in real-time sensor data for multiple water quality parameters, such as: 

Dissolved Oxygen (DO) 

pH 

Turbidity 

Ammonia 

Electrical Conductivity (EC) 

Anomalies are detected using the IQR (Interquartile Range) method and visualized in a dynamic Matplotlib animation. 

📁 Files 

main_plot.py: Main Python script for real-time visualization and anomaly detection. 

*.csv: Sensor data files for different parameters (e.g., DO, pH, turbidity). 

anomaly_logged_data_*.csv: Auto-generated log files of detected anomalies during visualization. 

📊 Features 

Real-time animated plotting of multiple parameters. 

Outlier detection using statistical thresholds (IQR). 

Dynamic background color changes based on thresholds. 

Saves anomaly data automatically on window close. 

Optional export of animation to .mp4 using FFmpeg. 

🧪 Requirements 

Install required Python packages: 

pip install pandas matplotlib 

To enable video export, download and install FFmpeg, and update the path in the script: 

matplotlib.rcParams['animation.ffmpeg_path'] = "path_to_ffmpeg" 

▶️ Usage 

Place all sensor CSV files in the same directory. 

Ensure CSV files have at least the following columns: 

index (timestamp or row number) 

value (sensor reading) 

Run the script: 

python main_plot.py 

When the plot window is closed, anomaly logs will be saved to CSV. 

📌 Notes 

Current anomaly detection is univariate (IQR). You can extend it using Mahalanobis distance for multivariate detection. 

For larger datasets, consider optimizing performance or using data streaming libraries. 

📷 Sample Output 

Real-time animated chart with colored lines for each parameter and red markers for anomalies. 

🧠 Future Enhancements 

Mahalanobis-based multivariate anomaly detection. 

Dashboard integration (e.g., using Dash or Plotly). 

Sensor calibration checks and alerting system. 

 
