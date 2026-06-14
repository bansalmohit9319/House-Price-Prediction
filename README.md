# 🏠 House Price Prediction System

An advanced Machine Learning-powered web application that predicts residential property prices based on key housing attributes such as area, number of bedrooms, bathrooms, location, property type, and other structural features.

The application provides real-time price estimation, live currency conversion, prediction history tracking, interactive analytics dashboards, and data visualization capabilities through a user-friendly Streamlit interface.

---

## 🚀 Key Features

### 🔹 Machine Learning Prediction

* Predict house prices using a trained Random Forest Regression model.
* Accurate estimation based on multiple housing parameters.

### 🔹 Real-Time Currency Conversion

* Live exchange rates fetched through Currency Exchange API.
* Instantly convert predicted prices into multiple international currencies.

### 🔹 Prediction History Tracking

* Automatically saves user predictions.
* Download prediction history in CSV format.

### 🔹 Interactive Data Analytics

* House price distribution analysis.
* Area vs Price relationship visualization.
* Statistical summary dashboard.

### 🔹 Advanced Filtering

* Filter properties by area range.
* Filter properties by bedroom count.
* Explore housing data interactively.

### 🔹 Modern User Interface

* Responsive Streamlit dashboard.
* Light/Dark theme support.
* Clean and user-friendly design.

---

## 🛠️ Technology Stack

| Category             | Technology   |
| -------------------- | ------------ |
| Programming Language | Python       |
| Machine Learning     | Scikit-Learn |
| Web Framework        | Streamlit    |
| Data Processing      | Pandas       |
| Visualization        | Matplotlib   |
| Model Storage        | Joblib       |
| API Integration      | Requests     |
| Dataset Format       | CSV          |

---

## 📂 Project Structure

```text
House-Price-Prediction/
│
├── app.py
│
├── DATA/
│   ├── housing.csv
│   └── Model/
│       └── house_model.pkl
│
├── prediction_history.csv
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### Clone Repository

```bash
git clone https://github.com/your-username/House-Price-Prediction.git
cd House-Price-Prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 📊 Machine Learning Model

The application utilizes a **Random Forest Regression Model** trained on housing market data to estimate property prices.

### Input Features

* Area (sq ft)
* Bedrooms
* Bathrooms
* Living Area
* Kitchen Area
* Dining Area
* Garage Area
* Balcony Area
* Floors
* House Age
* Location
* Property Type

### Output

* Predicted House Price (USD)
* Real-Time Currency Conversion

---

## 📈 Dashboard Analytics

The dashboard provides:

* House Price Distribution Graph
* Area vs Price Scatter Plot
* Average Property Price
* Maximum Property Price
* Minimum Property Price
* Top 5 Most Expensive Properties

---

## 🔮 Future Enhancements

* Interactive Maps Integration
* AI-Based Property Recommendations
* User Authentication System
* Cloud Database Integration
* Model Retraining Dashboard
* Property Comparison Tool
* Deployment on AWS / Azure / Render

---

## 👨‍💻 Developer

**Mohit Bansal**
