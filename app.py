import streamlit as st
import pandas as pd
import pickle


st.set_page_config(
    page_title="Laptop Price Prediction App",
    page_icon="💻",
    layout="wide"
)


st.title("💻 Laptop Price Prediction App")
st.write("Welcome! Use the menu on the left sidebar to get started.")
st.write("📊 **Visualization** → View charts and patterns in laptop data.")
st.write("💡 **Prediction** → Predict estimated laptop prices.")

# ==========================
# CUSTOM CSS
# ==========================
st.markdown("""
<style>

.main {
    background-color: #F8F5FF;
}

h1, h2, h3 {
    color: #5E4B8B;
}

.stButton>button {
    background-color: #CDB4DB;
    color: black;
    border-radius: 10px;
    border: none;
    padding: 0.5rem 1rem;
}

.stButton>button:hover {
    background-color: #B8A1D9;
    color: white;
}

.card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    text-align: center;
}

.big-font {
    font-size: 28px;
    font-weight: bold;
    color: #5E4B8B;
}

.small-font {
    font-size: 16px;
    color: #666666;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# ABOUT PROJECT
# ==========================

st.subheader("📌 About This Project")

st.info("""
This application predicts laptop prices based on specifications such as:

- Company
- Product Type
- RAM
- Weight
- Operating System
- Screen Resolution
- Screen Size

The prediction model was built using an Artificial Neural Network (ANN).
""")

# ==========================
# FEATURES
# ==========================

st.subheader("✨ Available Features")

feature1, feature2 = st.columns(2)

with feature1:
    st.success("📈 Visualization Page")
    st.write("""
    - Explore dataset distributions
    - Analyze laptop specifications
    - View charts and trends
    """)

with feature2:
    st.success("💡 Prediction Page")
    st.write("""
    - Input laptop specifications
    - Get estimated laptop price
    - Real-time prediction
    """)

st.divider()

# ==========================
# QUICK START
# ==========================

st.subheader("🚀 Quick Start")

st.markdown("""
1. Open **Visualization** page to explore the dataset.
2. Open **Prediction** page.
3. Enter laptop specifications.
4. Click **Predict Price**.
5. View estimated laptop price instantly.
""")

st.divider()


