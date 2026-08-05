"""
Módulo para carregar dados econômicos e financeiros.
Fontes: Banco Central do Brasil e Yahoo Finance.
"""

import pandas as pd
import yfinance as yf
from bcb import sgs
from datetime import datetime, timedelta


def get_bcb_series(codigo: int, nome: str, data_inicio: str = "2015-01-01") -> pd.Series:
    """
    Busca série temporal do Banco Central (SGS).
    
    Parâmetros:
    -----------
    codigo : int
        Código da série no SGS (ex: 433 = IPCA, 432 = Selic)
    nome : str
        Nome que a série receberá
    data_inicio : str
        Data inicial no formato YYYY-MM-DD
    """
    serie = sgs.get(codigo, start=data_inicio)
    serie.name = nome
    return serie


def get_ibovespa(data_inicio: str = "2015-01-01") -> pd.Series:
    """
    Busca dados históricos do Ibovespa via Yahoo Finance.
    """
    ticker = yf.Ticker("^BVSP")
    df = ticker.history(start=data_inicio)
    serie = df["Close"]
    serie.name = "Ibovespa"
    # Remove timezone para facilitar merges
    serie.index = serie.index.tz_localize(None)
    return serie


def carregar_dados(data_inicio: str = "2015-01-01") -> pd.DataFrame:
    """
    Carrega e junta os principais indicadores em um único DataFrame.
    
    Retorna:
    --------
    pd.DataFrame com colunas: IPCA, Selic, Cambio, Ibovespa
    """
    print("Baixando dados do Banco Central...")
    ipca = get_bcb_series(433, "IPCA", data_inicio)          # IPCA mensal
    selic = get_bcb_series(432, "Selic", data_inicio)        # Selic meta
    cambio = get_bcb_series(1, "Cambio_USD_BRL", data_inicio)  # Dólar comercial

    print("Baixando dados do Ibovespa...")
    ibov = get_ibovespa(data_inicio)

    # Junta tudo
    df = pd.concat([ipca, selic, cambio, ibov], axis=1)

    # Como IPCA é mensal, fazemos forward fill para alinhar com dados diários
    df = df.ffill()

    # Remove linhas sem Ibovespa (finais de semana/feriados)
    df = df.dropna(subset=["Ibovespa"])

    print(f"Dados carregados: {df.shape[0]} linhas | {df.shape[1]} colunas")
    print(f"Período: {df.index.min().date()} até {df.index.max().date()}")
    
    return df


if __name__ == "__main__":
    # Teste rápido
    dados = carregar_dados("2020-01-01")
    print("\nPrimeiras linhas:")
    print(dados.head())
    print("\nInformações:")
    print(dados.info())
