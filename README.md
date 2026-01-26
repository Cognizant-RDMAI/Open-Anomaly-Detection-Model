# Open Multiparameter Anomaly Detection Model
---

## Motivation, Purpose, Challenges, and Justification

Continuous monitoring of river water quality under **Section 82 of the Environment Act 2021** generates very high-frequency multi-parameter data that cannot be reviewed manually.  
To extract maximum value from these monitoring programs, there is a clear need for **robust, automated methods** for anomaly detection and event analysis.  

- Enable **automated detection of pollution events** and anomalies in high-frequency water quality data.  
- Provide a **scalable framework** for multi-parameter sensor data ingestion, decomposition, and clustering.  
- Support **interpretability and domain expert analysis** through visualizations, including PCA biplots and cluster overlays.  

**Challenges:**  
The high-frequency, multi-parameter nature of river water quality data makes manual review **impractical**.  
Complex temporal patterns, seasonal variations, and multivariate interactions make **anomaly detection difficult**.  
Automated, robust methods are **needed** to extract actionable insights and support regulatory compliance efficiently.

**Prior Work & Improvement:**  
Previous research focused on single-parameter or low-frequency datasets, often missing multivariate patterns and temporal trends.  
This work provides an **end-to-end multi-parameter framework** with robust pipelines using **MSTL decomposition, Butterworth filtering, harmonic regression, Isolation Forest, and KMeans clustering** to detect complex anomalies.

**Advantages:**  
The framework enables **automated, high-frequency anomaly detection** and clustering across multiple water quality parameters.  
It provides **interpretable outputs and visualizations** to support timely decision-making and expert analysis.

**Justification:**  
Regulatory requirements and high-frequency multivariate data make manual review impractical.  
Our approach combines **statistical decomposition, unsupervised learning, and visual analytics**, providing a **scalable, robust, and interpretable solution** that previous methods cannot achieve.


## 1. Introduction
Under Section 82 of the Environment Act 2021, sewerage undertakers are required to continuously monitor receiving water quality upstream and downstream of their assets. Meeting this requirement necessitates robust analytical methods that can:

Analyse high-frequency sensor data (typically 15-minute to 1-hour intervals)

Detect anomalous behaviour and potential pollution events

Support operational response and regulatory reporting

This framework integrates historical and real-time multi-parameter sensor data into a complete analytical pipeline:

Data ingestion → preprocessing → decomposition → anomaly detection → clustering → visualization

The pipeline is designed to operate incrementally, making it suitable for real-time deployment while remaining transparent and interpretable for regulatory and operational use.

[!IMPORTANT]
Use of third-party datasets or materials is subject to their respective terms and conditions. Users are responsible for ensuring compliance with any applicable licenses or usage restrictions.


## 2. Motivation
The ecological status of UK rivers has declined significantly in recent years, prompting increased regulatory emphasis on early pollution detection and real-time monitoring. While modern sensor networks generate large volumes of high-frequency data, extracting actionable insight from these data streams remains challenging.

Traditional approaches often rely on:

Manual inspection of time series

Static threshold-based rules

Retrospective (offline) analysis

These methods struggle to distinguish between natural variability, sensor faults, and genuine pollution events, leading to delayed response, unnecessary operational costs, equipment damage, and regulatory non-compliance.

To address these limitations, this project develops an automated framework capable of detecting, grouping, and supporting interpretation of diverse water quality anomalies in near real time, while retaining transparency for expert review.

## 3. Project Overview
<p><i>River Deep Mountain AI is an innovation project funded by the Ofwat Innovation Fund working collaboratively to develop open-source AI/ML models that can inform effective actions to tackle waterbody pollution. 
 
The project consists of 6 core partners: Northumbrian Water, Cognizant Ocean, Xylem Inc, Water Research Centre Limited, The Rivers Trust and ADAS. The project is further supported by 6 water companies across the United Kingdom and Ireland. </i></p>

## 4. Purpose and functionality
Online models process sensor data in real time, enabling immediate detection of anomalies like chemical spills or microbial contamination—offline models analyze data too late to prevent harm.

