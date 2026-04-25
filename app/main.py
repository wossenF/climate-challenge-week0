import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from utils import load_data, preprocess

st.set_page_config(page_title="Climate Dashboard", layout="wide")

st.title("🌍 African Climate Dashboard")

# Load data
df = load_data()
df = preprocess(df)

# Sidebar filters
st.sidebar.header("Filters")

countries = st.sidebar.multiselect(
    "Select Countries",
    options=df["Country"].unique(),
    default=df["Country"].unique()
)

year_range = st.sidebar.slider(
    "Select Year Range",
    int(df["YEAR"].min()),
    int(df["YEAR"].max()),
    (2015, 2026)
)

variable = st.sidebar.selectbox(
    "Select Variable",
    ["T2M", "PRECTOTCORR", "RH2M"]
)

# Filter data
filtered_df = df[
    (df["Country"].isin(countries)) &
    (df["YEAR"].between(year_range[0], year_range[1]))
]

# -----------------------------
# 📈 Temperature Trend
# -----------------------------
st.subheader("📈 Temperature Trend")

monthly = filtered_df.groupby(["Country", "YEAR", "Month"])[variable].mean().reset_index()

fig1, ax1 = plt.subplots(figsize=(10,5))
sns.lineplot(data=monthly, x="YEAR", y=variable, hue="Country", ax=ax1)
ax1.set_title(f"{variable} Trend Over Time")

st.pyplot(fig1)

# -----------------------------
# 📊 Precipitation Distribution
# -----------------------------
st.subheader("📊 Precipitation Distribution")

fig2, ax2 = plt.subplots(figsize=(10,5))
sns.boxplot(data=filtered_df, x="Country", y="PRECTOTCORR", ax=ax2)

st.pyplot(fig2)