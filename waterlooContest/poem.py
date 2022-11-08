R = []
vowels = 'aeiou'
for verse in [[input() for j in range(4)] for i in range(int(input()))]:
    for line in verse:
        lastWord = line.split(" ")[-1].lower()
        result = ''
        for character in range(len(lastWord)-1, -1, -1):
            result += lastWord[character]
            if lastWord[character] in vowels:
                break
        R.append(result)
    if R[0] == R[1] == R[2] == R[3]:
        print('perfect')
    elif R[0] == R[1] and R[2] == R[3]:
        print('even')
    elif R[0] == R[3] and R[1] == R[2]:
        print('shell')
    elif R[0] == R[2] and R[1] == R[3]:
        print('cross')
    else:
        print('free')
    R.clear()
