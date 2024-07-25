## Como executar em distribuições Ubuntu

1. Execute o comando ```git clone https://github.com/fco3lho/lexical-analyzer.git```
2. Entre na pasta com o comando ```cd lexical-analyzer```
3. Execute o código com o comando ```python3 main.py```

## Passo-a-passo do código

1. Leitura do arquivo .txt para salvar o código em uma string com a função abaixo:

```python
  def save_string():
    with open('data.txt', 'r') as file:
      string = file.read()
      return string
  
  string = save_string()
```
2. Separação da string do código em tokens com a função descrita abaixo:

```python
  def token_separation(string):
    global separate_string_input
    temp = ''
    quote_counter = 0

    for char in string:
      if re.match(r'[^a-zA-Z0-9\s."]', char):
        separate_string_input.append(temp)
        separate_string_input.append(char)
        temp = ''
      elif temp == '' and char == '"' and quote_counter == 0:
        temp += char
        quote_counter = 1      
      elif char == string[len(string)-1]:
        temp += char
        separate_string_input.append(temp)
        temp = ''
      elif char == '"' and quote_counter == 1:
        temp += char
        separate_string_input.append(temp)
        temp = ''
        quote_counter = 0
      elif quote_counter == 1:
        temp += char
      elif char.isspace() == False:
        temp += char
      else:
        separate_string_input.append(temp)
        temp = ''

    separate_string_input = [item for item in separate_string_input if item]
  
  token_separation(string)
```

3. Entra em um loop que percorre todos tokens salvos, onde é verificado se o token é valido para o AFD usado, e se for válido, é verificado se o token é uma palavra reservada, uma variável, um número inteiro, um número decimal ou um texto, se não for válido, é retornado um erro da análise léxica: 

```python
  for word in separate_string_input:
    if returnNextState(word) != False:
      if word in reserved_words:
        tokens.append(reserved_words[word])
      elif returnNextState(word) == 'ID':
        id.append(word)
        tokens.append("ID_" + str(id.index(word)))
      elif returnNextState(word) == 'NUMINT':
        num_int.append(word)
        tokens.append("NUMINT_" + str(num_int.index(word)))
      elif returnNextState(word) == 'NUMDEC':
        num_dec.append(word)
        tokens.append("NUMDEC_" + str(num_dec.index(word)))
      elif returnNextState(word) == 'TEXT':
        text.append(word)
        tokens.append("TEXT_" + str(text.index(word)))
      else:
        tokens.append(returnNextState(word))
    else:
      print("\033[1;31mErro na análise léxica\033[0m")
      break
```
- Função ```returnNextState(token)``` usada no loop acima:

```python
  def returnNextState(token):
    state = "q0"

    transitions = {
      ('q0', re.compile(r'^[a-zA-Z]$')): 'q1',
      ('q1', re.compile(r'^[a-zA-Z0-9]$')): 'q1',

      ('q0', re.compile(r'^[0-9]$')): 'q3',
      ('q3', re.compile(r'^[0-9]$')): 'q3',
      ('q3', re.compile(r'^[^0-9\.]$')): 'q4',
      ('q3', re.compile(r'^\.$')): 'q5',
      ('q5', re.compile(r'^[0-9]$')): 'q6',
      ('q6', re.compile(r'^[0-9]$')): 'q6',

      ('q0', re.compile(r'^\"$')): 'q8',
      ('q8', re.compile(r'^[^\"]$')): 'q8',
      ('q8', re.compile(r'^\"$')): 'q9',
      ('q8', re.compile(r'\n')): 'q42',

      ('q0', re.compile(r'^\/$')): 'q10',
      ('q10', re.compile(r'^\/$')): 'q11',
      ('q11', re.compile(r'^[^\/]$')): 'q11',
      ('q11', re.compile(r'\n')): 'q12',
      ('q10', re.compile(r'^[^\/]$')): 'q13',
      
      ('q0', re.compile(r'^\+$')): 'q14',
      ('q0', re.compile(r'^\-$')): 'q15',
      ('q0', re.compile(r'^\*$')): 'q16',
      ('q0', re.compile(r'^\%$')): 'q17',
      ('q0', re.compile(r'^\=$')): 'q18',
      ('q18', re.compile(r'^\=$')): 'q19',
      ('q18', re.compile(r'^[^\=]$')): 'q20',
      ('q0', re.compile(r'^\!$')): 'q21',
      ('q21', re.compile(r'^\=$')): 'q22',
      ('q21', re.compile(r'^[^\!]$')): 'q23',
      ('q0', re.compile(r'^\<$')): 'q24',
      ('q24', re.compile(r'^\=$')): 'q25',
      ('q24', re.compile(r'^[^\<]$')): 'q26',
      ('q0', re.compile(r'^\>$')): 'q27',
      ('q27', re.compile(r'^\=$')): 'q28',
      ('q27', re.compile(r'^[^\>]$')): 'q29',
      ('q0', re.compile(r'^\|$')): 'q30',
      ('q30', re.compile(r'^\|$')): 'q31',
      ('q0', re.compile(r'^\&$')): 'q32',
      ('q32', re.compile(r'^\&$')): 'q33',
      ('q0', re.compile(r'^\,$')): 'q34',
      ('q0', re.compile(r'^\;$')): 'q35',
      ('q0', re.compile(r'^\($')): 'q36',
      ('q0', re.compile(r'^\)$')): 'q37',
      ('q0', re.compile(r'^\[$')): 'q38',
      ('q0', re.compile(r'^\]$')): 'q39',
      ('q0', re.compile(r'^\{$')): 'q40',
      ('q0', re.compile(r'^\}$')): 'q41',
    }

    finish_states = {
      'q1': 'ID',
      'q3': 'NUMINT',
      'q6': 'NUMDEC',
      'q9': 'TEXT',
      'q42': 'ERROR',
      'q12': 'COMMENT',
      'q13': '/',
      'q14': '+',
      'q15': '-',
      'q16': '*',
      'q17': '%',
      'q19': '==',
      'q20': '=',
      'q22': '!=',
      'q23': '!',
      'q25': '>=',
      'q26': '>',
      'q28': '<=',
      'q29': '<',
      'q31': '||',
      'q33': '&&',
      'q34': ',',
      'q35': ';',
      'q36': '(',
      'q37': ')',
      'q38': '[',
      'q39': ']',
      'q40': '{',
      'q41': '}'
    }

    for char in token:
      for (current_state, regex_pattern), next_state in transitions.items():
        if state == current_state and regex_pattern.match(str(char)):
          state = next_state
        
    if state in finish_states:
      if finish_states[state] != "ERROR":
        return finish_states[state]
      else:
        return False
    else:
      return False
```

- Palavras reservadas usadas para verificação no loop:

```python
  reserved_words = {
    "int": "INT",
    "float": "FLOAT",
    "char": "CHAR",
    "boolean": "BOOLEAN",
    "void": "VOID",
    "if": "IF",
    "else": "ELSE",
    "for": "FOR",
    "while": "WHILE",
    "scanf": "SCANF",
    "println": "PRINTLN",
    "main": "MAIN",
    "return": "RETURN"
  }
```