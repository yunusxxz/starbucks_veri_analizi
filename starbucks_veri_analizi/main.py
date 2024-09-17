import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")
df = pd.read_csv("starbucks.csv")

df_filtered = df
with st.sidebar:
    st.subheader("Data Filter")
    nTypes = ["All"] + list(df["type"].unique())
    nType = st.radio("Type:", nTypes)
    if nType != "All":
        df_filtered = df[df["type"] == nType]

    cal_min, cal_max = st.slider(
        "Calories Range:",
        min(df["calories"]),
        max(df["calories"]),
        (min(df["calories"]), max(df["calories"])),
        step=1
    )

    cal_filter = (df_filtered["calories"] >= cal_min) & (df_filtered["calories"] <= cal_max )
    df_filtered = df_filtered[cal_filter]



st.subheader(f"Data Count: {df_filtered.count()['item']}")
print(df_filtered.count()['item'])

print(df.columns)
st.dataframe(df_filtered, use_container_width=True)
