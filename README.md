# Open Real Time Classification Model

## 1. Introduction
To safeguard public health and protect the environment, online and continuous water quality monitoring is crucial for the water sector. Regulatory compliance also necessitates deploying real-time monitoring solutions, which can capture the evolving states of a particular river or water network and provide online information on diverse events (e.g., pollution, CSO, etc.). This work introduces a comprehensive end-to-end (E2E) framework that combines online data ingestion and ascertains real-time anomaly detection for water utilities in the UK.  Online multiparameter time-series data can originate from various sources such as SCADA systems, IoT-based sensors, or sondes deployed in water utilities. These platforms continuously collect environmental data across multiple parameters, enabling real-time monitoring of water quality. A key challenge in this context is detecting anomalies—sudden or unusual changes in the data that may indicate pollution events, sensor faults, or operational issues.  Once detected, it is equally important to categorize these anomalies to distinguish between natural variations, technical errors, and potential threats to water safety. Therefore, our approach focuses on detecting anomalies in continuous water quality monitoring data followed by categorizing anomalies in continuous monitoring data. We capture this heterogeneous time series data and classify anomalies incrementally with respect to time. Second, this approach is scalable and can ingest multiparameter time series data, as required. The model also learns critical features from historical observations to understand the past behavior of parameters to improve accuracy. For validation, the system successfully detected a live sensor fouling event, indicated by a decline in Turbidity and conductivity.    This method strengthens real-time surveillance and supports water utilities in making prompt, informed decisions. 

### Summary of data exploration:

A range of selected parameters were chosen taking into account values of interest and those that fall under Section 82 regulations and include pH, dissolved oxygen, turbidity, conductivity, temperature, chlorophyll (cphyll), ammonium, and saturated dissolved oxygen percentage. These readings provide a detailed temporal record of water quality conditions.  


## 2. Motivation
- provided by Nicolai/Elisabeth

## 3. Project Overview
<p><i>River Deep Mountain AI is an innovation project funded by the Ofwat Innovation Fund working collaboratively to develop open-source AI/ML models that can inform effective actions to tackle waterbody pollution. 
 
The project consists of 6 core partners: Northumbrian Water, Cognizant Ocean, Xylem Inc, Water Research Centre Limited, The Rivers Trust and ADAS. The project is further supported by 6 water companies across the United Kingdom and Ireland. </i></p>

## 4. Purpose and functionality

### Why offline predictions and classifications are not enough for water utilities?

### Real Time Anomaly Detection and Classification?

- Single Parameter

<div align="center">
  <img width = "40%" src="https://github.com/user-attachments/assets/651ba1d3-0108-4078-86cd-7b6d9edfab94">
</div>

- Multiparameter 
<div align="center">
  <img width = "40%" src="https://github.com/user-attachments/assets/ffb96b6f-a468-44d0-b380-6de928b993ee">
</div>

### Why was time series decomposition is introduced and its historical values are ingested?

<div align="center">
  <img width = "40%" src="https://github.com/user-attachments/assets/5f2dab38-9227-49a2-8386-53033489cf0d">
</div>

### Challenges and alternatives


## 5. Installation Instructions including requirements
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
