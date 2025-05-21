# Open Real Time Classification Model

This package contains example code to run the Real Time Anomaly Detection and Classification Model. It also provides time-series decomposition approaches in order to learn the seasonality and trands..

> [!NOTE]
> Note that this model rely over data acquisition from the sensors via different API using JSON. For test purposes, one may use CSV as given in [EA](https://environment.data.gov.uk/hydrology/explore)- however, model will ingest the data incrementally in a similar fashion as in real time sensor data stream. These datasets may be governed by separate terms and conditions or license provisions. 

> [!IMPORTANT]
> Your use of such third-party materials is subject to any such terms and you should check that you can comply with any applicable restrictions or terms and conditions before use.



## 1. Introduction
To protect public health and meet regulatory demands, **real-time water quality monitoring** is essential. This work presents an approach to detect and classifying anomalies in multiparameter time-series data-stream, ingested from water quality sensor. Furthermore, the system identifies unusual patterns—such as pollution or sensor faults—and categorizes them in real time. It learns from historical data to improve accuracy and scalability, and have detected live events such as sensor fouling, contamination, and rainfall for water utilities.

### Summary of data exploration:

A range of selected parameters were chosen that fall under Section 82 regulations such as 
- pH,
- Dissolved Oxygen,
- Turbidity,
- Ammonium,
- Electrical Conductivity,
> [!NOTE]
> Although, Electrical Conductivity is not the Section 82 parameter. It was prioritized in this framework as it typically responds the fastest during unexpected events, making it a reliable early indicator for anomaly detection.

## 2. Motivation
In response to the worsening state of UK rivers, the government is prioritising early pollution detection and real-time monitoring through the Environment Act 2021. While modern sensor networks generate vast, high frequency data, interpreting these at scale remains a significant challenge. Traditional methods rely on timely manual review processes and often fail to distinguish between natural variations, pollution events or sensor faults. This leads to costly equipment damage, failing to meet regulatory compliance and more importantly reduced ability to mitigate impact of pollution events.
 
To address this challenge, we have built a model for automatically detect, classify and validate diverse water quality events in real-time. 

## 3. Project Overview
<p><i>River Deep Mountain AI is an innovation project funded by the Ofwat Innovation Fund working collaboratively to develop open-source AI/ML models that can inform effective actions to tackle waterbody pollution. 
 
The project consists of 6 core partners: Northumbrian Water, Cognizant Ocean, Xylem Inc, Water Research Centre Limited, The Rivers Trust and ADAS. The project is further supported by 6 water companies across the United Kingdom and Ireland. </i></p>

## 4. Purpose and functionality
Online models process sensor data in real time, enabling immediate detection of anomalies like chemical spills or microbial contamination—offline models analyze data too late to prevent harm.

### Why offline predictions and classifications are not enough for water utilities?
- **Real-time decisions are critical** — water utilities must respond instantly to diverse unlikely events (e.g pollution) to avoid service disruptions and health risks.
- **Offline models miss dynamic patterns** — water conditions change rapidly, requiring continuous monitoring and adaptive analytics.
- **Regulatory and customer expectations demand immediacy** — delays in detection or response can lead to non-compliance, fines, and loss of public trust.

> [!NOTE]
> Why was time series decomposition is introduced and its historical values are ingested?

In general, water sensors generates multivariate time-series data. Time series decomposition separates this time series data into trend, seasonality, and residual components. One can use this information to understand underlying patterns and behaviors in the data.


### Possible extensions
- Real Time Multiparameter Anomaly Detection
- Real Time Sensor Fouling Event Detection
- Real Time Correlation Analysis
- Real Time Upstream and Downstream Data Analysis
- Real Time Event Classification


## 5. Installation instructions including requirements
Installation Guide
This guide walks you through setting up the **OpenRealTimeClassificationModel** project in your local or cloud environment.

> [!NOTE]
> This repository is shared for transparency and reproducibility. Code contributions are not accepted at this time.
 

### Directory Structure
    OpenRealTimeClassificationModel/
    ├── README.md                 # Project overview and usage instructions
    ├── MultiParameter.py         # Model for multi parameter
    ├── SingleParameter.py        # Model for single parameter
    ├── Decomposition and correlation matrix.ipynb       # Model for time series decomposition for single parameter
    ├── MODEL_CARD.md             # Model details (empty at the moment)
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
- numPy: Array and math operations
- animate

### Ingest Real Time Data and Run E2E pipeline
Input data should be either API callable via JSON or in the form of CSV:
```
datasets/
└── multiParameter/
    └── <your_folder>/
        ├── input
        └── ...
```


### Running the Model
Input multi parameter data stream could be obtain from JSON. Use the ```multiParameter.py``` to run the full pipeline.

### Planned Improvements
_Real-Time Event Classification planned_

- Dry weather sewage spills
- Dry weather agricultural pollution
- Runoff: pollution (there is a significant input of organic matter that produces a negative impact despite dilution effects)
- Runoff: dilution (changes associated with high rainfall – but no negative impact discernible from sensor data)  

## 6. Example usage (e.g., Jupyter notebooks) 
This package provides three pretrained models:

```singleParameter.py```: a single-parameter anomaly detection model, was tested over time series observations of Turbidity data from 2016 to 2018. This model can be causally evaluated on any online real-time data from data streams, where data can be ingested via any API, JSON, or online evolving CSV. The following image illustrates real-time anomaly detection in a turbidity dataset. The approach leverages the Interquartile Range (IQR) method to identify anomalies as data streams in, updating the detection algorithm on the fly. However, a key limitation of this method is its reduced sensitivity to long-term pollution trends.

<br>
<div align="center">
  <img width = "40%" src="https://github.com/user-attachments/assets/651ba1d3-0108-4078-86cd-7b6d9edfab94"><br>
  <figcaption>Real Time Anomaly Detection for Turbidity</figcaption>
</div><br>


```multiParameter.py```: a multi-parameter anomaly detection model, was tested over time series observations of Section 82 parameters along with electrical conductivity. This model can be causally evaluated on any online multi-parameter real-time sensor data from data streams, where data can be ingested via any API, JSON, or online evolving CSV.

<br>
<div align="center">
  <img width = "40%" src="https://github.com/user-attachments/assets/ffb96b6f-a468-44d0-b380-6de928b993ee"><br>
  <figcaption>Real Time Anomaly Detection in a Multiparameter Data Stream</figcaption>
</div>
<br>



```TimeComp.py```: A model that ingests a single parameter time series and decomposes it in order to identify the trends, seasonality, and patterns.  The best starting point is to open TimeDecomp.ipynb in VertaxAI, which gives an example of loading data and computing diverse components of a time series using prophet. Incorporating time series decomposition can enhance performance by capturing underlying trends and seasonal patterns that IQR alone may miss.

<br>
<div align="center">
  <img width = "40%" src="https://github.com/user-attachments/assets/5f2dab38-9227-49a2-8386-53033489cf0d"><br>
  <figcaption>Decomposition of pH</figcaption>
</div>
<br>


### Custom Data Collection
_Number of identified locations:_
- **England** - 8


### Training
- Unlike offline Machine Learning models, this model trains and ingest the sequentially and learn from it. 



> [!TIP]
> You do not need to perform manual labeling. The model is designed such as to capture the anomolies autonomously.
> You need to adjust the normalization in order to fit the chart over scale. This is user dependent.


### Identifying the anomalies

- The model identifies the anomolies in real-time and point the red dot over the anomly.
- Anomolies were directly exported to CSV file in binary format (0,1)
- Commonly detects sudden changes and variations in the time-series data


## 7. Links to datasets and dependencies 

Some of the multiparameter dataset can be obtained from hydrology data from EA i.e [EA](https://environment.data.gov.uk/hydrology/explore). The model is developed using Python and related dependencies. To run the model, you must install the valid libraries i.e [pandas](https://www.google.com), [matplotlib](https://matplotlib.org/), [prophet](https://facebook.github.io/prophet/), and [animation](https://matplotlib.org/stable/users/explain/animations/animations.html). 


## 8. Citation details for research papers
- Bhatia, S., Jain, A., Li, P., Kumar, R., & Hooi, B. (2021, April). Mstream: Fast anomaly detection in multi-aspect streams. In Proceedings of the Web Conference 2021 (pp. 3371-3382).
- Hall, J., Zaffiro, A. D., Marx, R. B., Kefauver, P. C., Krishnan, E. R., Haught, R. C., & Herrmann, J. G. (2007). On–Line water quality parameters as indicators of distribution system contamination. Journal‐American Water Works Association, 99(1), 66-77.
- Von Sperling, M. (2007). Wastewater characteristics, treatment and disposal. IWA publishing. 


## 9. Disclaimer 
Open Real Time Classification Model is an experimental research work developed as part of River Deep Mountain AI. You are fully responsible for assessing whether its use or distribution is appropriate for your needs. Any risks associated with using or distributing this model and its outputs are solely yours to assume.
 
By utilising Open Real Time Classification Model, you acknowledge and accept the rights and permissions granted under the relevant license. Exercise caution when relying on, publishing, downloading, or otherwise using Open Real Time Classification Model  or any generated outputs.