- **Decisions making** — water utilities must respond instantly to diverse unlikely events (e.g pollution) to avoid service disruptions and health risks.
- **Dynamic system behaviour** — water quality exhibits strong temporal and seasonal variability.
- **Regulatory and customer expectations demand immediacy** — delays in detection or response can lead to non-compliance, fines, and loss of public trust.

The model was designed to work as part of a fully automated End-to-End (E2E) sensor data pipeline. It performs the following core functions:
- **Anomaly Detection**
   - Multi parameter

-  **Scalability**: Process the data array at a time $t$. Can be expended to include further parameters, however, this may increase computational complexity and lower the speed. The may create synchronisation challenges.



> [!NOTE]
> Why was time series decomposition is introduced and its historical values are ingested?

Water quality data exhibit strong trends and seasonality. Decomposition separates observations into trend, seasonal, and residual components, allowing anomalies to be detected relative to expected behaviour rather than raw values alone.


### Possible extensions
- Real Time Multiparameter Anomaly Detection
- Sensor Fouling Event Detection
- Correlation Analysis
- Upstream and Downstream Data Analysis
- Automated Event Classification


## 5. Installation instructions including requirements
Installation Guide
This guide walks you through setting up the **OpenRealTimeClassificationModel** project in your local or cloud environment.

> [!NOTE]
> This repository is shared for transparency and reproducibility. Code contributions are not accepted at this time.
 

### Directory Structure
    OpenRealTimeClassificationModel/
    ├── README.md                 # Project overview and usage instructions
    ├── MultiparameterAnomalyDetectionModel.ipynb        # Model for multi parameter
    ├── infer_periods.ipynb       
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




### Summary of data exploration:

A range of selected parameters were chosen that fall under Section 82 regulations such as 
- pH,
- Dissolved Oxygen,
- Turbidity,
- Ammonium,
- Temperature
- Electrical Conductivity,

> [!NOTE]
> Although, Electrical Conductivity is not the Section 82 parameter. It was prioritized in this framework as it typically responds the fastest during unexpected events, making it a reliable early indicator for anomaly detection.


### Identifying the anomalies

- The model identifies the anomolies in real-time and point the red dot over the anomly.
- Anomolies were directly exported to CSV file in binary format (0,1)
- Commonly detects sudden changes and variations in the time-series data


## 7. Links to datasets and dependencies 

