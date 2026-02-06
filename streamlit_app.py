# app.py
import streamlit as st
from pathlib import Path

# --- Configuração da página ---
st.set_page_config(
    page_title="Erik Marta Garcia | Portfólio",
    page_icon="🚀",
    layout="wide",
)

# --- Carregar CSS ---
def load_css():
    css_path = Path("styles/style.css")
    if css_path.exists():
        with open(css_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# --- Hero Section ---
st.markdown("""
<section class="hero">
    <h1>Erik Marta Garcia</h1>
    <h2>Engenheiro de Machine Learning | Cientista de Dados</h2>
    <p>Transformo dados em modelos escaláveis, prontos para produção e orientados a impacto no negócio.</p>
    <div class="cta">
        <a href="#projetos">Ver Projetos</a>
        <a href="https://linkedin.com" target="_blank">LinkedIn</a>
        <a href="https://github.com" target="_blank">GitHub</a>
    </div>
</section>
""", unsafe_allow_html=True)

# --- Sobre Mim ---
st.markdown("""
<section class="section">
    <h3>Sobre Mim</h3>
    <p>
        Atuo com Machine Learning e Ciência de Dados em projetos end-to-end,
        desde a exploração e tratamento dos dados até a entrega de modelos
        prontos para produção, seguindo boas práticas de engenharia.
    </p>
</section>
""", unsafe_allow_html=True)

# --- Tech Stack ---
st.markdown("""
<section class="section">
    <h3>Stack Técnica</h3>
    <ul class="stack">
        <li><strong>Linguagens:</strong> Python, SQL</li>
        <li><strong>Machine Learning:</strong> Scikit-learn, XGBoost, LightGBM</li>
        <li><strong>Dados:</strong> Pandas, NumPy</li>
        <li><strong>Deploy:</strong> Streamlit, FastAPI</li>
        <li><strong>Infra:</strong> Git, Docker (básico)</li>
    </ul>
</section>
""", unsafe_allow_html=True)

# --- Projetos ---
st.markdown("""
<section class="section" id="projetos">
    <h3>Projetos em Destaque</h3>
    <div class="projects">
        <div class="card">
            <h4>Previsão de Churn</h4>
            <p>Modelo de classificação com XGBoost focado em retenção de clientes.</p>
            <span>ROC-AUC: 0.87</span>
            <div class="links">
                <a href="#">GitHub</a>
                <a href="#">Demo</a>
            </div>
        </div>
        <div class="card">
            <h4>Análise de Crédito</h4>
            <p>Pipeline completo de dados com foco em risco de crédito.</p>
            <span>F1-Score: 0.81</span>
            <div class="links">
                <a href="#">GitHub</a>
            </div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# --- Contato ---
st.markdown("""
<section class="section footer">
    <h3>Contato</h3>
    <p>Aberto a oportunidades e projetos desafiadores.</p>
    <p>
        <a href="https://linkedin.com">LinkedIn</a> ·
        <a href="https://github.com">GitHub</a> ·
        <a href="mailto:email@email.com">Email</a>
    </p>
</section>
""", unsafe_allow_html=True)


# ==============================
# styles/style.css
# ==============================

"""
.hero {
    padding: 80px 0;
    text-align: center;
}

.hero h1 {
    font-size: 3rem;
    margin-bottom: 0.5rem;
}

.hero h2 {
    font-weight: 400;
    color: #6b7280;
}

.hero p {
    max-width: 700px;
    margin: 1rem auto;
    font-size: 1.1rem;
}

.cta a {
    margin: 0 10px;
    padding: 10px 18px;
    border-radius: 8px;
    text-decoration: none;
    background: #2563eb;
    color: white;
}

.section {
    padding: 60px 0;
    max-width: 900px;
    margin: auto;
}

.stack li {
    margin-bottom: 8px;
}

.projects {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 20px;
}

.card {
    padding: 20px;
    border-radius: 12px;
    background: #111827;
}

.card h4 {
    margin-bottom: 8px;
}

.card span {
    font-size: 0.9rem;
    color: #9ca3af;
}

.links a {
    margin-right: 12px;
    text-decoration: none;
    color: #3b82f6;
}

.footer {
    text-align: center;
    color: #9ca3af;
}
"""