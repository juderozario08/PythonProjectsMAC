with open('tmuLabs/Tuesday8am/secret_code.txt', 'r+') as f:
    reading = list(iter(f))
    faultCode = 'https://tinyurl.com/'
    for i in reading:
        for j in range(1, len(i)):
            decoded = chr((ord(i[j])-65 + 6) % 26 + 65)
            if decoded.upper() != i[j].upper() and i[j].isupper():
                faultCode += decoded.upper()
    f.write('\n'+faultCode)
