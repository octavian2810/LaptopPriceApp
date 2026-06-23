import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ======= Konfigurasi Halaman ======= setiap buat haalaman baru, harus ada konfigurasi halaman

st.set_page_config(
    page_title="Visualization of Laptop Prices",
    page_icon="📊", 
    layout="wide" #Full width layout for better visualization
)

st.title("📊 Visualization of Laptop Prices")
st.write("This page displays various visualizations from the laptop price dataset.")

# ======= Load Data ======= 

@st.cache_data #Harus pakai cache_data biar data ga di load ulang setiap ada interaksi
def load_data():
    laptop_df = pd.read_csv("data/laptop_prices-selected-columns.csv")
    return laptop_df

laptop_df = load_data()


# ======= Sidebar Filter ======= 

st.sidebar.header("Spesifikasi Laptop")

company = st.sidebar.selectbox(
    "Company",
    sorted(laptop_df["Company"].unique())
)

typename = st.sidebar.selectbox(
    "Type",
    sorted(laptop_df["TypeName"].unique())
)

os = st.sidebar.selectbox(
    "OS",
    sorted(laptop_df["OS"].unique())
)

st.write(f"Showing **{len(laptop_df)} data** from total {len(laptop_df)} data.")

# ======= Visualisasi =======

st.subheader("📈 Distribution of Data")

# Baris pertama: 2 chart
col1, col2 = st.columns(2)

with col1:
    st.write("**Distribution of Price**")
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.hist(laptop_df["Price_euros"], bins=20, color="pink", edgecolor="white")
    ax.set_xlabel("Price")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)
    plt.close(fig)  # penting: tutup figure setelah ditampilkan

with col2:
    st.write("**Distribution of RAM**")
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.hist(laptop_df["Ram"], bins=20, color="purple", edgecolor="white")
    ax.set_xlabel("RAM")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)
    plt.close(fig)

# Baris kedua: 2 chart
col3, col4 = st.columns(2)

with col3:
    st.write("**Distribution of Price by Company**")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.histplot(x="Company", y="Price_euros", data=laptop_df, ax=ax)
    ax.set_xlabel("Company")
    ax.set_ylabel("Price (Euros)")
    st.pyplot(fig)
    plt.close(fig)

with col4:
    st.write("**Distribution of RAM by Company**")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.histplot(x="Company", y="Ram", data=laptop_df, ax=ax)
    ax.set_xlabel("Company")
    ax.set_ylabel("RAM")
    st.pyplot(fig)
    plt.close(fig)

# ======= Tampilkan Dataframe =======

st.subheader("📄 Result Data of Filter")
st.dataframe(laptop_df, use_container_width=True)

st.markdown("""
<div style="
padding:15px;
border-radius:10px;
background-color:#F3E8FF;
border-left:5px solid #A855F7;
">
<b>📂 Dataset Source</b><br>
<a href="https://raw.githubusercontent.com/octavian2810/LaptopPriceApp/main/laptop_prices-selected-columns.csv" target="_blank">
Laptop Prices Dataset (GitHub Repository)
</a>
</div>
""", unsafe_allow_html=True)