Some of the multiparameter dataset can be obtained from hydrology data from EA i.e [EA](https://environment.data.gov.uk/hydrology/explore). The model is developed using Python and related dependencies. To run the model, you must install the valid libraries i.e [pandas](https://www.google.com), [matplotlib](https://matplotlib.org/), [prophet](https://facebook.github.io/prophet/), and [animation](https://matplotlib.org/stable/users/explain/animations/animations.html). 

# Disclaimer 

River Deep Mountain AI (“RDMAI”) consists of **10 parties**. The parties currently participating in RDMAI are listed at the end of this section and are collectively referred to in these terms as the **“consortium”**.

This section provides additional context and usage guidance specific to the artificial intelligence models and/or software (the **“Software”**) distributed under the **MIT License**. It **does not modify or override the terms of the MIT License**. In the event of any conflict between this section and the terms of the MIT License, the **MIT License terms shall take precedence**.

---

## 1. Research and Development Status

The Software has been created as part of a **research and development project** and reflects a **point-in-time snapshot** of an evolving project. It is provided **without any warranty, representation, or commitment** of any kind, including with regards to:  
- Title  
- Non-infringement  
- Accuracy  
- Completeness  
- Performance  

The Software is for **information purposes only** and it is **not**:  
1. Intended for **production use** unless the user **accepts full liability** for its use and independently validates that the Software is appropriate for its intended purpose.  
2. Intended to be the **basis of making any decision** without independent validation.  

No party, including any member of the development consortium, is obligated to provide **updates, maintenance, or support** in relation to the Software and/or any associated documentation.


2. **Software Knowledge Cutoff**  
The Software was trained on publicly available data up to **September 2015**. It may not reflect current scientific understanding, environmental conditions, or regulatory standards. Users are solely responsible for verifying the accuracy, timeliness, and applicability of any outputs.

3. **Experimental and Generative Nature**  
The Software may exhibit limitations, including but not limited to:  
  - Inaccurate, incomplete, or misleading outputs  
  - Embedded biases and/or assumptions in training data  
  - Non-deterministic and/or unexpected behaviour  
  - Limited transparency in model logic or decision-making  

Users must **critically evaluate and independently validate** all outputs and exercise independent scientific, legal, and technical judgment when using the Software and/or any outputs. The Software is **not a substitute** for professional expertise and/or regulatory compliance.






4. **Usage Considerations**

- **Bias and Fairness:**  
  The Software may reflect biases present in its training data. Users are responsible for identifying and mitigating such biases in their applications.

- **Ethical and Lawful Use:**  
  The Software is intended solely for lawful, ethical, and development purposes. It must not be used in any way that could result in harm to individuals, communities, and/or the environment, or in any way that violates applicable laws and/or regulations.

- **Data Privacy:**  
  The Software was trained on publicly available datasets. Users must ensure compliance with all applicable data privacy laws and licensing terms when using the Software in any way.

- **Environmental and Regulatory Risk:**  
  Users are **not permitted** to use the Software for environmental monitoring, regulatory reporting, or decision making in relation to public health, public policy, and/or commercial matters. Any such use is in violation of these terms and undertaken entirely at the user’s **sole risk and discretion**.




## 5. No Liability
- **The Software is not permitted for use** in environmental monitoring, regulatory compliance, or decision making in relation to public health, public policy, and/or commercial matters.

- **Any use of the Software in such contexts** is in violation of these terms and undertaken entirely at the user’s own risk.

- **The development consortium and all consortium members, contributors, and their affiliates expressly disclaim any responsibility or liability** for any use of the Software including (but not limited to):
  - **Environmental, ecological, public health, public policy, or commercial outcomes**
  - **Regulatory and/or legal compliance failures**
  - **Misinterpretation, misuse, or reliance on the Software’s outputs**
  - **Any direct, indirect, incidental, or consequential damages arising from use of the Software**, including (but not limited to):
    - Loss of profit
    - Loss of use
    - Loss of income
    - Loss of production or accruals
    - Loss of anticipated savings
    - Loss of business or contracts
    - Loss or depletion of goodwill
    - Loss of goods
    - Loss or corruption of data, information, or software
    - Pure economic loss
    - Wasted expenditure resulting from use of the Software — whether arising in contract, tort, or otherwise, even if foreseeable


Users assume full responsibility for their use of the Software, validating the Software’s outputs and for any decisions and / or actions taken based on their use of the Software and / or its outputs.


## 8. Consortium Members
- Northumbrian Water Limited
- Cognizant Worldwide Limited
- Xylem Water Solutions UK Limited
- Water Research Centre Limited
- RSK ADAS Limited
- The Rivers Trust
- Wessex Water Limited
- Northern Ireland Water
- Southwest Water Limited
- Anglian Water Services Limited



## 8. Citation details for research papers
- Bhatia, S., Jain, A., Li, P., Kumar, R., & Hooi, B. (2021, April). Mstream: Fast anomaly detection in multi-aspect streams. In Proceedings of the Web Conference 2021 (pp. 3371-3382).
- Hall, J., Zaffiro, A. D., Marx, R. B., Kefauver, P. C., Krishnan, E. R., Haught, R. C., & Herrmann, J. G. (2007). On–Line water quality parameters as indicators of distribution system contamination. Journal‐American Water Works Association, 99(1), 66-77.
- Von Sperling, M. (2007). Wastewater characteristics, treatment and disposal. IWA publishing. 


## 9. Disclaimer 
Open Real Time Classification Model is an experimental research work developed as part of River Deep Mountain AI. You are fully responsible for assessing whether its use or distribution is appropriate for your needs. Any risks associated with using or distributing this model and its outputs are solely yours to assume.
 
By utilising Open Real Time Classification Model, you acknowledge and accept the rights and permissions granted under the relevant license. Exercise caution when relying on, publishing, downloading, or otherwise using Open Real Time Classification Model  or any generated outputs.


