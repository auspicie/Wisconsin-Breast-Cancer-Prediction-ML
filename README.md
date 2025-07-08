# 🧬 Breast Cancer Prediction using Machine Learning

## 📌 Overview

This project applies machine learning techniques to predict whether a breast tumor is \*\*malignant\*\* or \*\*benign\*\* using the Wisconsin Breast Cancer Diagnostic dataset. It leverages various clinical features extracted from digitized images of fine needle aspirates (FNAs) to assist in early cancer detection and decision-making support.

## 🚀 Features

- Exploratory Data Analysis

- Data Preprocessing: Handling missing values, feature scaling
- Model Selection: Evaluation of multiple ML classifiers (Logistic Regression, KNN, SVM, Random Forest, XGBoost, etc.)
- Performance Metrics: Accuracy, precision, recall, F1-score, ROC-AUC curve
- Model Saving: Export of trained model and scaler for deployment
- Deployment: Streamlit app for interactive prediction

## 🛠️ Installation

**Clone the repository**

```bash
git clone https://github.com/auspicie/Breast-Cancer_Prediction-ML.git
cd Breast-Cancer_Prediction-ML

**Install dependencies**

pip install -r requirements.txt
```

## 💻 Usage
**Run the Streamlit app:**
streamlit run Cancer_app.py

## 📷 Streamlit App Preview
![Diabetes App Screenshot] (https://github.com/auspicie/Wisconsin-Breast-Cancer-Prediction-ML/blob/fe2be02877895e96135047f16b3c904ce67759af/Breast%20Cancer.png)
---

## 📊 Dataset
-**Name:** Wisconsin Breast Cancer Diagnostic Dataset  
- **Source:**[Kaggle](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data)
- *Size:** 569 samples × 30 features + 1 target
- **Target Variable:** `diagnosis` (`M = Malignant`, `B = Benign`)

## 🤝 Contributing
Contributions are welcome! Feel free to:
Open an issue
Submit a pull request

## 📄 License
This project is licensed under the [MIT License](LICENSE).

## 📌 Notes
- Ensure that the `heart\_disease\_model.pkl` and `scaler.pkl` are in the same directory as the app.
### Author: Samsudeen Bankole
Built with ❤️ using Streamlit and Scikit-learn.





