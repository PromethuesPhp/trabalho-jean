# App de Finanças Pessoais

Programa de linha de comando para controle financeiro pessoal desenvolvido em Python.
Permite registrar receitas e despesas, visualizar extratos, gerar relatórios por categoria
e exportar um resumo em arquivo de texto. Os dados são salvos automaticamente a cada registro.

## Como rodar

```bash
python financas.py
```

## Funcionalidades

- **Opção 1 - Registrar:** cadastra um novo lançamento informando tipo (receita ou despesa), valor, categoria e descrição. Valida cada entrada antes de aceitar.
- **Opção 2 - Ver extrato:** lista todos os lançamentos registrados com data, tipo, categoria e valor formatado.
- **Opção 3 - Relatório:** exibe o saldo atual, total de receitas, total de despesas e os valores agrupados por categoria.
- **Opção 4 - Exportar:** gera o arquivo `relatorio.txt` com o resumo completo do relatório.
- **Opção 5 - Sair:** encerra o programa. Nenhum dado é perdido pois o histórico é salvo a cada registro.

## Funções implementadas

| Função | Responsabilidade |
|--------|-----------------|
| `carregar_historico()` | Lê o arquivo JSON do disco e retorna o histórico de lançamentos. Se o arquivo não existir, retorna uma lista vazia. |
| `salvar_historico()` | Grava a lista de lançamentos atualizada no arquivo JSON após cada novo registro. |
| `registrar()` | Coleta e valida os dados do usuário (tipo, valor, categoria, descrição) e adiciona o lançamento ao histórico. |
| `ver_extrato()` | Percorre a lista de lançamentos e exibe cada um formatado no terminal. |
| `calcular_relatorio()` | Soma receitas, despesas e agrupa os valores por categoria, retornando os totais calculados. |
| `exibir_relatorio()` | Exibe no terminal o saldo, totais e os valores por categoria usando os dados calculados. |
| `exportar_relatorio()` | Gera o arquivo `relatorio.txt` com o resumo financeiro completo. |

## Tecnologias usadas

Python 3 · json · os · datetime

## O que aprendi
Se eu fizesse de novo, acho que primeiro planejaria a estrutura das funções no papel antes de escrever qualquer código.
Isso evitaria o retrabalho que tive; seria mais fácil se eu já tivesse uma ideia clara de como o código ficaria e do que seria necessário,
sem perder tempo reestruturando-o depois. Aprendi que tenho que fica mais tempo com a cabeça baixa no código e que nao importa quanto tempo passe,
eu sempre escrevo input com M.

