def bowTie(h):
    print(
        ''.join(['*'*(2*i + 1) + ' '*2*(h - (2*i + 1)) + '*'*(2*i + 1)+'\n' for i in range(h//2 + 1)]) + ''.join(
            ['*'*(2*i + 1) + ' '*2*(h - (2*i + 1)) + '*'*(2*i + 1)+'\n' for i in range(h//2 - 1, -1, -1)]))


bowTie(int(input()))
