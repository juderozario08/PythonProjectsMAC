def q1(a, b):
    if a == 0 and b == 0:
        return 0
    if a > 0:
        return 1 + q1(a-1, b)
    return 1 + q1(a, b-1)


def q2(num):
    if num <= 1:
        return 0
    if num <= 2:
        return 1
    return 1 + q2(num//2)


def q3(string):
    if len(string) == 0:
        return ''
    return string[len(string)-1::] + q3(string[0:len(string)-1])


def q4(x, n):
    if n == 0:
        return 1
    return x*q4(x, n-1)


countcalls = 0


def q5(x, n):
    global countcalls
    if n == 0:
        return countcalls
    countcalls += 1
    return q5(x, n-1)


def q6(x, n):
    global countcalls
    if n == 0:
        print(countcalls)
        return 1
    countcalls += 1
    if n % 2 == 0:
        return q6(x, n/2)**2
    return x*q6(x, n-1)


def q7():
    f = open('tmuLabs/kdpF.txt')
    line = f.readline()
    print(line)
    seq = ''
    for line in f:
        seq = seq + line
    seq = seq.replace('\n', '')
    seq = seq.upper()
    print(seq)
    print(gcContent(seq))


def gcContent(sequence):
    countG = 0
    countC = 0
    countLen = 0
    for i in sequence:
        if i == 'G':
            countG += 1
        elif i == 'C':
            countC += 1
        countLen += 1
    return f'{(countG/countLen)*100}% of G \n{(countC/countLen)*100}% of C'


if __name__ == '__main__':
    # print(q1(9, 7))
    # print(q2(4))
    # print(q3('Who let the dogs out?'))
    # print(q5(2, 0))
    # print(q6(2, 4))
    q7()
