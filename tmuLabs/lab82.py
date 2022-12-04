''' 
#### Outputs ####
Question 1
16

Question 2
5

Question 3
?tuo sgod eht tel ohW

Question 4
4096

Question 5
13

Question 6
4096
6

Question 7
>200 bp region of the chromosome of E. coli, containing gene kdpF, shortest gene

TTGCAGCCAGAATTCTACCCTTCCGGTATCACTTTTAGGCCATTGGAGGTGCACTATGAGTGCAGGCGTGATAACCGGCGT
ATTGCTGGTGTTTTTATTACTGGGTTATCTGGTTTATGCCCTGATCAATGCGGAGGCGTTCTGATGGCTGCGCAAGGGTTCTT
ACTGATCGCCACGTTTTTACTGGTGTTAATGGTGC

48.743718592964825
'''


def add(a, b):
    if b == 1:
        return a+1
    return 1 + add(a, b-1)


def log2(x):
    if x <= 1:
        return 0
    return 1 + log2(x/2)


def reverse(sentence):
    if len(sentence) == 1:
        return sentence
    return sentence[len(sentence)-1:] + reverse(sentence[0:len(sentence)-1])


def power(x, n):
    if n == 0:
        return 1
    return x*power(x, n-1)


countcalls = 0


def powerCounter(x, n):
    global countcalls
    countcalls += 1
    if n == 0:
        return countcalls
    return powerCounter(x, n-1)


def betterPower(x, n):
    global countcalls
    countcalls += 1
    if n == 0:
        return 1
    else:
        if n % 2 == 0:
            return betterPower(x, n/2)**2
        return x*betterPower(x, n-1)


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
    return (((len(sequence) - len(sequence.replace('G', '').replace('C', ''))) / len(sequence)) * 100)


if __name__ == '__main__':
    print('Question 1')
    print(add(9, 7))
    print('\nQuestion 2')
    print(log2(20))
    print('\nQuestion 3')
    print(reverse('Who let the dogs out?'))
    print('\nQuestion 4')
    print(power(2, 12))
    print('\nQuestion 5')
    print(powerCounter(2, 12))
    print('\nQuestion 6')
    countcalls = 0
    print(betterPower(2, 10))
    print(countcalls)
    print('\nQuestion 7')
    q7()
