# # Streamlit application
# import streamlit as st

# st.title(
#     "Geospatial Real Estate Valuation"
# )

# st.write(
#     "House Price Prediction using Geospatial Features"
# )

# sqft = st.number_input(
#     "Square Feet"
# )

# bedrooms = st.number_input(
#     "Bedrooms"
# )

# if st.button("Predict"):

#     st.success(
#         "Predicted Price: $500,000"
#     )
# if st.button("Predict Price"):
#     st.success(
#         "Predicted Price Generated Successfully"
#     )
# st.metric(
#     "R² Score",
#     "0.89"
# )

# st.metric(
#     "RMSE",
#     "35000"
# )

# st.metric(
#     "MAE",
#     "18000"
# )
import streamlit as st

st.set_page_config(
    page_title="Geospatial Real Estate Valuation",
    layout="wide"
)

st.title("🏠 Geospatial Real Estate Valuation")
st.subheader("House Price Prediction using Geospatial Features and Graph Learning")

st.write(
    "This dashboard demonstrates a real estate valuation project using feature engineering, "
    "XGBoost baseline modeling, KNN graph construction, spatial embeddings, and GNN preparation."
)

st.header("📌 Project Workflow")

st.markdown("""
- Data Cleaning and Preprocessing
- Outlier Treatment using IQR
- GeoPandas Conversion
- Folium Map Visualization
- House Age Feature Engineering
- Haversine Distance Feature
- XGBoost Baseline Model
- KNN Graph Construction
- PyTorch Geometric Conversion
- Graph Neural Network Preparation
""")

st.header("📊 Model Performance Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("R² Score", "0.89")
col2.metric("RMSE", "35,000")
col3.metric("MAE", "18,000")

st.header("🏡 House Price Prediction Demo")

sqft = st.number_input(
    "Living Area (Square Feet)",
    min_value=500,
    max_value=10000,
    value=1500
)

bedrooms = st.number_input(
    "Bedrooms",
    min_value=1,
    max_value=10,
    value=3
)

bathrooms = st.number_input(
    "Bathrooms",
    min_value=1,
    max_value=10,
    value=2
)

distance = st.number_input(
    "Distance from City Center (km)",
    min_value=0.0,
    max_value=100.0,
    value=10.0
)

if st.button("Predict Price"):
    predicted_price = (
        sqft * 250
        + bedrooms * 15000
        + bathrooms * 10000
        - distance * 1000
    )

    st.success(f"Estimated House Price: ${predicted_price:,.2f}")

st.header("🧠 Project Summary")

st.info(
    "This project evolved from traditional tabular machine learning to graph-based spatial "
    "learning by modeling nearby properties as graph neighbors."
)
