def save_string():
  with open('data.txt', 'r') as file:
    string = file.read()
    return string