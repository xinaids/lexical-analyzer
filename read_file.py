def save_string():
    with open('data.txt', 'r', encoding="utf-8") as file:
        string = file.read()
        return string
