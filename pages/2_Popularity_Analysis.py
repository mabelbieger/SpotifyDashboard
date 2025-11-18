import streamlit as st
import plotly.express as px
from utils import load_data

st.title("⭐ Análise de Popularidade")

df = load_data()

pop_min = st.sidebar.slider("Popularidade mínima", 0, 100, 50)
df_pop = df[df["track_popularity"] >= pop_min]

fig1 = px.scatter(df_pop, x="danceability", y="track_popularity",
                  hover_data=["track_name"],
                  title="Popularidade vs Danceability")
st.plotly_chart(fig1, use_container_width=True)

fig2 = px.scatter(df_pop, x="energy", y="track_popularity",
                  hover_data=["track_name"],
                  title="Popularidade vs Energy")
st.plotly_chart(fig2, use_container_width=True)
