from reserved_words import reserved_words
from afd import returnNextState

separate_string_input = []
id = []
num_int = []
num_dec = []
text = []
tokens = []

def token_separation(text):
  global separate_string_input
  temp = ''
  quote_counter = 0

  for char in string:
    if temp == '' and char == '"':
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

string = 'int main ( ) { int x = 6.25 ; }'
token_separation(string)

for word in separate_string_input:
  if returnNextState(word) != False:
    if word in reserved_words:
      tokens.append(reserved_words[word])
    elif returnNextState(word) == 'ID':
      id.append(word)
      tokens.append(word)
    elif returnNextState(word) == 'NUMINT':
      num_int.append(word)
      tokens.append(word)
    elif returnNextState(word) == 'NUMDEC':
      num_dec.append(word)
      tokens.append(word)
    elif returnNextState(word) == 'TEXT':
      text.append(word)
      tokens.append(word)
    else:
      tokens.append(word)
  else:
    print("\033[1;31mErro na análise léxica\033[0m")
    break

print("Tokens:", tokens)
print("ID: ", id)
print("NUMINT", num_int)
print("NUMDEC", num_dec)
print("TEXT: ", text)
