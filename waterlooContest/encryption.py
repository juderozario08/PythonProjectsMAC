def encrypt(key, string):
    counter = 0
    result = ''
    for i in string:
        if 65 <= i <= 90:
            result += chr((i + key[counter % len(key)]) % 26 + 65)
            counter += 1
    return result


print(encrypt(list(map(ord, input())), list(map(ord, input()))))
