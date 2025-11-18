# 🎵 Dashboard das 30.000 Músicas do Spotify

Este projeto é um **dashboard interativo em Streamlit** que explora um dataset de 30.000 músicas do Spotify, analisando popularidade, atributos de áudio, duração, tempo musical (BPM) e correlações entre variáveis.

---

## 🎯 Objetivo do Projeto

- Visualizar padrões e tendências no dataset
- Facilitar a exploração por meio de gráficos interativos
- Permitir comparações entre atributos de áudio
- Analisar correlações separadamente em múltiplas páginas

---

## 📂 Arquitetura do Projeto

spotify_dashboard/
│── app.py
│── utils.py
│── requirements.txt
│── data/
│ └── spotify_30000.csv
│── pages/
│ ├── 1_Overview.py
│ ├── 2_Popularity_Analysis.py
│ ├── 3_Audio_Features.py
│ ├── 4_Duration_Tempo.py
│ └── 5_Correlation.py
└── README.md


---

## 🚀 Como Executar Localmente

### 1. Instale dependências
pip install -r requirements.txt
streamlit run app.py
