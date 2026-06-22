# 📊 Employee Salary Prediction App

### 🌐 Live Demo

https://drive.google.com/file/d/1vX76monxcbm3Bsjtp5avAt851eqeUvB6/view?usp=sharing

---

# 📌 Overview

Employee Salary Prediction App is an interactive Machine Learning web application developed using **Streamlit** that enables users to upload their own employee dataset and predict salaries using multiple regression algorithms.

The application automates the complete Machine Learning workflow, including data preprocessing, model training, evaluation, and visualization, making it suitable for HR analytics, salary benchmarking, and educational purposes.

---

# 🚀 Features

* 📁 Upload any CSV dataset
* 🎯 Select the target column (Salary)
* 🔄 Automatic data preprocessing

  * Handle missing values
  * Encode categorical features
  * Feature scaling
  * Train-test split
* 🤖 Multiple Machine Learning models

  * Linear Regression
  * Decision Tree Regressor
  * Random Forest Regressor
  * Support Vector Regressor (SVR)
  * Gradient Boosting Regressor
* 📊 Performance evaluation

  * R² Score
  * Mean Absolute Error (MAE)
  * Mean Squared Error (MSE)
* 📈 Interactive Plotly visualizations
* 🔥 Correlation Heatmap
* 🌳 Feature Importance (Random Forest)

---

# 🛠 Tech Stack

| Technology   | Purpose                   |
| ------------ | ------------------------- |
| Python       | Programming Language      |
| Streamlit    | Web Application           |
| Pandas       | Data Processing           |
| NumPy        | Numerical Operations      |
| Scikit-learn | Machine Learning          |
| Plotly       | Interactive Charts        |
| Matplotlib   | Data Visualization        |
| Seaborn      | Statistical Visualization |

---

# 📂 Project Structure

```
Employee-Salary-Predictor/
│
├── main.py                 # Streamlit Application
├── README.md               # Project Documentation
├── requirements.txt        # Dependencies
└── dataset.csv             # Sample Dataset (Optional)
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/your-username/employee-salary-predictor.git
```

## 2. Navigate to Project Folder

```bash
cd employee-salary-predictor
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Run Application

```bash
streamlit run main.py
```

---

# 📊 Application Workflow

```
User Uploads Dataset
        │
        ▼
Dataset Validation
        │
        ▼
Target Column Selection
        │
        ▼
Data Preprocessing
        │
        ├── Handle Missing Values
        ├── Encode Categorical Variables
        ├── Feature Scaling
        └── Train-Test Split
        │
        ▼
Model Selection
        │
        ▼
Model Training
        │
        ▼
Performance Evaluation
        │
        ▼
Visualization & Prediction Results
```

---

# 🤖 Machine Learning Models

The application supports the following regression models:

### 1. Linear Regression

Simple regression algorithm used as the baseline model.

### 2. Decision Tree Regressor

Builds a tree-based model capable of capturing nonlinear relationships.

### 3. Random Forest Regressor

An ensemble learning algorithm that combines multiple decision trees for improved prediction accuracy.

### 4. Support Vector Regressor (SVR)

Uses Support Vector Machines for regression tasks and performs well with complex datasets.

### 5. Gradient Boosting Regressor

Builds multiple weak learners sequentially to create a highly accurate prediction model.

---

# 📈 Model Evaluation Metrics

The application evaluates every trained model using:

* R² Score
* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)

These metrics help compare model performance and identify the most accurate algorithm.

---

# 📊 Visualizations

The application provides multiple interactive visualizations:

* Dataset Preview
* Correlation Heatmap
* Actual vs Predicted Salary Plot
* Feature Importance Chart
* Interactive Plotly Graphs

---

# 📌 Use Cases

* HR Analytics
* Salary Benchmarking
* Workforce Planning
* Data Science Learning
* Machine Learning Projects
* Employee Compensation Analysis

---

# ⚠️ Requirements

* Dataset must be in CSV format.
* Target column should contain numeric salary values.
* Missing values are automatically handled.
* Categorical features are encoded before model training.
* Large datasets may require additional processing time.

---

# 📦 Dependencies

```
streamlit
pandas
numpy
scikit-learn
matplotlib
seaborn
plotly
```

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

# 🌟 Future Enhancements

* Hyperparameter tuning
* Cross-validation
* Model download
* Prediction API
* Model persistence using Joblib
* Explainable AI (SHAP)
* Advanced feature engineering
* User authentication

---


If you found this project helpful, consider giving it a ⭐ on GitHub.
