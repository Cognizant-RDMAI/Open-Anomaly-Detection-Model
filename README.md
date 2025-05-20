# Open Real Time Classification Model

## 1. Introduction
To protect public health and meet regulatory demands, **real-time water quality monitoring** is essential. This work presents an approach to detect and classifying anomalies in multiparameter time-series data-stream, ingested from water quality sensor. Furthermore, the system identifies unusual patterns—such as pollution or sensor faults—and categorizes them in real time. It learns from historical data to improve accuracy and scalability, and have detected live events such as sensor fouling, contamination, and rainfall for water utilities.

### Summary of data exploration:

A range of selected parameters were chosen that fall under Section 82 regulations such as 
- pH,
- Dissolved Oxygen,
- Turbidity,
- Ammonium,
- Electrical Conductivity,


Although, Electrical Conductivity is not the Section 82 parameter. It was prioritized in this framework as it typically responds the fastest during unexpected events, making it a reliable early indicator for anomaly detection.


## 2. Motivation
- provided by Nicolai/Elisabeth

## 3. Project Overview
<p><i>River Deep Mountain AI is an innovation project funded by the Ofwat Innovation Fund working collaboratively to develop open-source AI/ML models that can inform effective actions to tackle waterbody pollution. 
 
The project consists of 6 core partners: Northumbrian Water, Cognizant Ocean, Xylem Inc, Water Research Centre Limited, The Rivers Trust and ADAS. The project is further supported by 6 water companies across the United Kingdom and Ireland. </i></p>

## 4. Purpose and functionality
Online models process sensor data in real time, enabling immediate detection of anomalies like chemical spills or microbial contamination—offline models analyze data too late to prevent harm.

### Why offline predictions and classifications are not enough for water utilities?
- **Real-time decisions are critical** — water utilities must respond instantly to diverse unlikely events (e.g pollution) to avoid service disruptions and health risks.
- **Offline models miss dynamic patterns** — water conditions change rapidly, requiring continuous monitoring and adaptive analytics.
- **Regulatory and customer expectations demand immediacy** — delays in detection or response can lead to non-compliance, fines, and loss of public trust.


### Why was time series decomposition is introduced and its historical values are ingested?
In general, water sensors generates multivariate time-series data. Time series decomposition separates this time series data into trend, seasonality, and residual components. One can use this information to understand underlying patterns and behaviors in the data.
<div align="center">
  <img width = "40%" src="https://github.com/user-attachments/assets/5f2dab38-9227-49a2-8386-53033489cf0d"><br>
  <figcaption>Code World</figcaption>
</div>

### Possible extensions
- Real Time Multiparameter Anomaly Detection
- Real Time Sensor Fouling Event Detection
- Real Time Correlation Analysis
- Real Time Upstream and Downstream Data Analysis
- Real Time Event Classification


## 5. Installation instructions including requirements
Installation Guide
This guide walks you through setting up the **OpenRealTimeClassificationModel** project in your local or cloud environment.
 
> **Note:** This repository is shared for transparency and reproducibility.  
> Code contributions are not accepted at this time.
 
--- 

### Directory Structure
    OpenRealTimeClassificationModel/
    ├── README.md                 # Project overview and usage instructions
    ├── MultiParameter.py         # Model for multi parameter
    ├── SingleParameter.py        # Model for single parameter
    ├── Decomposition and Correlation Matrix.py        # Model for single parameter
    ├── MODEL_CARD.md             # Model details
    ├── INSTALL.md                # Step-by-step installation instructions
    ├── CONTRIBUTING.md           # Contribution guidelines (internal use only)
    ├── CHANGELOG.md              # List of changes and improvements made to the project
    ├── requirements.txt          #python libraries required 
    └── LICENSE                   # Licensing information and usage rights

### Clone the repository
 
First, clone this project to your local machine or cloud environment
```https://github.com/Cognizant-RDMAI/OpenRealTimeClassificationModel```
This will download all project files including the model scripts
 
### Create a Python Virtual Environment (Optional but Recommended)
 
Using a virtual environment avoids conflicts with other Python packages on your system
```
python3 -m venv venv
source venv/bin/activate    #macOS/Linux
venv/Scripts/Activate       #Windows
```
This creates an isolated environment where all dependencies will be installed.

### Install Dependencies
 
All required Python packages are listed in the ```requirements.txt``` file. To install them:
```
pip install -r requirements.txt
```
This includes:
- matplotlib
- pandas
- NumPy: Array and math operations
- Animate

### Ingest Real Time Data and Run E2E pipeline
Input data should be either API callable via JSON or in the form of CSV:
```
datasets/
└── multiParameter/
    └── <your_folder>/
        ├── inpput
        └── ...
```
Use the ```multiparameter.py``` to run the full pipeline


## 6. Example usage (e.g., Jupyter notebooks) 
The following image illustrates real-time anomaly detection in a turbidity dataset. The approach leverages the Interquartile Range (IQR) method to identify anomalies as data streams in, updating the detection algorithm on the fly. However, a key limitation of this method is its reduced sensitivity to long-term pollution trends. Incorporating time series decomposition can enhance performance by capturing underlying trends and seasonal patterns that IQR alone may miss.

- Single Parameter

<div align="center">
  <img width = "40%" src="https://github.com/user-attachments/assets/651ba1d3-0108-4078-86cd-7b6d9edfab94"><br>
  <figcaption>Code World</figcaption>
</div>

- Multiparameter 
<div align="center">
  <img width = "40%" src="https://github.com/user-attachments/assets/ffb96b6f-a468-44d0-b380-6de928b993ee"><br>
  <figcaption>Code World</figcaption>
</div>


## 7. Links to datasets and dependencies 

Some of the multiparameter dataset can be obtained from hydrology data from EA i.e [EA](https://www.google.com), [matplotlib](https://matplotlib.org/),


The model is developed using Python and related dependencies. To run the model, you must install the valid libraries i.e [pandas](https://www.google.com), [matplotlib](https://matplotlib.org/), [prophet](https://facebook.github.io/prophet/), and [animation](https://matplotlib.org/stable/users/explain/animations/animations.html). 


## 8. Citation details for research papers
- Bhatia, S., Jain, A., Li, P., Kumar, R., & Hooi, B. (2021, April). Mstream: Fast anomaly detection in multi-aspect streams. In Proceedings of the Web Conference 2021 (pp. 3371-3382).
- Hall, J., Zaffiro, A. D., Marx, R. B., Kefauver, P. C., Krishnan, E. R., Haught, R. C., & Herrmann, J. G. (2007). On–Line water quality parameters as indicators of distribution system contamination. Journal‐American Water Works Association, 99(1), 66-77.
- Von Sperling, M. (2007). Wastewater characteristics, treatment and disposal. IWA publishing. 


## 9. Disclaimer 
Open Real Time Classification Model is an experimental research work developed as part of River Deep Mountain AI. You are fully responsible for assessing whether its use or distribution is appropriate for your needs. Any risks associated with using or distributing this model and its outputs are solely yours to assume.
 
By utilising Open Real Time Classification Model, you acknowledge and accept the rights and permissions granted under the relevant license. Exercise caution when relying on, publishing, downloading, or otherwise using Open Real Time Classification Model  or any generated outputs.
