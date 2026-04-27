# 📊 Employee Salary Prediction App

An interactive **Machine Learning web app** built using Streamlit that allows users to upload their dataset and predict employee salaries using multiple regression models.


## 🚀 Features

* 📁 Upload your own CSV dataset
* 🎯 Select target column (Salary)
* 🔄 Automatic data preprocessing:

  * Handling missing values
  * Encoding categorical variables
  * Feature scaling
* 🤖 Train multiple ML models:

  * Linear Regression
  * Decision Tree
  * Random Forest
  * Support Vector Machine (SVM)
  * Gradient Boosting
* 📊 Model performance metrics:

  * R² Score
  * MAE (Mean Absolute Error)
  * MSE (Mean Squared Error)
* 📈 Interactive visualizations using Plotly
* 🔥 Correlation heatmap using Seaborn
* 🌳 Feature importance (Random Forest)


## 🛠️ Tech Stack

* Python 🐍
* Streamlit
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Plotly


## 📂 Project Structure

📁 Employee-Salary-Predictor
│── app.py          # Main Streamlit application
│── README.md       # Project documentation
│── requirements.txt

## ⚙️ Installation & Setup

1. Clone the repository:
bash
git clone https://github.com/your-username/employee-salary-predictor.git
cd employee-salary-predictor

2. Install dependencies:
bash
pip install -r requirements.txt

3. Run the app:
bash
streamlit run app.py

## 📊 How It Works

1. Upload a CSV dataset
2. Select the **target column (Salary)**
3. App automatically:

   * Encodes categorical variables
   * Scales features
   * Splits data into train/test sets
4. Choose ML models from sidebar
5. View:

   * Model performance
   * Actual vs Predicted plots
   * Correlation heatmap
   * Feature importance

## 📈 Models Used

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor
* Support Vector Regressor (SVR)
* Gradient Boosting Regressor

All models are implemented using Scikit-learn.

## 📌 Example Use Case

* HR analytics
* Salary benchmarking
* Workforce planning
* Data science learning projects

## ⚠️ Notes

* Ensure your dataset is clean and relevant
* Target column must be numeric
* Large datasets may take longer to process

