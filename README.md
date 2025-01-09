# 📆 dcalendario
**dcalendario** é uma biblioteca Python que cria uma tabela de calendário detalhada para análises de dados, incluindo informações úteis como ano, mês, trimestre, semana, entre outras. Essa tabela pode ser usada em projetos de ciência de dados, business intelligence (BI), e aplicações que necessitam de cálculos baseados em datas.

## ✨ Instalação
Instale a biblioteca diretamente do PyPI usando o pip:
```
pip install dcalendario
```

## 🚀 Funcionalidade
A biblioteca gera um DataFrame pandas com uma tabela de calendário detalhada, baseada em um intervalo de datas fornecido pelo usuário.

### Principais Recursos:
- Geração automática de datas entre o início e o fim do intervalo.
- Adiciona colunas com informações úteis:
- Ano, mês, nome do mês, trimestre, semestre, semana, entre outras.
- Identifica se a data pertence ao ano/mês atual.
- Indica se a data é no passado (comparando com a maior data do intervalo).
