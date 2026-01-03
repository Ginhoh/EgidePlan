# EgidePlan
Sistema de controle e armazenamento de gastos
Descrição
-
EgidePlan é uma aplicação GUI (CustomTkinter) para controle simples de gastos mensais. A interface principal é o arquivo `interface.py`. O programa armazena os gastos em um arquivo Excel chamado `total_de_gastos.xlsx`, criando uma aba para o mês atual quando necessário.

Funcionalidades principais
- Tela Home: apresentação e dicas rápidas.
- Tela Dashboard: mostra total gasto, média por entrada, categorias com maior/menor gasto e comparação com o mês anterior.
- Tela Gastos: lista os registros do mês atual, permite adicionar e remover gastos.
- Tela Contato: links para LinkedIn, GitHub, e-mail e portfólio.

Arquivos relevantes
- `interface.py`: arquivo principal — inicia a janela e controla navegação entre telas.
- `funcoes.py`: funções utilitárias (retorna mês atual, verifica/cria abas na planilha, checa se há apenas uma aba).
- `gastos.py`: leitura/escrita da planilha, exibição da lista de gastos, diálogo para adicionar/remover.
- `dashboard.py`: cálculo de totais, médias, categorias e montagem do dashboard.
- `home_contato.py`: conteúdo das telas Home e Contato.
- `total_de_gastos.xlsx`: arquivo de dados (deve ficar na mesma pasta do projeto). Se não existir, crie uma cópia vazia com esse nome ou o código criará as abas necessárias.
- `assents/`: pasta com recursos (ex.: `logo.ico`).

Dependências
- Python 3.8+ (recomendado)
- Instale as dependências com:

`pip install customtkinter openpyxl pillow`

Como usar
1. Certifique-se de que `total_de_gastos.xlsx` esteja na mesma pasta do projeto (ou deixe que o programa crie as abas do mês).
2. Execute o programa principal:

`python interface.py`

3. Navegue pelo menu lateral:
- `Home`: tela inicial.
- `Dashboard`: métricas e comparações.
- `Gastos`: lista atual, botão `Adicionar Gasto` e `Remover Gasto`.
- `Contato`: links externos.

Adicionar gastos
- Ao adicionar um gasto, preencha `Título do Gasto`, `Valor` e `Categoria`.
- IMPORTANTE: use ponto como separador decimal — por exemplo: `12.50` (não use vírgula). Caso use vírgula, o programa pode lançar um erro ao converter para float.

Remover gastos
- Ao remover, informe o número do registro conforme listado (o índice exibido na lista). O índice corresponde à ordem mostrada (começa em 1 para a primeira entrada depois do cabeçalho).

Observações e dicas
- O programa cria uma aba com o nome do mês atual (em português) se ela não existir.
- Evite manter o arquivo Excel aberto em outro programa enquanto o EgidePlan salva alterações.
- Se ocorrerem erros de conversão de valores, verifique o formato do campo `Valor` (usar ponto) e se há células vazias ou inválidas na coluna B.
- Ícone e imagens são carregados de `assents/logo.ico` — mantenha essa pasta presente.

Suporte e desenvolvimento
- O código é organizado em módulos para facilitar manutenção — edite `gastos.py` e `dashboard.py` para alterar regras de cálculo ou formato de exibição.

Licença
- Consulte o arquivo `LICENSE` no repositório para informações sobre licença.
