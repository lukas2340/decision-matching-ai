import streamlit as st
import pandas as pd
import joblib
import os

# Caminhos para os dados e modelo
DATA_DIR = "data"
MODEL_PATH = "model/model.pkl"

# Função para carregar os dados
@st.cache_data
def load_data():
    prospects = pd.read_json(os.path.join(DATA_DIR, "prospects.json"))
    vagas = pd.read_json(os.path.join(DATA_DIR, "vagas.json"))
    return prospects, vagas

# Carregar modelo treinado
@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

# Interface
st.set_page_config(page_title="IA de Recrutamento - Decision", layout="wide")
st.title("🤖 IA para Recrutamento - Decision")

# Carrega dados e modelo
try:
    prospects, vagas = load_data()
    model = load_model()
except Exception as e:
    st.error("Erro ao carregar os dados ou modelo: " + str(e))
    st.stop()

# Lista de vagas disponíveis
vaga_ids = list(prospects.keys())
vaga_id = st.selectbox("Selecione uma vaga:", vaga_ids)

# Mostra candidatos da vaga
st.subheader("Candidatos para a vaga:")
candidatos = pd.DataFrame(prospects[vaga_id]['prospects'])
st.dataframe(candidatos[['nome', 'situacao_candidado', 'comentario']])

# Simulação de previsão de sucesso
st.subheader("Simulação de score (exemplo fixo para demonstração):")
if st.button("Rodar predição para todos os candidatos"):
    import random
    candidatos['score_sucesso (%)'] = [random.randint(50, 99) for _ in range(len(candidatos))]
    st.dataframe(candidatos[['nome', 'situacao_candidado', 'score_sucesso (%)']])

st.info("🔧 Esta versão demonstra interface e dados reais. O modelo real deve ser treinado e integrado via `trai
