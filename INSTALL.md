Installation Guide
This guide walks you through setting up the **BB3AB - Slurry-Real Time Multiparameter Anomaly Identification and Detection** project in your local or cloud environment.
 
> **Note:** This repository is shared for transparency and reproducibility.  
> Code contributions are not accepted at this time.
 
--- 
## Installation Instructions
### 1. Clone the repository
 
First, clone this project to your local machine or cloud environment
```https://github.com/Cognizant-RDMAI/BB3AB-Real-Time-Multiparameter-Anomaly-Identification-and-Detection```
This will download all project files including the model scripts
 
### 2. Create a Python Virtual Environment (Optional but Recommended)
 
Using a virtual environment avoids conflicts with other Python packages on your system
```
python3 -m venv venv
source venv/bin/activate    #macOS/Linux
venv/Scripts/Activate       #Windows
```
This creates an isolated environment where all dependencies will be installed.

### 3. Install Dependencies
 
All required Python packages are listed in the ```requirements.txt``` file. To install them:
```
pip install -r requirements.txt
```
This includes:
- matplotlib
- pandas
- NumPy: Array and math operations
- Animate

### 3. Ingest Real Time Data and Run E2E pipeline
Input data should be either API callable via JSON or in the form of CSV:
```
datasets/
└── multiParameter/
    └── <your_folder>/
        ├── inpput
        └── ...
```
Use the ```multiparameter.py``` to run the full pipeline
