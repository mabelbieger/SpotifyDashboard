import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from utils import load_data

st.title("📈 Correlação entre variáveis")

df = load_data()

numeric_cols = ["track_popularity", "danceability", "energy",
                "loudness", "speechiness", "acousticness",
                "instrumentalness", "liveness", "valence",
                "tempo", "duration_ms"]

corr = df[numeric_cols].corr()

fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)
