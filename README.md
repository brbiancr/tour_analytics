# Tour Analytics

> Status do projeto: Em desenvolvimento
> 

> Este projeto realiza uma análise completa de dados de turnês musicais, respondendo perguntas sobre faturamento, shows, artistas e desempenho financeiro, utilizando Python e bibliotecas de análise de dados.
> 

# 📝 Descrição do Desafio

O desafio consiste em processar um **arquivo de estatísticas da Google Play Store** e gerar **análises gráficas e métricas descritivas**.

As principais etapas incluem:

1. **Limpeza de dados**
    - Tratar informações inconsistentes e preparar variáveis necessárias.
    - Criar colunas derivadas quando necessário (ex: receita por show).
2. **Análises e métricas**
    - Identificar **a artista com mais aparições e maior média de faturamento bruto**.
    - Determinar **a turnê com maior média de faturamento dentro de um único ano**.
    - Listar **as 3 turnês mais lucrativas por show**, considerando valores ajustados para 2022.
    - Gerar gráfico de linha para a artista top mostrando **faturamento por ano**.
    - Exiber **as 5 artistas com maior quantidade de shows** em gráfico de barras.

---

## 🔍 Análise prevista

- Comparação de faturamento entre artistas
- Ranking das turnês mais lucrativas da história
- Evolução anual de receita da artista mais relevante
- Quantidade de shows por artista e sua relação com faturamento

---

## 📊 Tecnologias Utilizadas

| Tecnologia | Finalidade |
| --- | --- |
| Python | Scripts de ingestão, processamento e análise |
| Pandas | Manipulação de limpeza dos dados |
| Jupyter notebook | ambiente de análise |
| Matplotlib | Para criação de gráficos e vizualização |

---

## 🗂 Estrutura do Projeto

```bash
/TourAnalytics                 
 ├── data/                                 # Dados brutos do projeto
 │   └── concert_tours_womans.csv          # Base de dados das turnês
 │   └── processed/                        # Dados limpos
 ├── outputs/
 ├── scripts/                              # Script de limpeza dos dadaos
 └── README.md
```