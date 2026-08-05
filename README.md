# Análise de Indicadores Econômicos e Mercado Financeiro Brasileiro

Projeto de análise exploratória de dados focado em indicadores macroeconômicos e mercado financeiro do Brasil.

**Objetivo:** Unir conhecimento de Economia com técnicas de Data Science para gerar insights sobre a relação entre variáveis macroeconômicas e o mercado de ações.

---

## Indicadores analisados

| Indicador | Fonte | Descrição |
|---------|-------|---------|
| **IPCA** | Banco Central / Sidra IBGE | Inflação oficial do Brasil |
| **Selic** | Banco Central | Taxa básica de juros |
| **Câmbio (USD/BRL)** | Banco Central | Taxa de câmbio |
| **Ibovespa** | Yahoo Finance | Principal índice da bolsa brasileira |

---

## O que este projeto demonstra

- Coleta de dados econômicos via APIs públicas
- Limpeza e preparação de séries temporais
- Análise exploratória (EDA)
- Visualizações claras e profissionais
- Análise de correlação entre variáveis macro e mercado
- Geração de insights de negócio/economia

---

## Estrutura do projeto

```
analise-indicadores-economicos-brasil/
├── README.md
├── requirements.txt
├── notebooks/
│   └── 01_analise_indicadores.ipynb
├── src/
│   └── data_loader.py
└── reports/
    └── figures/          # gráficos salvos
```

---

## Como executar

### 1. Clone o repositório
```bash
git clone https://github.com/mayconserzedelo/analise-indicadores-economicos-brasil.git
cd analise-indicadores-economicos-brasil
```

### 2. Crie um ambiente virtual (recomendado)
```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
# ou
venv\Scripts\activate           # Windows
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Execute o notebook
Abra o arquivo `notebooks/01_analise_indicadores.ipynb` no Jupyter ou VS Code.

---

## Principais bibliotecas utilizadas

- **pandas** → manipulação de dados
- **numpy** → operações numéricas
- **matplotlib** + **seaborn** → visualização
- **yfinance** → dados do Ibovespa
- **requests** / **bcb** → dados do Banco Central

---

## Insights esperados (exemplos)

- Como a Selic se relaciona com o desempenho do Ibovespa
- Comportamento do câmbio em períodos de alta inflação
- Correlação entre IPCA e taxa de juros
- Momentos de maior volatilidade no mercado brasileiro

---

## Próximos passos (melhorias futuras)

- [ ] Adicionar mais indicadores (PIB, desemprego, balança comercial)
- [ ] Criar dashboard interativo (Streamlit ou Power BI)
- [ ] Modelos simples de previsão (ARIMA / Prophet)
- [ ] Análise de regime (períodos de alta/baixa volatilidade)

---

## Autor

**Maycon Serzedelo**  
Economista em transição para Data Science | Foco em FinTech e análise quantitativa  

- LinkedIn: [linkedin.com/in/maycon-serzedelo-854972215](https://www.linkedin.com/in/maycon-serzedelo-854972215/)
- GitHub: [github.com/mayconserzedelo](https://github.com/mayconserzedelo)

---

## Licença

Este projeto é de uso educacional e de portfólio.
