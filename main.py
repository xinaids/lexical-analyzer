from reserved_words import reserved_words
from afd import returnNextState
from read_file import save_string
import re

separate_string_input = []
id = []
num_int = []
num_dec = []
text = []
tokens = []

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

string = save_string()
token_separation(string)

for  word in separate_string_input:
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

print("Separate string:", separate_string_input)
print("Tokens:", tokens)
print("ID: ", id)
print("NUMINT", num_int)
print("NUMDEC", num_dec)
print("TEXT: ", text)
