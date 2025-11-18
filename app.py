import streamlit as st
from utils import load_data

st.set_page_config(page_title="Spotify Dashboard", layout="wide")

st.title("🎵 Dashboard das 30.000 músicas do Spotify")

st.markdown("""
## 📌 Objetivo do Dashboard
Explorar um conjunto de 30.000 músicas do Spotify, analisando:
- Popularidade
- Atributos de áudio (danceability, energy, valence…)
- Tempo musical (BPM)
- Duração
- Correlações

Use o menu lateral para navegar entre as páginas.
""")

df = load_data()

st.subheader("Amostra dos dados")
st.dataframe(df.head(10))
