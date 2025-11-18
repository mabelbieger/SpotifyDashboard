import streamlit as st
import plotly.express as px
from utils import load_data

st.title("⏱️ Duração vs Tempo")

df = load_data()

dur_range = st.sidebar.slider("Duração da música (min)", 
                              float(df["duration_min"].min()),
                              float(df["duration_min"].max()),
                              (0.0, 5.0))

filtered = df[(df["duration_min"] >= dur_range[0]) &
              (df["duration_min"] <= dur_range[1])]

fig = px.scatter(filtered, x="duration_min", y="tempo",
                 hover_data=["track_name", "track_artist"],
                 title="Duração (min) vs Tempo (BPM)")
st.plotly_chart(fig, use_container_width=True)

fig2 = px.histogram(filtered, x="duration_min",
                    title="Distribuição da duração das músicas")
st.plotly_chart(fig2, use_container_width=True)
