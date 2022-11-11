with open('tmuLabs/secret_code.txt', 'r') as secret_file:
    code = ''
    lines = list(iter(secret_file))
    for line in lines:
        for char in range(1, len(line)):
            if line[char].isalpha() and line[char].isupper():
                code += chr((ord(line[char].lower()) - 97 + 6) % 26 + 97)
    print(f'https://tinyurl.com/{code.upper()}')
