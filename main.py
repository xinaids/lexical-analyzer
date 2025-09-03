from reserved_words import reserved_words
from afd import returnNextState
from read_file import save_string
import re

# Listas auxiliares
id = []
num_int = []
num_dec = []
text = []
chars = []

# Lista final de tokens organizados por linha
tokens_by_line = []

def token_separation(string):
    tokens = []
    line = 1
    col = 1
    temp = ''
    quote_counter = 0
    single_quote_counter = 0
    i = 0

    while i < len(string):
        char = string[i]

        # Quebra de linha
        if char == '\n':
            if temp:
                tokens.append((temp, line, col - len(temp)))
                temp = ''
            if tokens:
                tokens_by_line.append(tokens)
                tokens = []
            line += 1
            col = 1
            i += 1
            continue

        # Comentários de linha // -> ignora
        if char == '/' and i + 1 < len(string) and string[i + 1] == '/':
            if temp:
                tokens.append((temp, line, col - len(temp)))
                temp = ''
            while i < len(string) and string[i] != '\n':
                i += 1
                col += 1
            continue

        # Strings
        if char == '"' and quote_counter == 0:
            if temp:
                tokens.append((temp, line, col - len(temp)))
                temp = ''
            temp += char
            quote_counter = 1
        elif char == '"' and quote_counter == 1:
            temp += char
            tokens.append((temp, line, col - len(temp) + 1))
            temp = ''
            quote_counter = 0
        elif quote_counter == 1:
            temp += char

        # Chars
        elif char == "'" and single_quote_counter == 0:
            if temp:
                tokens.append((temp, line, col - len(temp)))
                temp = ''
            temp += char
            single_quote_counter = 1
        elif char == "'" and single_quote_counter == 1:
            temp += char
            tokens.append((temp, line, col - len(temp) + 1))
            temp = ''
            single_quote_counter = 0
        elif single_quote_counter == 1:
            temp += char

        # Operadores compostos
        elif char in ['=', '<', '>', '!'] and i + 1 < len(string) and string[i + 1] == '=':
            if temp:
                tokens.append((temp, line, col - len(temp)))
                temp = ''
            tokens.append((char + '=', line, col))
            i += 1
            col += 2
            continue

        # Símbolos isolados
        elif re.match(r'[^a-zA-Z0-9\s."\']', char):
            if temp:
                tokens.append((temp, line, col - len(temp)))
                temp = ''
            tokens.append((char, line, col))

        # Último caractere
        elif i == len(string) - 1:
            temp += char
            tokens.append((temp, line, col - len(temp) + 1))
            temp = ''
        elif not char.isspace():
            temp += char
        else:
            if temp:
                tokens.append((temp, line, col - len(temp)))
                temp = ''
        i += 1
        col += 1

    if temp:
        tokens.append((temp, line, col - len(temp)))
    if tokens:
        tokens_by_line.append(tokens)


string = save_string()
token_separation(string)

# Classes de símbolos
class_map = {
    '=': "ATRIBUICAO",
    '==': "COMPARACAO",
    '!=': "COMPARACAO",
    '<': "COMPARACAO",
    '<=': "COMPARACAO",
    '>': "COMPARACAO",
    '>=': "COMPARACAO",

    '+': "ARITMETICO",
    '-': "ARITMETICO",
    '*': "ARITMETICO",
    '%': "ARITMETICO",

    ';': "DELIMITADOR",
    ',': "DELIMITADOR",

    '(': "AGRUPADOR",
    ')': "AGRUPADOR",
    '{': "AGRUPADOR",
    '}': "AGRUPADOR",
    '[': "AGRUPADOR",
    ']': "AGRUPADOR",
}

# --- saída no console e no arquivo ---
with open("resultado.txt", "w", encoding="utf-8") as f:
    for line_tokens in tokens_by_line:
        out = []
        for word, line, col in line_tokens:
            state = returnNextState(word)
            if state != False:
                if word in reserved_words:
                    out.append(f"<PALAVRA_RESERVADA, {word}, {line}, {col}>")
                elif state == 'ID':
                    id.append(word)
                    out.append(f"<ID, {word}, {line}, {col}>")
                elif state == 'NUMINT':
                    num_int.append(word)
                    out.append(f"<NUMERO_INTEIRO, {word}, {line}, {col}>")
                elif state == 'NUMDEC':
                    num_dec.append(word)
                    out.append(f"<NUMERO_DECIMAL, {word}, {line}, {col}>")
                elif state == 'TEXT':
                    text.append(word)
                    out.append(f"<STRING, {word}, {line}, {col}>")
                elif state == 'CHAR':
                    chars.append(word)
                    out.append(f"<CARACTERE, {word}, {line}, {col}>")
                elif state in class_map:
                    out.append(f"<{class_map[state]}, {word}, {line}, {col}>")
                else:
                    out.append(f"<{state}, {word}, {line}, {col}>")
            else:
                msg = f"Erro na análise léxica na linha {line}, coluna {col}"
                print("\033[1;31m" + msg + "\033[0m")
                f.write(msg + "\n")
                break
        line_out = " ".join(out)
        print(line_out)
        f.write(line_out + "\n")
