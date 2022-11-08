def encrypt(key, string):
    counter = 0
    result = ''
    for i in string:
        if 65 <= i <= 90:
            result += chr((i-65 + key[counter % len(key)]-65) % 26 + 65)
            counter += 1
    return result


print(encrypt(list(map(ord, input())), list(map(ord, input()))))
