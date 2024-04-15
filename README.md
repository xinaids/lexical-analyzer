## Ambiente de desenvolvimento

1. Para criar o ambiente, digite no terminal: ```python -m venv venv```
2. Para ativar o ambiente, digite no terminal: ```source venv/bin/activate```
3. Para instalar as dependências, digite no terminal: ```pip install -r requirements.txt```
4. Para desativar o ambiente, digite no terminal: ```deactivate```

- Caso instale uma nova dependência, digite no terminal: ```pip freeze > requirements.txt```

## Caminho a ser seguido 

1. Separação dos primeiros tokens da string de entrada
2. Verificação no Autômato Finito Determinístico
3. Análise do retorno do Autômato Finito Determinístico
4. Se o retorno é diferente de falso, é analisado se o token está incluso no grupo de palavras reservadas
5. Se existe no grupo de palavras reservadas, salva no array de tokens finais como palavra reservada

Obs.: Funcionando com alguns erros de expressões regulares.