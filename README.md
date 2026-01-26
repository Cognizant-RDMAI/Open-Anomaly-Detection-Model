# Open Anomaly Detection Model
---

## Motivation, Purpose, Challenges, and Justification

<p align="justify">
Continuous monitoring of river water quality under <b>Section 82 of the Environment Act 2021</b> generates very high-frequency multi-parameter data that cannot be reviewed manually. To extract maximum value from these monitoring programs, there is a clear need for <b>robust, automated methods</b> for anomaly detection, including.
</p>

<ul>
<li>Enable <b>automated detection of pollution events</b> and anomalies in high-frequency water quality data.</li>
<li>Provide a <b>scalable framework</b> for multi-parameter sensor data ingestion, decomposition, and clustering.</li>
<li>Support <b>interpretability and domain expert analysis</b> through visualizations, including PCA biplots and cluster overlays.</li>
</ul>

<p align="justify">
<b>Challenges:</b><br>
The high-frequency, multi-parameter nature of river water quality data makes manual review <b>impractical</b>. Complex temporal patterns, seasonal variations, and multivariate interactions make <b>anomaly detection difficult</b>. Automated, robust methods are <b>needed</b> to extract actionable insights and support regulatory compliance efficiently.
</p>

<p align="justify">
<b>Prior Work & Improvement:</b><br>
Previous research focused on single-parameter or low-frequency datasets, often missing multivariate patterns and temporal trends. This work provides an <b>end-to-end multi-parameter framework</b> with robust pipelines using <b>MSTL decomposition, Butterworth filtering, harmonic regression, Isolation Forest, and KMeans clustering</b> to detect complex anomalies.
</p>

<p align="justify">
<b>Advantages:</b><br>
The framework enables <b>automated, high-frequency anomaly detection</b> and clustering across multiple water quality parameters. It provides <b>interpretable outputs and visualizations</b> to support timely decision-making and expert analysis.
</p>

<p align="justify">
<b>Justification:</b><br>
Regulatory requirements and high-frequency multivariate data make manual review impractical. Our approach combines <b>statistical decomposition, unsupervised learning, and visual analytics</b>, providing a <b>scalable, robust, and interpretable solution</b> that previous methods cannot achieve.
</p>

## Project Details

[River Deep Mountain AI](https://www.cognizant.com/us/en/industries/ocean/rdmai) is an innovation project funded by the **Ofwat Innovation Fund**, working collaboratively to develop **open-source AI/ML models** that can inform effective actions to tackle waterbody pollution.

The project consists of **6 core partners**:  
- Northumbrian Water  
- Cognizant Ocean  
- Xylem Inc  
- Water Research Centre Limited  
- The Rivers Trust  
- ADAS  

The project is further supported by **6 water companies** across the **United Kingdom and Ireland**.


### Possible extensions
- Real Time Multiparameter Anomaly Detection
- Sensor Fouling Event Detection
- Correlation Analysis
- Upstream and Downstream Data Analysis
- Automated Event Classification

## Report
Open Anomal Detection Model Report is available [here](https://python-poetry.org/docs/#installation)


## Installation instructions including requirements
### Project Setup Guide

This guide walks you through setting up the **OpenMultiparameterAnomalyDetectionModel** project in your local or cloud environment.
### Clone the Repository

First, you need to clone this repository to your local machine. If you are new to Git, open a terminal and run the following commands:

```
git clone https://github.com/Cognizant-RDMAI/Open-Multiparameter-Anomaly-Detection-Model.git
cd Open-Multiparameter-Anomaly-Detection-Model
```

This will download the project into a new folder named Open-Multiparameter-Anomaly-Detection-Model and navigate you into it.



### Water Quality Data Pipeline

The `load_and_prepare_data` function ingests and cleans Section 82 water quality data. It aligns six key variables (`do`, `ph`, `turb`, `amm`, `cond`, `temp`) to a common datetime index, removes duplicates, fills missing values, and produces a clean combined DataFrame ready for analysis.

**Key Steps:**

- **Hourly Resampling:** Converts raw data to hourly means for consistent time series analysis.  
- **Range Selection:** Focuses on a user-defined time frame. Warns if the selected range is less than one year, as short data may affect seasonal and residual decomposition accuracy.  
- **Missing Data Handling:** Detects fully missing days and groups consecutive missing days for review.  
- **Optional Interpolation:** Prompts the user to fill missing values. Interpolation is required for MSTL decomposition, ensuring evenly spaced, complete time series so trends, seasonality, and residuals are estimated reliably.

✅ Ensures clean, aligned, and complete data for downstream analysis and MSTL-based seasonal decomposition.


**Run `OpenAnomalyModel.ipynb`**  
   - Install the dependencies.
   - Ingest the data as specified format.
   - Approximate runtime: **1 minutes** on an M1 Mac.

### Directory Structure
      OpenRealAnomalynModel/
      ├── README.md 
      ├── MODEL_CARD.md
      ├── INSTALL.md
      ├── CONTRIBUTING.md
      ├── CHANGELOG.md
      ├── requirements.txt
      ├── LICENSE
      └── notebooks/
          ├── OpenAnomalyModel.ipynb
          └── infer_periods.ipynb



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


