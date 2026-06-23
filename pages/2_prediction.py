import streamlit as st
import pandas as pd
import pickle
import joblib
from pathlib import Path
from tensorflow import keras

# ======= Path =======
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "models"

# ======= Konfigurasi Halaman =======
st.set_page_config(
    page_title="Prediction of Laptop Prices",
    page_icon="💡",
    layout="wide"
)

st.title("💡 Prediction of Laptop Prices")
st.write("Fill in the laptop data to get a price estimate.")

# ======= Load Model & Artifacts =======
@st.cache_resource
def load_model():
    return keras.models.load_model(MODEL_DIR / "ann_model.keras")

@st.cache_resource
def load_artifacts():
    scaler = joblib.load(MODEL_DIR / "scaler.pkl")

    with open(MODEL_DIR / "feature_columns.pkl", "rb") as f:
        feature_columns = pickle.load(f)

    return scaler, feature_columns

model = load_model()
scaler, feature_columns = load_artifacts()

# ======= Form Input =======
st.sidebar.header("📝 Fill the specification of Laptop")

col1, col2 = st.columns(2)

product = col1.text_input("Product:", value="MacBook Pro")

company = col1.selectbox(
    "Company:",
    ['Apple', 'HP', 'Acer', 'Asus', 'Dell', 'Lenovo', 'Chuwi', 'MSI',
     'Microsoft', 'Toshiba', 'Huawei', 'Xiaomi', 'Vero', 'Razer',
     'Mediacom', 'Samsung', 'Google', 'Fujitsu', 'LG']
)

typename = col1.selectbox(
    "Type:",
    ['Ultrabook', 'Notebook', 'Netbook', 'Gaming', '2 in 1 Convertible', 'Workstation']
)

os_name = col1.selectbox(
    "OS:",
    ['macOS', 'No OS', 'Windows 10', 'Mac OS X', 'Linux', 'Android',
     'Windows 10 S', 'Chrome OS', 'Windows 7']
)

screen = col1.selectbox(
    "Screen:",
    ['Standard', 'Full HD', 'Quad HD+', '4K Ultra HD']
)

inches = col2.selectbox(
    "Screen Size:",
    [13.3, 15.6, 15.4, 14.0, 12.0, 11.6, 17.3, 10.1, 13.5, 12.5, 13.0]
)

ram = col2.selectbox(
    "RAM:",
    [2, 4, 6, 8, 12, 16, 24, 32, 64]
)

weight = col2.number_input(
    "Weight:",
    min_value=0.5,
    max_value=5.0,
    value=1.37,
    step=0.01
)

# ======= Tombol Prediksi =======
if st.button("🔮 Predict Now!", use_container_width=True):

    input_data = pd.DataFrame([{
        "Company": company,
        "Product": product,
        "TypeName": typename,
        "OS": os_name,
        "Screen": screen,
        "Inches": inches,
        "Ram": ram,
        "Weight": weight
    }])

    # One Hot Encoding
    input_encoded = pd.get_dummies(input_data)

    # Samakan kolom dengan data training
    input_encoded = input_encoded.reindex(columns=feature_columns, fill_value=0)

    # Scaling
    input_scaled = scaler.transform(input_encoded)

    # Prediction
    prediction = model.predict(input_scaled)[0][0]

    st.divider()
    st.success(f"💰 Estimation of Laptop Price: **€{prediction:,.2f}**")
    st.info("ℹ️ This result is an estimate based on the Artificial Neural Network model, not a definitive amount.")