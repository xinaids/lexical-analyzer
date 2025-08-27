from reserved_words import reserved_words
from afd import returnNextState
from read_file import save_string
import re

separate_string_input = []
id = []
num_int = []
num_dec = []
text = []
chars = []
comments = []
tokens = []

def token_separation(string):
    global separate_string_input
    temp = ''
    quote_counter = 0
    single_quote_counter = 0

    i = 0
    while i < len(string):
        char = string[i]

        # Ignora quebras de linha
        if char == '\n':
            if temp:
                separate_string_input.append(temp)
                temp = ''
            i += 1
            continue

        # Comentários de linha (// até o fim da linha)
        if char == '/' and i + 1 < len(string) and string[i+1] == '/':
            if temp:
                separate_string_input.append(temp)
                temp = ''
            comment = ''
            while i < len(string) and string[i] != '\n':
                comment += string[i]
                i += 1
            separate_string_input.append(comment)
            continue

        # Strings (aspas duplas)
        if char == '"' and quote_counter == 0:
            if temp:
                separate_string_input.append(temp)
                temp = ''
            temp += char
            quote_counter = 1
        elif char == '"' and quote_counter == 1:
            temp += char
            separate_string_input.append(temp)
            temp = ''
            quote_counter = 0
        elif quote_counter == 1:
            temp += char

        # Chars (aspas simples)
        elif char == "'" and single_quote_counter == 0:
            if temp:
                separate_string_input.append(temp)
                temp = ''
            temp += char
            single_quote_counter = 1
        elif char == "'" and single_quote_counter == 1:
            temp += char
            separate_string_input.append(temp)
            temp = ''
            single_quote_counter = 0
        elif single_quote_counter == 1:
            temp += char

        # Operadores compostos (==, <=, >=, !=)
        elif char in ['=', '<', '>', '!'] and i + 1 < len(string) and string[i+1] == '=':
            if temp:
                separate_string_input.append(temp)
                temp = ''
            separate_string_input.append(char + '=')
            i += 1  # pula o próximo '='

        # Símbolos isolados
        elif re.match(r'[^a-zA-Z0-9\s."\']', char):
            if temp:
                separate_string_input.append(temp)
                temp = ''
            separate_string_input.append(char)

        # Último caractere
        elif i == len(string) - 1:
            temp += char
            separate_string_input.append(temp)
            temp = ''
        elif not char.isspace():
            temp += char
        else:
            if temp:
                separate_string_input.append(temp)
                temp = ''
        i += 1

    separate_string_input = [item for item in separate_string_input if item]

string = save_string()
token_separation(string)

for word in separate_string_input:
    # Comentários tratados direto aqui
    if word.startswith("//"):
        comments.append(word)
        tokens.append("COMMENT_" + str(comments.index(word)))
        continue

    state = returnNextState(word)
    if state != False:
        if word in reserved_words:
            tokens.append(reserved_words[word])
        elif state == 'ID':
            id.append(word)
            tokens.append("ID_" + str(id.index(word)))
        elif state == 'NUMINT':
            num_int.append(word)
            tokens.append("NUMINT_" + str(num_int.index(word)))
        elif state == 'NUMDEC':
            num_dec.append(word)
            tokens.append("NUMDEC_" + str(num_dec.index(word)))
        elif state == 'TEXT':
            text.append(word)
            tokens.append("TEXT_" + str(text.index(word)))
        elif state == 'CHAR':
            chars.append(word)
            tokens.append("CHAR_" + str(chars.index(word)))
        else:
            tokens.append(state)
    else:
        print("\033[1;31mErro na análise léxica\033[0m")
        break

print("Separate string:", separate_string_input)
print("Tokens:", tokens)
print("ID: ", id)
print("NUMINT", num_int)
print("NUMDEC", num_dec)
print("TEXT: ", text)
print("CHAR: ", chars)
print("COMMENT: ", comments)
