# Análise de Indicadores Econômicos e Mercado Financeiro Brasileiro

Projeto completo de análise exploratória + comparação internacional + regimes de volatilidade + previsão.

**Autor:** Maycon Serzedelo  
Economista em transição para Data Science | Foco em FinTech e análise quantitativa

---

## O que o projeto cobre

1. **12 indicadores econômicos do Brasil** (IPCA, Selic, Câmbio, PIB, Produção Industrial, Varejo, etc.)
2. **Comparação com mercados emergentes** (México, Índia, China + S&P 500 como referência)
3. **Análise de regimes de volatilidade** (alta vs baixa)
4. **Modelos de previsão** (ARIMA e Prophet)
5. Correlações e insights macroeconômicos

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

## Como executar

```bash
git clone https://github.com/mayconserzedelo/analise-indicadores-economicos-brasil.git
cd analise-indicadores-economicos-brasil
pip install -r requirements.txt
```

Depois abra o notebook:
`notebooks/01_analise_indicadores.ipynb`

---

## Estrutura

```
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
