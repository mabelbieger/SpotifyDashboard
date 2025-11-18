import streamlit as st
import plotly.express as px
from utils import load_data

st.title("📊 Visão Geral")

df = load_data()

pop_range = st.sidebar.slider("Popularidade", 0, 100, (0, 100))

filtered = df[(df["track_popularity"] >= pop_range[0]) &
              (df["track_popularity"] <= pop_range[1])]

st.metric("Total de músicas filtradas", len(filtered))
st.metric("Popularidade média", round(filtered["track_popularity"].mean(), 2))

fig = px.histogram(filtered, x="track_popularity", title="Distribuição da popularidade")
st.plotly_chart(fig, use_container_width=True)

top10 = filtered.sort_values("track_popularity", ascending=False).head(10)
st.subheader("Top 10 músicas mais populares")
st.dataframe(top10[["track_name", "track_artist", "track_popularity"]])
