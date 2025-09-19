

# SafeTransact: Fraud Detection in Financial Transactions

SafeTransact is a data science project that uses machine learning to identify fraudulent financial transactions. It provides tools for data analysis, model training, and an interactive Streamlit web app for real-time fraud prediction. The project helps users explore transaction data, visualize patterns, and deploy a fraud detection model easily.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
  - [Jupyter Notebook](#jupyter-notebook)
  - [Streamlit App](#streamlit-app)
- [File Descriptions](#file-descriptions)
-

---

## Project Overview
This project aims to:
- Analyze transaction data to understand patterns of fraud.
- Engineer features that help distinguish between legitimate and fraudulent transactions.
- Build and evaluate a machine learning model to predict fraud.
- Provide an interactive web interface for users to test the model on new data.

## Features
- **Data Exploration:** Visualize and summarize transaction data.
- **Feature Engineering:** Create new features to improve model performance.
- **Model Training:** Train and evaluate a fraud detection model (e.g., Random Forest, Logistic Regression).
- **Streamlit App:** User-friendly web app for real-time fraud prediction.
- **Visualization:** Correlation heatmaps, distribution plots, and more.

## Project Structure
- `fraud_detection.py` — Streamlit app for fraud detection.
- `analysis_model.ipynb` — Jupyter notebook for data analysis and model development.
- `AIML Dataset.csv` — Transaction dataset used for training and analysis.
- `fraud_detection_pipeline.pkl` — Saved machine learning pipeline/model.
- `README.md` — Project documentation.

## Requirements
Install the following Python packages:
- streamlit
- pandas
- numpy
- scikit-learn
- seaborn
- matplotlib

You can install all dependencies with:
```bash
pip install streamlit pandas numpy scikit-learn seaborn matplotlib
```

## Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/safeTransact.git
   cd safeTransact
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   # or manually as shown above
   ```
3. **(Optional) Prepare the dataset:**
   Ensure `AIML Dataset.csv` is present in the project directory.

## Usage

### Jupyter Notebook
Open `analysis_model.ipynb` in Jupyter Notebook or VS Code. Run the cells sequentially to:
- Explore the dataset
- Visualize data distributions and correlations
- Engineer features
- Train and evaluate the fraud detection model
- Save the trained model pipeline

### Streamlit App
To launch the web app:
```bash
python -m streamlit run fraud_detection.py
```
This will open a browser window where you can interact with the fraud detection model, upload new data, and view predictions.


## File Descriptions
- **fraud_detection.py**: Streamlit web app for fraud prediction.
- **analysis_model.ipynb**: Notebook for EDA, feature engineering, and model training.
- **AIML Dataset.csv**: Transaction data. 
   - [Download AIML Dataset.csv](<https://www.kaggle.com/datasets/amanalisiddiqui/fraud-detection-dataset?resource=download>)
- **fraud_detection_pipeline.pkl**: Serialized model pipeline for use in the app.
- **README.md**: Project documentation and instructions.




