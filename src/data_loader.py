"""
Módulo para carregar dados econômicos e financeiros.
Fontes: Banco Central do Brasil (SGS) e Yahoo Finance.
"""

import pandas as pd
import yfinance as yf
from bcb import sgs


def get_bcb_series(codigo: int, nome: str, data_inicio: str = "2015-01-01"):
    """Busca série do Banco Central com tratamento de erro."""
    try:
        serie = sgs.get(codigo, start=data_inicio)
        if serie is None or serie.empty:
            print(f"  [AVISO] {nome} (código {codigo}) veio vazio")
            return None
        serie.name = nome
        print(f"  [OK] {nome}")
        return serie
    except Exception as e:
        print(f"  [ERRO] {nome} (código {codigo}): {e}")
        return None


def get_yahoo_series(ticker: str, nome: str, data_inicio: str = "2015-01-01"):
    """Busca série do Yahoo Finance com tratamento de erro."""
    try:
        dados = yf.Ticker(ticker).history(start=data_inicio)
        if dados.empty:
            print(f"  [AVISO] {nome} ({ticker}) veio vazio")
            return None
        serie = dados["Close"]
        serie.name = nome
        serie.index = serie.index.tz_localize(None)
        print(f"  [OK] {nome}")
        return serie
    except Exception as e:
        print(f"  [ERRO] {nome} ({ticker}): {e}")
        return None


def carregar_dados(data_inicio: str = "2015-01-01") -> pd.DataFrame:
    """
    Carrega indicadores econômicos do Brasil + índices de mercados emergentes.
    Séries que falharem são ignoradas (não quebram o restante).
    """
    print("Baixando dados do Banco Central...")

    series_bcb = [
        (433, "IPCA"),
        (189, "IGP_M"),
        (432, "Selic"),
        (1, "Cambio_USD_BRL"),
        (24363, "IBC_Br"),
        (4380, "PIB"),
        (21859, "Producao_Industrial"),
        (1455, "Vendas_Varejo"),
        (24369, "Desemprego"),
        (20631, "Credito_Total"),
        (3546, "Reservas_Internacionais"),
    ]

    lista = []
    for codigo, nome in series_bcb:
        s = get_bcb_series(codigo, nome, data_inicio)
        if s is not None:
            lista.append(s)

    print("\nBaixando índices de mercados...")
    series_yahoo = [
        ("^BVSP", "Ibovespa"),
        ("^GSPC", "SP500"),
        ("^MXX", "Mexico_IPC"),
        ("^NSEI", "India_Nifty"),
        ("000001.SS", "China_Shanghai"),
    ]

    for ticker, nome in series_yahoo:
        s = get_yahoo_series(ticker, nome, data_inicio)
        if s is not None:
            lista.append(s)

    if not lista:
        raise ValueError("Nenhuma série foi carregada com sucesso.")

    df = pd.concat(lista, axis=1)
    df = df.ffill()

    # Remove linhas totalmente vazias
    df = df.dropna(how="all")

    # Se tiver Ibovespa, remove fins de semana com base nele
    if "Ibovespa" in df.columns:
        df = df.dropna(subset=["Ibovespa"])

    print(f"\nDados carregados com sucesso!")
    print(f"Linhas: {df.shape[0]} | Colunas: {df.shape[1]}")
    print(f"Período: {df.index.min().date()} → {df.index.max().date()}")
    print(f"Indicadores disponíveis: {list(df.columns)}")

    return df


if __name__ == "__main__":
    dados = carregar_dados("2020-01-01")
    print("\n", dados.tail())
