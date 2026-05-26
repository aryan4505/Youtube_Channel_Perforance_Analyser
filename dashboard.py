import streamlit as st
import pandas as pd

df = pd.read_csv(
    "outputs/reports/channel_analysis.csv"
)

st.title(
    "YouTube Channel Performance Dashboard"
)

st.dataframe(df)

st.bar_chart(df["Views"])