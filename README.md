# BB3AB-Real-Time-Multiparameter-Anomaly-Identification-and-Detection

Introduction for the model (what is this? ) 
Motivation (provided by Nicolai/Elisabeth - I will send to you before EOD today)
Project overview (short, provided by Nicolai/Elisabeth - see text above) 
Purpose and functionality  
Installation Instructions including requirements 
Example usage (e.g., Jupyter notebooks) 
Links to datasets and dependencies 
Citation details for research papers ,  
Disclaimer (provided by Nicolai /Elisabeth - see text above) 






## 1. Introduction
To safeguard public health and protect the environment, online and continuous water quality monitoring is crucial for the water sector. Regulatory compliance also necessitates deploying real-time monitoring solutions, which can capture the evolving states of a particular river or water network and provide online information on diverse events (e.g., pollution, CSO, etc.). This work introduces a comprehensive end-to-end (E2E) framework that combines online data ingestion and ascertains real-time anomaly detection for water utilities in the UK.  Online multiparameter time-series data can originate from various sources such as SCADA systems, IoT-based sensors, or sondes deployed in water utilities. These platforms continuously collect environmental data across multiple parameters, enabling real-time monitoring of water quality. A key challenge in this context is detecting anomalies—sudden or unusual changes in the data that may indicate pollution events, sensor faults, or operational issues.  Once detected, it is equally important to categorize these anomalies to distinguish between natural variations, technical errors, and potential threats to water safety. Therefore, our approach focuses on detecting anomalies in continuous water quality monitoring data followed by categorizing anomalies in continuous monitoring data. We capture this heterogeneous time series data and classify anomalies incrementally with respect to time. Second, this approach is scalable and can ingest multiparameter time series data, as required. The model also learns critical features from historical observations to understand the past behavior of parameters to improve accuracy. For validation, the system successfully detected a live sensor fouling event, indicated by a decline in Turbidity and conductivity.    This method strengthens real-time surveillance and supports water utilities in making prompt, informed decisions. 


## 2. Motivation
- provided by Nicolai/Elisabeth

## 3. Project Overview
_River Deep Mountain AI is an innovation project funded by the Ofwat Innovation Fund working collaboratively to develop open-source AI/ML models that can inform effective actions to tackle waterbody pollution. 
 
The project consists of 6 core partners: Northumbrian Water, Cognizant Ocean, Xylem Inc, Water Research Centre Limited, The Rivers Trust and ADAS. The project is further supported by 6 water companies across the United Kingdom and Ireland._

## 4. Purpose and functionality


## 5. Installation Instructions including requirements



## 6. Example usage (e.g., Jupyter notebooks) 

## 7. Links to datasets and dependencies 
The model is developed using Python and related dependencies. To run the model, you must install the valid libraries i.e [pandas](https://www.google.com), [matplotlib](https://matplotlib.org/), [prophet](https://facebook.github.io/prophet/), and [animation](https://matplotlib.org/stable/users/explain/animations/animations.html). 


## 8. Citation details for research papers

- Bhatia, S., Jain, A., Li, P., Kumar, R., & Hooi, B. (2021, April). Mstream: Fast anomaly detection in multi-aspect streams. In Proceedings of the Web Conference 2021 (pp. 3371-3382).
- Hall, J., Zaffiro, A. D., Marx, R. B., Kefauver, P. C., Krishnan, E. R., Haught, R. C., & Herrmann, J. G. (2007). On–Line water quality parameters as indicators of distribution system contamination. Journal‐American Water Works Association, 99(1), 66-77.
- Von Sperling, M. (2007). Wastewater characteristics, treatment and disposal. IWA publishing. 


## 9. Disclaimer 
Open Real Time Classification Model is an experimental research work developed as part of River Deep Mountain AI. You are fully responsible for assessing whether its use or distribution is appropriate for your needs. Any risks associated with using or distributing this model and its outputs are solely yours to assume.
 
By utilising Open Real Time Classification Model, you acknowledge and accept the rights and permissions granted under the relevant license. Exercise caution when relying on, publishing, downloading, or otherwise using Open Real Time Classification Model  or any generated outputs.



## 2. Dependencies



## 3. Summary of data exploration:

A range of selected parameters were chosen taking into account values of interest and those that fall under Section 82 regulations and include pH, dissolved oxygen, turbidity, conductivity, temperature, chlorophyll (cphyll), ammonium, and saturated dissolved oxygen percentage. These readings provide a detailed temporal record of water quality conditions.  


## 4. Directory Structure
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


# License and Disclaimers

The Colab notebooks and the associated code are licensed under MIT 4.0. You may obtain a copy of the License at: [MIT](https://opensource.org/license/mit)

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


# Citations
To be updated


# References


# Acknowledgements
To be Updated

 
