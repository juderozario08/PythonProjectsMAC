def operation(L, scalar):
    updatedL = []
    for i in L:
        updatedL.append(i*scalar if i != 4 else i)
    return updatedL


if __name__ == '__main__':
    L = []
    size = int(input("Enter the number of numbers you have: "))
    for i in range(size):
        L.append(int(input("Enter a number: ")))
    if len(set(L)) != len(L):
        print('-1')
    else:
        scalar = int(input("Enter a scalar value: "))
        operation(L, scalar)
