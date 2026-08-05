"""
Dashboard Interativo - Indicadores Econômicos e Mercados Emergentes
Autor: Maycon Serzedelo
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from src.data_loader import carregar_dados

# Configuração da página
st.set_page_config(
    page_title="Indicadores Econômicos Brasil",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Título
st.title("📊 Indicadores Econômicos e Mercados Emergentes")
st.markdown("**Autor:** Maycon Serzedelo | Economista em transição para Data Science")
st.markdown("---")


@st.cache_data(ttl=3600)
def load_data(data_inicio: str):
    """Carrega os dados com cache para não baixar toda hora."""
    return carregar_dados(data_inicio=data_inicio)


# Sidebar
st.sidebar.header("⚙️ Configurações")
data_inicio = st.sidebar.selectbox(
    "Data de início",
    options=["2018-01-01", "2020-01-01", "2022-01-01"],
    index=0,
)

with st.spinner("Carregando dados... Isso pode levar alguns segundos na primeira vez."):
    df = load_data(data_inicio)

st.sidebar.success(f"Dados carregados: {df.shape[0]} linhas")
st.sidebar.markdown(f"Período: **{df.index.min().date()}** → **{df.index.max().date()}**")

# Abas principais
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📈 Indicadores Brasil",
    "🌍 Mercados Emergentes",
    "🔥 Correlações",
    "📉 Regimes de Volatilidade",
    "ℹ️ Sobre",
])

# ============================================================
# TAB 1 - Indicadores do Brasil
# ============================================================
with tab1:
    st.subheader("Indicadores Macroeconômicos do Brasil")

    indicadores_br = {
        "IPCA": "IPCA (Inflação)",
        "IGP_M": "IGP-M",
        "Selic": "Selic (%)",
        "Cambio_USD_BRL": "Câmbio USD/BRL",
        "IBC_Br": "IBC-Br (Atividade)",
        "PIB": "PIB",
        "Producao_Industrial": "Produção Industrial",
        "Vendas_Varejo": "Vendas no Varejo",
        "Desemprego": "Desemprego (%)",
        "Credito_Total": "Crédito Total",
        "Reservas_Internacionais": "Reservas Internacionais",
        "Ibovespa": "Ibovespa",
    }

    # Filtro de indicadores
    opcoes = [v for k, v in indicadores_br.items() if k in df.columns]
    selecionados = st.multiselect(
        "Selecione os indicadores",
        options=opcoes,
        default=["Ibovespa", "Selic (%)", "Câmbio USD/BRL", "IPCA (Inflação)"],
    )

    # Mapeia de volta para o nome da coluna
    col_map = {v: k for k, v in indicadores_br.items()}
    cols_plot = [col_map[s] for s in selecionados if s in col_map]

    if cols_plot:
        # Cria subplots
        n = len(cols_plot)
        fig = make_subplots(
            rows=n,
            cols=1,
            shared_xaxes=True,
            subplot_titles=[indicadores_br[c] for c in cols_plot],
            vertical_spacing=0.04,
        )

        for i, col in enumerate(cols_plot, 1):
            fig.add_trace(
                go.Scatter(x=df.index, y=df[col], name=indicadores_br[col], mode="lines"),
                row=i,
                col=1,
            )

        fig.update_layout(height=250 * n, showlegend=False, title_text="Evolução dos Indicadores")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Selecione pelo menos um indicador.")

# ============================================================
# TAB 2 - Mercados Emergentes
# ============================================================
with tab2:
    st.subheader("Comparação com Mercados Emergentes")

    mercados = ["Ibovespa", "SP500", "Mexico_IPC", "India_Nifty", "China_Shanghai"]
    mercados_ok = [m for m in mercados if m in df.columns]

    if len(mercados_ok) >= 2:
        # Normaliza base 100
        df_norm = df[mercados_ok].dropna(how="all")
        df_norm = df_norm / df_norm.iloc[0] * 100

        fig = px.line(
            df_norm,
            title="Desempenho Comparado (Base 100)",
            labels={"value": "Base 100", "variable": "Índice"},
        )
        fig.update_layout(height=500)
        st.plotly_chart(fig, use_container_width=True)

        # Tabela de performance
        st.markdown("### Performance")
        retornos = df[mercados_ok].pct_change()
        resumo = pd.DataFrame(
            {
                "Retorno Total (%)": (df[mercados_ok].iloc[-1] / df[mercados_ok].iloc[0] - 1) * 100,
                "Volatilidade Anualizada (%)": retornos.std() * np.sqrt(252) * 100,
                "Sharpe (aprox)": (retornos.mean() * 252) / (retornos.std() * np.sqrt(252)),
            }
        ).round(2)
        st.dataframe(resumo.sort_values("Retorno Total (%)", ascending=False), use_container_width=True)
    else:
        st.warning("Dados de mercados emergentes insuficientes.")

# ============================================================
# TAB 3 - Correlações
# ============================================================
with tab3:
    st.subheader("Matrizes de Correlação")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Indicadores do Brasil**")
        cols_br = [
            "IPCA", "Selic", "Cambio_USD_BRL", "IBC_Br", "PIB",
            "Producao_Industrial", "Vendas_Varejo", "Desemprego", "Ibovespa",
        ]
        cols_br = [c for c in cols_br if c in df.columns]
        corr_br = df[cols_br].corr()

        fig1 = px.imshow(
            corr_br,
            text_auto=".2f",
            color_continuous_scale="RdBu_r",
            zmin=-1,
            zmax=1,
            title="Correlação – Brasil",
        )
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        st.markdown("**Mercados**")
        if len(mercados_ok) >= 2:
            corr_mkt = df[mercados_ok].pct_change().corr()
            fig2 = px.imshow(
                corr_mkt,
                text_auto=".2f",
                color_continuous_scale="RdBu_r",
                zmin=-1,
                zmax=1,
                title="Correlação de Retornos – Mercados",
            )
            st.plotly_chart(fig2, use_container_width=True)

# ============================================================
# TAB 4 - Regimes de Volatilidade
# ============================================================
with tab4:
    st.subheader("Regimes de Volatilidade – Ibovespa")

    df_vol = df[["Ibovespa"]].copy()
    df_vol["Retorno"] = df_vol["Ibovespa"].pct_change()
    df_vol["Vol_21d"] = df_vol["Retorno"].rolling(21).std() * np.sqrt(252)
    mediana = df_vol["Vol_21d"].median()
    df_vol["Regime"] = np.where(df_vol["Vol_21d"] > mediana, "Alta Volatilidade", "Baixa Volatilidade")

    st.metric("Mediana da Volatilidade Anualizada", f"{mediana:.2%}")

    # Gráfico de regimes
    fig = go.Figure()

    for regime, cor in [("Baixa Volatilidade", "green"), ("Alta Volatilidade", "red")]:
        mask = df_vol["Regime"] == regime
        fig.add_trace(
            go.Scatter(
                x=df_vol.index[mask],
                y=df_vol["Ibovespa"][mask],
                mode="markers",
                name=regime,
                marker=dict(size=3, color=cor),
            )
        )

    fig.update_layout(title="Ibovespa por Regime de Volatilidade", height=450)
    st.plotly_chart(fig, use_container_width=True)

    # Volatilidade
    fig2 = px.line(df_vol, y="Vol_21d", title="Volatilidade Móvel 21 dias (anualizada)")
    fig2.add_hline(y=mediana, line_dash="dash", line_color="red", annotation_text="Mediana")
    st.plotly_chart(fig2, use_container_width=True)

    # Stats
    st.markdown("### Estatísticas por Regime")
    stats = df_vol.groupby("Regime").agg(
        {"Retorno": ["mean", "std", "count"], "Ibovespa": ["mean", "min", "max"]}
    ).round(4)
    st.dataframe(stats, use_container_width=True)

# ============================================================
# TAB 5 - Sobre
# ============================================================
with tab5:
    st.subheader("Sobre o Projeto")
    st.markdown(
        """
        Este dashboard faz parte do portfólio de **Maycon Serzedelo**.

        ### O que você encontra aqui:
        - 12 indicadores macroeconômicos do Brasil (Banco Central + IBGE)
        - Comparação com mercados emergentes (México, Índia, China + S&P 500)
        - Análise de regimes de volatilidade do Ibovespa
        - Matrizes de correlação

        ### Fontes de dados
        - Banco Central do Brasil (SGS)
        - Yahoo Finance

        ### Tecnologias
        - Python · Pandas · Streamlit · Plotly · python-bcb · yfinance

        ---
        🔗 [GitHub do projeto](https://github.com/mayconserzedelo/analise-indicadores-economicos-brasil)  
        🔗 [LinkedIn](https://www.linkedin.com/in/maycon-serzedelo-854972215/)
        """
    )

st.sidebar.markdown("---")
st.sidebar.caption("Desenvolvido por Maycon Serzedelo")
