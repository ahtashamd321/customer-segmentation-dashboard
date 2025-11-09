# ====================================================
# 🎯 CUSTOMER SEGMENTATION DASHBOARD
# ====================================================

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

st.set_page_config(page_title="Customer Segmentation Dashboard", layout="wide")

# ====================================================
# 🧭 Sidebar
# ====================================================
st.sidebar.title("⚙️ Dashboard Settings")
st.sidebar.markdown("Use this panel to customize your clustering.")

uploaded_file = st.sidebar.file_uploader("Upload CSV Dataset", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅ Dataset Uploaded Successfully!")
else:
    st.info("Please upload your dataset to begin.")
    st.stop()

# ====================================================
# 🧹 Data Cleaning
# ====================================================
st.subheader("📊 Raw Data Preview")
st.dataframe(df.head())

# Drop CustomerID if present
if 'CustomerID' in df.columns:
    df.drop('CustomerID', axis=1, inplace=True)

# Clean and convert income column
if 'Annual Income (k$)' in df.columns:
    df['Annual Income (k$)'] = df['Annual Income (k$)'].replace('[^0-9.]', '', regex=True)
    df['Annual Income (k$)'] = pd.to_numeric(df['Annual Income (k$)'], errors='coerce')

# Encode gender
if 'Gender' in df.columns:
    le = LabelEncoder()
    df['Gender'] = le.fit_transform(df['Gender'])

# Fill missing values with median
df.fillna(df.median(numeric_only=True), inplace=True)

# ====================================================
# ⚖️ Feature Scaling
# ====================================================
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df.select_dtypes(include=[np.number]))
df_scaled = pd.DataFrame(scaled_data, columns=df.select_dtypes(include=[np.number]).columns)

# ====================================================
# 🔢 K-Means Clustering
# ====================================================
st.sidebar.subheader("🔹 Choose Number of Clusters (k)")
k = st.sidebar.slider("Select k value", 2, 10, 5)

kmeans = KMeans(n_clusters=k, random_state=42)
df_scaled["Cluster"] = kmeans.fit_predict(df_scaled)

# Add cluster labels to original dataframe
df["Cluster"] = df_scaled["Cluster"]

# ====================================================
# 📈 PCA for 2D Visualization
# ====================================================
pca = PCA(n_components=2)
pca_result = pca.fit_transform(df_scaled.drop("Cluster", axis=1))
df["PCA1"] = pca_result[:, 0]
df["PCA2"] = pca_result[:, 1]

# ====================================================
# 🖼️ Visualizations
# ====================================================
st.header("🧠 Customer Segmentation Results")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📍 Cluster Distribution")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.countplot(x='Cluster', data=df, palette='Set2', ax=ax)
    st.pyplot(fig)

with col2:
    st.subheader("💡 Cluster Scatter (PCA Projection)")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.scatterplot(x='PCA1', y='PCA2', hue='Cluster', palette='Set2', data=df, s=50, ax=ax)
    st.pyplot(fig)

# ====================================================
# 📊 Cluster Insights
# ====================================================
st.subheader("📈 Cluster Summary Statistics")
summary = df.groupby('Cluster').mean().round(2)
st.dataframe(summary)

# ====================================================
# 💾 Downloadable Results
# ====================================================
csv = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="⬇️ Download Clustered Data (CSV)",
    data=csv,
    file_name='clustered_customers.csv',
    mime='text/csv',
)

st.success("✅ Clustering Completed Successfully! Explore results above.")
