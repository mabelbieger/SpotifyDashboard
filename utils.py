import pandas as pd
import streamlit as st

@st.cache_data
def load_data(path="data/spotify_30000.csv"):
    df = pd.read_csv(path)

    # converter duração para minutos
    df["duration_min"] = df["duration_ms"] / 60000

    return df
