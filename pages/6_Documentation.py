import streamlit as st

st.title("📘 Documentação do Dashboard Spotify")

st.markdown("""
## 🎯 Objetivo do Dashboard

O objetivo deste dashboard é analisar dados do Spotify para compreender padrões de **popularidade**, **características de áudio**, **tempo**, **duração** e **correlação entre variáveis musicais**.  
Ele foi desenvolvido utilizando **Streamlit, Plotly e dados extraídos da API do Spotify**.

---

## 🗂️ Como Navegar Entre as Seções

O menu lateral do Streamlit apresenta várias páginas, cada uma com um foco específico:

- **Overview** – Visão geral do dataset, estatísticas iniciais e contexto dos dados.
- **Popularity Analysis** – Gráficos e análises relacionadas à popularidade das músicas.
- **Audio Features** – Visualização de atributos como energy, danceability, valence, etc.
- **Duration & Tempo** – Análise de duração das faixas e variação de BPM.
- **Correlation** – Relações entre diferentes características musicais com heatmaps interativos.

Basta clicar no nome da página desejada no menu lateral para navegar.

---

## 🎚️ Como os Filtros Influenciam os Dados

O dashboard possui filtros que permitem explorar melhor o dataset:

- **Ano**
- **Gênero**
- **Artista**
- **Popularidade mínima**
- **Intervalo de duração**
- **Faixas de tempo (BPM)**

Quando você altera um filtro:
- Os gráficos são atualizados automaticamente.
- A análise é recalculada de acordo com a seleção.
- Somente os dados filtrados são exibidos nas visualizações.

Isso permite comparar artistas, gêneros e períodos diferentes de forma interativa.

---

## ✔️ Conclusão

Esta documentação serve como uma introdução ao funcionamento do dashboard, auxiliando o usuário a entender **o objetivo geral**, **como navegar pelas páginas** e **como interpretar os dados filtrados**.

Explore cada página para entender como os dados musicais se comportam!
""")
