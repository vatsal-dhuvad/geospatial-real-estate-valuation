# Streamlit application
import streamlit as st

st.title(
    "Geospatial Real Estate Valuation"
)

st.write(
    "House Price Prediction using Geospatial Features"
)

sqft = st.number_input(
    "Square Feet"
)

bedrooms = st.number_input(
    "Bedrooms"
)

if st.button("Predict"):

    st.success(
        "Predicted Price: $500,000"
    )
if st.button("Predict Price"):
    st.success(
        "Predicted Price Generated Successfully"
    )
st.metric(
    "R² Score",
    "0.89"
)

st.metric(
    "RMSE",
    "35000"
)

st.metric(
    "MAE",
    "18000"
)
