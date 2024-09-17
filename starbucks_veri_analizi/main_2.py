import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

tips = sns.load_dataset("tips")
tips_filtered = tips

with st.sidebar:
    st.header("Tips Filter")
    days = st.multiselect("Days:", list(tips["day"].unique()), list(tips["day"].unique()))
    tips_filtered = tips[tips["day"].isin(days)]
    tb_criteria = st.radio("Total Bill Box Plot:", ["sex", "smoker", "day", "time"])

st.subheader(f"Items: {tips_filtered['total_bill'].count()}")
st.dataframe(tips_filtered, use_container_width=True)

col1, col2 = st.columns(2, gap="medium")
with col1:
    st.subheader("Statistics:")
    st.dataframe(tips_filtered.describe(), use_container_width=True)
    st.subheader("Correlation:")
    st.dataframe(tips_filtered[["total_bill", "tip", "size"]].corr(), use_container_width=True)

with col2:
    fig, ax = plt.subplots()
    sns.heatmap(tips_filtered[["total_bill", "tip", "size"]].corr(), fmt=".2f", annot=True, ax=ax, cmap="coolwarm")
    st.pyplot(fig)

    fig, ax = plt.subplots()
    sns.boxplot(y="total_bill", hue=tb_criteria, data=tips_filtered, ax=ax)
    st.pyplot(fig)
