"""
    Parsing user input for integral calculator
    """


string = input().replace(" ", "")
properString = ''
for i in range(len(string)):
    if string[i] == '-' and i != 0:
        properString += "+"+string[i]
    else:
        properString += string[i]

properString = properString.replace(" ", "").split("+")
upperBound = 3
lowerBound = 2
result = 0
for i in range(len(properString)):
    if properString[i][0] == 'x':
        properString[i] = "1"+properString[i]
    elif properString[i][:2] == '-x':
        properString[i] = "-1"+properString[i][1:]
    if properString[i][-1] == 'x':
        properString[i] += "^1"
for i in properString:
    xIndex = i.find('x')
    result += float(i[0:xIndex]) * upperBound**float(i[xIndex+2:len(i)]) - \
        float(i[0:xIndex]) * lowerBound**float(i[xIndex+2:len(i)])
print(properString)
print(result)
