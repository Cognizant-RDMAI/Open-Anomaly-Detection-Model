# Installation Guide

This guide walks you through setting up the **OpenAnomalyModel** project in a local or cloud environment.

> **Note:** This repository is shared for transparency and reproducibility.  
> Code contributions are not accepted at this time.

---

## Installation Instructions

### 1. Clone the Repository

Clone the project to your local machine or cloud environment:

```bash
git clone https://github.com/Cognizant-RDMAI/Open-Multiparameter-Anomaly-Detection-Model.git
cd Open-Multiparameter-Anomaly-Detection-Model```
This will download all project files, including notebooks, scripts, and example datasets.
 
### 2. **Create a Python Environment (Recommended)**

This project is tested with Python 3.13.

Option A: Conda
conda create -n openanomaly python=3.13
conda activate openanomaly

Option B: venv
python3.13 -m venv venv
source venv/bin/activate


For Windows:

venv\Scripts\activate

3. Install Dependencies
```bash
pip install -r requirements.txt
```

This installs all dependencies required for:

time-series decomposition

anomaly detection

clustering

visualization

Jupyter Notebook execution

Dataset Structure and Input Format

Input data can be provided either:

via an API callable returning JSON, or

as CSV files stored locally

Expected directory structure:

datasets/
└── multiParameter/
    └── <your_dataset_name>/
        ├── input/
        │   └── example.csv
        └── output/


An example CSV file is included in the repository to illustrate the required format.

Timestamp Format

All datetime values must follow this format:

YYYY-MM-DD HH:MM

Running the Model

The full anomaly detection pipeline is executed using the provided Jupyter Notebook.

Launch Jupyter:

jupyter notebook


Open the main notebook in the repository

Confirm the dataset path points to the appropriate datasets/ directory

Run all notebook cells sequentially

Note:
Earlier documentation referenced a multiparameter.py script; the current implementation runs entirely through the Jupyter Notebook.
