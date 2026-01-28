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
Open-Multiparameter-Anomaly-Detection-Model/
│
├── notebooks/
│   ├── OpenAnomalyModel.ipynb        # Main notebook / pipeline
│   └── infer_periods.py              # Helper module used by notebook
│
├── data/
│   └── sample_data/                  # Example or test datasets
│       └── example.csv
│
│
├── docs/                             # Documentation files
│   ├── INSTALL.md
│   ├── README.md
│   ├── CHANGELOG.md
│   ├── CONTRIBUTING.md
│   └── model-card.md
│
├── requirements.txt                  # Python dependencies
├── LICENSE

```

An example CSV file is included in the repository to illustrate the required format.


### 3. Input data must be ingested as follows:
The script is ingest, clean, and align Section 82 water quality data for analysis.
It ensures that all expected variables are present and ready for downstream processing.

Key Features:
- Automatically checks for missing or extra variables
- Aligns timestamps across variables
- Handles both single-file and multi-file inputs
- Prepares a clean DataFrame suitable for MSTL decomposition, clustering, or other analysis

Supported Inputs:
#### Multiple CSVs
- Provide a dictionary mapping variable names to CSV file paths. Example:

```bash
csv_dict = {
    'do': 'datasets/do.csv',
    'ph': 'datasets/ph.csv',
    'turb': 'datasets/turb.csv',
    'amm': 'datasets/amm.csv',
    'cond': 'datasets/cond.csv',
    'temp': 'datasets/temp.csv'
}
df = load_and_prepare_data(csv_dict)
```

#### Single CSV
Provide a single CSV containing all expected variables in columns:
```bash
df = load_and_prepare_data('datasets/multi_parameter.csv')
```
**Expected Variables**

```bash
['do', 'ph', 'turb', 'amm', 'cond', 'temp']

```


### 4. Timestamp Format

All datetime values must follow this format:

```bash
YYYY-MM-DD HH:MM
```

### 5.Helper Module

The repository includes a helper module, `infer_periods.py`, which is used internally by the main notebook and scripts to extract seasonal periods.

> **Note:** This file is already included in the repository and does **not** require separate installation. Ensure it remains in the same directory as the notebook when executing the pipeline.

Example usage inside the notebook:

```python
import infer_periods
from infer_periods import extractPeriods

```

### 6. Running the Model

The full anomaly detection pipeline is executed using the provided Jupyter Notebook.

Launch Jupyter:

```bash
jupyter notebook
```

- Open the main notebook in the repository
- Confirm the dataset path points to the appropriate datasets/ directory
- Run all notebook cells sequentially


