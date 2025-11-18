import streamlit as st
import plotly.express as px
from utils import load_data
import pandas as pd

st.title("🎛️ Atributos de Áudio")

df = load_data()

features = ["danceability", "energy", "speechiness", "acousticness",
            "instrumentalness", "liveness", "valence", "tempo"]

feature = st.sidebar.selectbox("Selecione a feature", features)

fig = px.histogram(df, x=feature, nbins=50,
                   title=f"Distribuição de {feature.capitalize()}")
st.plotly_chart(fig, use_container_width=True)

df["pop_bin"] = pd.cut(df["track_popularity"], bins=5)

fig2 = px.box(df, x="pop_bin", y=feature,
              title=f"{feature.capitalize()} por faixa de popularidade")
st.plotly_chart(fig2, use_container_width=True)
