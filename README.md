**# BB3AB-Real-Time-Multiparameter-Anomaly-Identification-and-Detection-**

To safeguard public health and protect the environment, online and continuous water quality monitoring is crucial for the water sector. Regulatory compliance also necessitates deploying real-time monitoring solutions, which can capture the evolving states of a particular river or water network and provide online information on diverse events (e.g., pollution, CSO, etc.). This work introduces a comprehensive end-to-end (E2E) framework that combines online data ingestion and ascertains real-time anomaly detection for water utilities in the UK.  Online multiparameter time-series data can originate from various sources such as SCADA systems, IoT-based sensors, or sondes deployed in water utilities. These platforms continuously collect environmental data across multiple parameters, enabling real-time monitoring of water quality. A key challenge in this context is detecting anomalies—sudden or unusual changes in the data that may indicate pollution events, sensor faults, or operational issues. 
Once detected, it is equally important to categorize these anomalies to distinguish between natural variations, technical errors, and potential threats to water safety. Therefore, our approach focuses on detecting anomalies in continuous water quality monitoring data followed by categorizing anomalies in continuous monitoring data. We capture this heterogeneous time series data and classify anomalies incrementally with respect to time. Second, this approach is scalable and can ingest multiparameter time series data, as required. The model also learns critical features from historical observations to understand the past behavior of parameters to improve accuracy. For validation, the system successfully detected a live sensor fouling event, indicated by a decline in Turbidity and conductivity.    This method strengthens real-time surveillance and supports water utilities in making prompt, informed decisions. 

**Advantages:**

Real-Time Anomalies Detection and Classification 

Multiparameter Water Quality Anomaly Detection 

**This project visualizes and detects anomalies in real-time sensor data for multiple water quality parameters, such as:**

Dissolved Oxygen (DO) 

pH 

Turbidity 

Ammonia 

Electrical Conductivity (EC) 

Anomalies are detected using the IQR (Interquartile Range) method and visualized in a dynamic Matplotlib animation. 


**Summary of data exploration:**

 

The dataset includes water quality readings from ten catchment areas: Clayhithe, Crimple Back, Lee Lea Bridge, Lee Springfield, Monks Leaze, Pymmes Brook East, Pymmes Brook West, Wharfe, and Witcombe. Each location is identified using upstream and downstream sensor data.  

A range of selected parameters were chosen taking into account values of interest and those that fall under Section 82 regulations and include pH, dissolved oxygen, turbidity, conductivity, temperature, chlorophyll (cphyll), ammonium, and saturated dissolved oxygen percentage.  

Data was collected over a period from September 15, 2014, to December 15, 2016. Each variable has a total of 37,255 readings. These readings provide a detailed temporal record of water quality conditions.  

The sensors captured both chemical and physical indicators to help assess environmental health. Data consistency across all locations allows for comparative analysis. 





**Files**

main_plot.py: Main Python script for real-time visualization and anomaly detection. 


anomaly_logged_data_*.csv: Auto-generated log files of detected anomalies during visualization. 

**Features**

Real-time animated plotting of multiple parameters. 

Outlier detection using statistical thresholds (IQR). 

Dynamic background color changes based on thresholds. 

Saves anomaly data automatically on window close. 

Optional export of animation to .mp4 using FFmpeg. 

**Requirements**

Install required Python packages: 

pip install pandas matplotlib 

To enable video export, download and install FFmpeg, and update the path in the script: 

matplotlib.rcParams['animation.ffmpeg_path'] = "path_to_ffmpeg" 

**Usage**


index (timestamp or row number) 

value (sensor reading) 

Run the script: 

python main_plot.py 

When the plot window is closed, anomaly logs will be saved to CSV. 

**Notes**

Current anomaly detection is univariate (IQR). You can extend it using Mahalanobis distance for multivariate detection. 

For larger datasets, consider optimizing performance or using data streaming libraries. 

**Sample Output** 

Real-time animated chart with colored lines for each parameter and red markers for anomalies. 

**Future Enhancements**

Mahalanobis-based multivariate anomaly detection. 

Dashboard integration (e.g., using Dash or Plotly). 

Sensor calibration checks and alerting system. 

 
