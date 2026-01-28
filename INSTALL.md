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
cd Open-Multiparameter-Anomaly-Detection-Model
```


This will download all project files, including notebooks, scripts, and example datasets.
 
### 2. **Python Environment (Used by Jupyter)**

Jupyter Notebook runs code using a Python kernel, which is tied to a specific Python environment. To ensure reproducible results and correct library versions, this project is tested with:

**Python 3.12**

We recommend creating an isolated environment and launching Jupyter from it.

#### Option A: Conda

```bash
conda create -n openanomaly python=3.13
conda activate openanomaly
pip install -r requirements.txt
jupyter notebook

```

#### Option B: venv
```bash
python3.13 -m venv venv
source venv/bin/activate    # macOS/Linux
venv\Scripts\activate       # Windows
pip install -r requirements.txt
jupyter notebook

```

For Windows:
```bash
venv\Scripts\activate
```
> **Note:**
> If you are using a managed environment (Google Colab, Azure ML, SageMaker), make sure the runtime uses Python 3.12 and install dependencies from requirements.txt. The notebook will then use that Python environment as its kernel.

This installs all dependencies required for:

- Time-series decomposition
- Anomaly detection
- Clustering
- Visualization
- Jupyter Notebook execution
- Dataset Structure and Input Format


Expected directory structure:

```bash
datasets/
└── multiParameter/
    └── <your_dataset_name>/
        ├── input/
        │   └── example.csv
        └── output/
```

An example CSV file is included in the repository to illustrate the required format.


### 3. Input data can be provided:
- as CSV files stored locally


### 4. Timestamp Format

All datetime values must follow this format:

```bash
YYYY-MM-DD HH:MM
```

### 5. Running the Model

The full anomaly detection pipeline is executed using the provided Jupyter Notebook.

Launch Jupyter:

```bash
jupyter notebook
```

- Open the main notebook in the repository
- Confirm the dataset path points to the appropriate datasets/ directory
- Run all notebook cells sequentially


