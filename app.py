import streamlit as st
import joblib
import pandas as pd
import os
import requests
import matplotlib.pyplot as plt
from datetime import datetime

# Page Settings
st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="wide"
)

# Load Model
model = joblib.load("DATA/Model/house_model.pkl")

# Load Dataset
data = pd.read_csv("DATA/housing.csv")

# Title
st.title("🏠 House Price Predictor")
st.markdown("### Predict House Prices using Machine Learning 🤖")

# Sidebar
st.sidebar.title("🏡 House Price Predictor")

st.sidebar.markdown("---")

st.sidebar.metric(
    "Houses",
    len(data)
)

st.sidebar.metric(
    "Avg Price",
    f"${data['price_usd'].mean():,.0f}"
)

st.sidebar.metric(
    "Max Price",
    f"${data['price_usd'].max():,.0f}"
)

st.sidebar.markdown("---")

st.sidebar.success("Live Currency API")

st.sidebar.success("Location Analysis")

st.sidebar.success("Prediction History")

st.sidebar.success("Data Visualization")

st.sidebar.caption(
    "Developed by Mohit bansal"
)

# Input Section
st.subheader("🏡 Enter House Details")

col1, col2 = st.columns(2)

with col1:
    area = st.number_input("Area (sq ft)", min_value=500)
    bedrooms = st.number_input("Bedrooms", min_value=1)
    bathrooms = st.number_input("Bathrooms", min_value=1)
    floors = st.number_input("Floors", min_value=1)
    age_years = st.number_input("House Age (Years)", min_value=0)

with col2:
    living_area = st.number_input("Living Area (sq ft)", min_value=100)
    kitchen_area = st.number_input("Kitchen Area (sq ft)", min_value=50)
    dining_area = st.number_input("Dining Area (sq ft)", min_value=50)
    garage_area = st.number_input("Garage Area (sq ft)", min_value=0)
    balcony_area = st.number_input("Balcony Area (sq ft)", min_value=0)

location = st.selectbox(
    "🌍 Location",
    sorted(data["location"].unique())
)

property_type = st.selectbox(
    "🏠 Property Type",
    sorted(data["property_type"].unique())
)
st.divider()

# Prediction Button
if st.button("🚀 Predict House Price"):
    prediction_data = pd.DataFrame({
        "area_sqft": [area],
        "bedrooms": [bedrooms],
        "bathrooms": [bathrooms],
        "living_area_sqft": [living_area],
        "kitchen_area_sqft": [kitchen_area],
        "dining_area_sqft": [dining_area],
        "garage_area_sqft": [garage_area],
        "balcony_area_sqft": [balcony_area],
        "floors": [floors],
        "age_years": [age_years],
        "location": [location],
        "property_type": [property_type]
    })

    prediction = model.predict(prediction_data)

    st.session_state["prediction"] = prediction[0]

    st.balloons()

    st.success(
        f"Predicted House Price: ${prediction[0]:,.2f}"
    )

    st.metric(
        label="Estimated House Price",
        value=f"${prediction[0]:,.2f}"
    )

# Currency Converter
if "prediction" in st.session_state:

    currency = st.selectbox(
        "💱 Select Currency",
        [
            "USD","INR","EUR","GBP","JPY","AUD","CAD","CHF","CNY","HKD",
            "SGD","NZD","SEK","NOK","DKK","RUB","ZAR","BRL","MXN","AED",
            "SAR","QAR","KWD","BHD","OMR","TRY","KRW","THB","MYR","IDR",
            "PHP","VND","PKR","BDT","LKR","NPR","EGP","NGN","KES","GHS"
        ]
    )

    try:
        response = requests.get(
            "https://open.er-api.com/v6/latest/USD",
            timeout=5
        )

        exchange_data = response.json()

        rate = exchange_data["rates"][currency]

        converted_price = (
            st.session_state["prediction"] * rate
        )

        st.metric(
            "💰 Converted Price",
            f"{converted_price:,.2f} {currency}"
        )

    except Exception:
        st.error("Error fetching exchange rates.")


#Prediction History
    history = pd.DataFrame({
        "area_sqft": [area],
        "bedrooms": [bedrooms],
        "bathrooms": [bathrooms],
        "living_area_sqft": [living_area],
        "kitchen_area_sqft": [kitchen_area],
        "dining_area_sqft": [dining_area],
        "garage_area_sqft": [garage_area],
        "balcony_area_sqft": [balcony_area],
        "floors": [floors],
        "age_years": [age_years],
        "location": [location],
        "property_type": [property_type],
        "timestamp": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
    })

    history.to_csv(
        "prediction_history.csv",
        mode="a",
        header=not os.path.exists("prediction_history.csv"),
        index=False
    )

# Area Filter
st.subheader("🔍 Area Filter")

min_area = int(data["area_sqft"].min())
max_area = int(data["area_sqft"].max())

selected_area = st.slider(
    "Select Area Range (sq ft)",
    min_area,
    max_area,
    (min_area, max_area)
)

filtered_data = data[
    (data["area_sqft"] >= selected_area[0]) &
    (data["area_sqft"] <= selected_area[1])
]

st.dataframe(filtered_data)

st.divider()

# Bedroom Filter
st.subheader("🛏 Filter by Bedrooms")

bedroom_filter = st.selectbox(
    "Select Bedrooms",
    sorted(data["bedrooms"].unique())
)

bedroom_data = data[
    data["bedrooms"] == bedroom_filter
]

st.dataframe(bedroom_data)

st.divider()

# Prediction History
st.subheader("📜 Prediction History")

if os.path.exists("prediction_history.csv"):
    history_df = pd.read_csv("prediction_history.csv")

    st.dataframe(history_df)

    csv = history_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Prediction History",
        data=csv,
        file_name="prediction_history.csv",
        mime="text/csv"
    )

st.divider()

# Price Distribution Graph
st.subheader("📊 House Price Distribution")

fig, ax = plt.subplots()

ax.hist(data["price_usd"], bins=10)

ax.set_xlabel("Price (USD)")
ax.set_ylabel("Number of Houses")
ax.set_title("House Price Distribution")

st.pyplot(fig)

st.divider()

# Area vs Price Graph
st.subheader("📈 Area vs Price Analysis")

fig2, ax2 = plt.subplots()

ax2.scatter(
    data["area_sqft"],
    data["price_usd"]
)

ax2.set_xlabel("Area (sq ft)")
ax2.set_ylabel("Price (USD)")
ax2.set_title("Area vs Price")

st.pyplot(fig2)

st.divider()

# Statistics Dashboard
st.subheader("📉 House Statistics Dashboard")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("🏠 Houses", len(data))

with col2:
    st.metric(
        "💰 Avg Price",
        f"${data['price_usd'].mean():,.2f}"
    )

with col3:
    st.metric(
        "📈 Max Price",
        f"${data['price_usd'].max():,.2f}"
    )

with col4:
    st.metric(
        "📉 Min Price",
        f"${data['price_usd'].min():,.2f}"
    )

st.divider()

# Top 5 Expensive Houses
st.subheader("🏆 Top 5 Most Expensive Houses")

top_houses = data.sort_values(
    by="price_usd",
    ascending=False
).head(5)

st.dataframe(top_houses)

st.divider()

# Dataset Preview
st.subheader("🗂 Dataset Preview")

st.dataframe(data.head(10))

st.divider()

# Dataset Statistics
st.subheader("📊 Dataset Statistics")

st.write(data.describe())

st.divider()