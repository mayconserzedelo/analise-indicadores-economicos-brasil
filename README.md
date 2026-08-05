# Análise de Indicadores Econômicos e Mercado Financeiro Brasileiro

Projeto de análise exploratória de dados focado em indicadores macroeconômicos e mercado financeiro do Brasil.

**Objetivo:** Unir conhecimento de Economia com técnicas de Data Science para gerar insights sobre a relação entre variáveis macroeconômicas e o mercado de ações.

---

## Indicadores analisados

| Indicador | Código SGS | Descrição |
|---------|------------|---------|
| **IPCA** | 433 | Inflação oficial (IBGE) |
| **IGP-M** | 189 | Índice Geral de Preços do Mercado |
| **Selic** | 432 | Taxa básica de juros (meta) |
| **Câmbio USD/BRL** | 1 | Taxa de câmbio comercial |
| **IBC-Br** | 24363 | Índice de Atividade Econômica do BC |
| **PIB** | 4380 | PIB mensal (valores correntes) |
| **Produção Industrial** | 21859 | Produção Industrial Mensal (PIM-PF) |
| **Vendas no Varejo** | 1455 | Volume de vendas no varejo (PMC) |
| **Desemprego** | 24369 | Taxa de desemprego (PNAD) |
| **Crédito Total** | 20631 | Saldo de crédito do sistema financeiro |
| **Reservas Internacionais** | 3546 | Reservas em US$ milhões |
| **Ibovespa** | Yahoo Finance | Principal índice da bolsa brasileira |

---

## O que este projeto demonstra

- Coleta de dados econômicos via APIs públicas (Banco Central + Yahoo Finance)
- Limpeza e preparação de séries temporais com frequências diferentes
- Análise exploratória (EDA) completa
- Visualizações claras e profissionais
- Análise de correlação entre variáveis macro e mercado
- Geração de insights econômicos e de negócio

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
├── data/
└── reports/
    └── figures/
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

- **pandas** + **numpy** → manipulação de dados
- **matplotlib** + **seaborn** → visualização
- **yfinance** → dados do Ibovespa
- **python-bcb** → dados do Banco Central (SGS)

---

## Insights que você pode explorar

- Relação entre Selic e desempenho do Ibovespa
- Comportamento do câmbio em períodos de alta inflação
- Correlação entre atividade econômica (IBC-Br / PIB / Produção Industrial) e bolsa
- Impacto do desemprego, crédito e vendas no varejo no mercado
- Evolução das reservas internacionais e percepção de risco

---

## Próximos passos (melhorias futuras)

- [ ] Criar dashboard interativo com Streamlit
- [ ] Modelos simples de previsão (ARIMA / Prophet)
- [ ] Análise de regimes (alta/baixa volatilidade)
- [ ] Comparação com outros mercados emergentes
- [ ] Adicionar variáveis de surpresa (realizado vs expectativa)

---

## Autor

**Maycon Serzedelo**  
Economista em transição para Data Science | Foco em FinTech e análise quantitativa

- LinkedIn: [linkedin.com/in/maycon-serzedelo-854972215](https://www.linkedin.com/in/maycon-serzedelo-854972215/)
- GitHub: [github.com/mayconserzedelo](https://github.com/mayconserzedelo)

---

## Licença

Projeto educacional e de portfólio.
