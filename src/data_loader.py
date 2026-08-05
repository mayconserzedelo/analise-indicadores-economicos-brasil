"""
Módulo para carregar dados econômicos e financeiros.
Fontes: Banco Central do Brasil (SGS) e Yahoo Finance.
"""

import pandas as pd
import yfinance as yf
from bcb import sgs


def get_bcb_series(codigo: int, nome: str, data_inicio: str = "2015-01-01") -> pd.Series:
    """
    Busca série temporal do Banco Central (SGS).

    Parâmetros
    ----------
    codigo : int
        Código da série no SGS
    nome : str
        Nome que a série receberá no DataFrame
    data_inicio : str
        Data inicial no formato YYYY-MM-DD
    """
    serie = sgs.get(codigo, start=data_inicio)
    serie.name = nome
    return serie


def get_ibovespa(data_inicio: str = "2015-01-01") -> pd.Series:
    """Busca dados históricos do Ibovespa via Yahoo Finance."""
    ticker = yf.Ticker("^BVSP")
    df = ticker.history(start=data_inicio)
    serie = df["Close"]
    serie.name = "Ibovespa"
    serie.index = serie.index.tz_localize(None)
    return serie


def carregar_dados(data_inicio: str = "2015-01-01") -> pd.DataFrame:
    """
    Carrega e junta os principais indicadores econômicos e financeiros.

    Indicadores incluídos:
    ----------------------
    Inflação e preços:
    - IPCA (433)
    - IGP-M (189)

    Juros e câmbio:
    - Selic (432)
    - Câmbio USD/BRL (1)

    Atividade econômica:
    - IBC-Br (24363)              → Proxy mensal de atividade
    - PIB (4380)                  → PIB mensal (valores correntes)
    - Produção Industrial (21859) → PIM-PF
    - Vendas no Varejo (1455)     → Volume de vendas (PMC)

    Mercado de trabalho e crédito:
    - Desemprego (24369)
    - Crédito Total (20631)

    Setor externo:
    - Reservas Internacionais (3546)

    Mercado:
    - Ibovespa (Yahoo Finance)

    Retorna
    -------
    pd.DataFrame com todos os indicadores alinhados temporalmente.
    """
    print("Baixando dados do Banco Central...")

    # Inflação e preços
    ipca = get_bcb_series(433, "IPCA", data_inicio)
    igpm = get_bcb_series(189, "IGP_M", data_inicio)

    # Juros e câmbio
    selic = get_bcb_series(432, "Selic", data_inicio)
    cambio = get_bcb_series(1, "Cambio_USD_BRL", data_inicio)

    # Atividade econômica
    ibc_br = get_bcb_series(24363, "IBC_Br", data_inicio)
    pib = get_bcb_series(4380, "PIB", data_inicio)
    producao_industrial = get_bcb_series(21859, "Producao_Industrial", data_inicio)
    vendas_varejo = get_bcb_series(1455, "Vendas_Varejo", data_inicio)

    # Mercado de trabalho e crédito
    desemprego = get_bcb_series(24369, "Desemprego", data_inicio)
    credito = get_bcb_series(20631, "Credito_Total", data_inicio)

    # Setor externo
    reservas = get_bcb_series(3546, "Reservas_Internacionais", data_inicio)

    print("Baixando dados do Ibovespa...")
    ibov = get_ibovespa(data_inicio)

    # Junta todas as séries
    df = pd.concat(
        [
            ipca,
            igpm,
            selic,
            cambio,
            ibc_br,
            pib,
            producao_industrial,
            vendas_varejo,
            desemprego,
            credito,
            reservas,
            ibov,
        ],
        axis=1,
    )

    # Forward fill para alinhar frequências diferentes (mensal vs diário)
    df = df.ffill()

    # Remove dias sem pregão
    df = df.dropna(subset=["Ibovespa"])

    print(f"\nDados carregados com sucesso!")
    print(f"Linhas: {df.shape[0]} | Colunas: {df.shape[1]}")
    print(f"Período: {df.index.min().date()} → {df.index.max().date()}")
    print(f"\nIndicadores: {list(df.columns)}")

    return df


if __name__ == "__main__":
    dados = carregar_dados("2020-01-01")
    print("\nPrimeiras linhas:")
    print(dados.head())
    print("\nEstatísticas descritivas:")
    print(dados.describe().round(2))
