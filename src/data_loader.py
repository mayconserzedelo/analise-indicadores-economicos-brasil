"""
Módulo para carregar dados econômicos e financeiros.
Fontes: Banco Central do Brasil (SGS) e Yahoo Finance.
"""

import pandas as pd
import yfinance as yf
from bcb import sgs


def get_bcb_series(codigo: int, nome: str, data_inicio: str = "2015-01-01") -> pd.Series:
    """Busca série temporal do Banco Central (SGS)."""
    serie = sgs.get(codigo, start=data_inicio)
    serie.name = nome
    return serie


def get_yahoo_series(ticker: str, nome: str, data_inicio: str = "2015-01-01") -> pd.Series:
    """Busca série de preço de fechamento via Yahoo Finance."""
    dados = yf.Ticker(ticker).history(start=data_inicio)
    serie = dados["Close"]
    serie.name = nome
    serie.index = serie.index.tz_localize(None)
    return serie


def carregar_dados(data_inicio: str = "2015-01-01") -> pd.DataFrame:
    """
    Carrega indicadores econômicos do Brasil + índices de mercados emergentes.
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

    print("Baixando índices de mercados emergentes...")
    ibov = get_yahoo_series("^BVSP", "Ibovespa", data_inicio)
    sp500 = get_yahoo_series("^GSPC", "SP500", data_inicio)           # EUA (referência)
    mexico = get_yahoo_series("^MXX", "Mexico_IPC", data_inicio)       # México
    india = get_yahoo_series("^NSEI", "India_Nifty", data_inicio)      # Índia
    china = get_yahoo_series("000001.SS", "China_Shanghai", data_inicio)  # China
    africa_sul = get_yahoo_series("^JN0U.JO", "Africa_Sul", data_inicio)  # África do Sul (se falhar, tenta outro)

    # Junta tudo
    df = pd.concat(
        [
            ipca, igpm, selic, cambio,
            ibc_br, pib, producao_industrial, vendas_varejo,
            desemprego, credito, reservas,
            ibov, sp500, mexico, india, china,
        ],
        axis=1,
    )

    df = df.ffill()
    df = df.dropna(subset=["Ibovespa"])

    print(f"\nDados carregados com sucesso!")
    print(f"Linhas: {df.shape[0]} | Colunas: {df.shape[1]}")
    print(f"Período: {df.index.min().date()} → {df.index.max().date()}")
    print(f"\nIndicadores: {list(df.columns)}")

    return df


if __name__ == "__main__":
    dados = carregar_dados("2020-01-01")
    print(dados.tail())
