# Análise de Indicadores Econômicos e Mercado Financeiro Brasileiro

Projeto completo de análise exploratória + comparação internacional + regimes de volatilidade + previsão + **dashboard interativo com Streamlit**.

**Autor:** Maycon Serzedelo  
Economista em transição para Data Science | Foco em FinTech e análise quantitativa

---

## 🚀 Dashboard Interativo (Streamlit)

Para rodar o dashboard localmente:

```bash
pip install -r requirements.txt
streamlit run app.py
```

O dashboard possui 5 abas:
1. **Indicadores Brasil** – evolução interativa dos 12 indicadores
2. **Mercados Emergentes** – comparação Ibovespa vs México, Índia, China e S&P 500
3. **Correlações** – matrizes de correlação
4. **Regimes de Volatilidade** – alta vs baixa volatilidade no Ibovespa
5. **Sobre** – informações do projeto

---

## O que o projeto cobre

- 12 indicadores econômicos do Brasil
- Comparação com mercados emergentes
- Análise de regimes de volatilidade
- Modelos de previsão (ARIMA e Prophet) no notebook
- Dashboard interativo com Streamlit + Plotly

---

## Indicadores Brasileiros

| Indicador | Código / Fonte |
|---------|----------------|
| IPCA | 433 |
| IGP-M | 189 |
| Selic | 432 |
| Câmbio USD/BRL | 1 |
| IBC-Br | 24363 |
| PIB | 4380 |
| Produção Industrial | 21859 |
| Vendas no Varejo | 1455 |
| Desemprego | 24369 |
| Crédito Total | 20631 |
| Reservas Internacionais | 3546 |
| Ibovespa | Yahoo Finance |

## Mercados Comparados

- Ibovespa (Brasil)
- S&P 500 (EUA)
- IPC (México)
- Nifty 50 (Índia)
- Shanghai Composite (China)

---

## Como executar o notebook

```bash
git clone https://github.com/mayconserzedelo/analise-indicadores-economicos-brasil.git
cd analise-indicadores-economicos-brasil
pip install -r requirements.txt
```

Abra: `notebooks/01_analise_indicadores.ipynb`

---

## Estrutura

```
├── app.py                          ← Dashboard Streamlit
├── README.md
├── requirements.txt
├── notebooks/01_analise_indicadores.ipynb
├── src/data_loader.py
└── reports/figures/
```

---

## Autor

**Maycon Serzedelo**  
[LinkedIn](https://www.linkedin.com/in/maycon-serzedelo-854972215/) · [GitHub](https://github.com/mayconserzedelo)
