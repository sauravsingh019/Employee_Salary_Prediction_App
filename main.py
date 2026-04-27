import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

st.set_page_config(page_title="Employee Salary Predictor", layout="wide")
st.title("📊 Employee Salary Prediction App")

st.sidebar.header("Upload Your Dataset")
file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

if file:
    df = pd.read_csv(file)
    st.subheader("Preview of Dataset")
    st.dataframe(df.head())

    # Select target column
    target = st.selectbox("Select the target column (Salary)", df.columns)

    # Drop rows with missing target values
    df = df.dropna(subset=[target])

    # Encode non-numeric columns
    for col in df.select_dtypes(include='object').columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col].astype(str))

    # Feature/Target split
    X = df.drop(target, axis=1)
    y = df[target]

    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Train/Test split
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    st.sidebar.header("Choose Models to Train")
    model_choices = st.sidebar.multiselect("Select ML Models", 
        ["Linear Regression", "Decision Tree", "Random Forest", "SVM", "Gradient Boosting"], 
        default=["Linear Regression", "Random Forest"])

    models = {
        "Linear Regression": LinearRegression(),
        "Decision Tree": DecisionTreeRegressor(),
        "Random Forest": RandomForestRegressor(),
        "SVM": SVR(),
        "Gradient Boosting": GradientBoostingRegressor()
    }

    results = {}

    st.subheader("Model Performance")
    for name in model_choices:
        model = models[name]
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        r2 = r2_score(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)

        results[name] = {
            "R² Score": round(r2, 3),
            "MAE": round(mae, 3),
            "MSE": round(mse, 3),
            "Predictions": y_pred
        }

        st.markdown(f"### {name}")
        st.write(f"- R² Score: {r2:.3f}")
        st.write(f"- MAE: {mae:.3f}")
        st.write(f"- MSE: {mse:.3f}")

        fig = px.scatter(x=y_test, y=y_pred, labels={"x": "Actual Salary", "y": "Predicted Salary"})
        fig.update_layout(title=f"Actual vs Predicted - {name}")
        st.plotly_chart(fig, use_container_width=True)

    # Correlation heatmap
    st.subheader("Correlation Heatmap")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

    # Feature importance for tree-based models
    if "Random Forest" in model_choices:
        importances = models["Random Forest"].feature_importances_
        feat_imp = pd.Series(importances, index=X.columns).sort_values(ascending=False)
        st.subheader("Feature Importance - Random Forest")
        fig = px.bar(feat_imp, title="Feature Importance", labels={'value': 'Importance', 'index': 'Features'})
        st.plotly_chart(fig, use_container_width=True)

else:
    st.info("👈 Upload a CSV file to get started.")
