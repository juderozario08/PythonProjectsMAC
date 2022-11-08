rows, columns = int(input()), int(input())
canvas = [[0]*columns for i in range(rows)]
counter = 0
for i in range(int(input())):
    string = input().split(" ")
    if string[0] == 'R':
        ro = int(string[1])-1
        for j in range(columns):
            if canvas[ro][j] == 0:
                canvas[ro][j] = 1
                counter += 1
            else:
                canvas[ro][j] = 0
                counter -= 1
    else:
        col = int(string[1])-1
        for j in range(rows):
            if canvas[j][col] == 0:
                canvas[j][col] = 1
                counter += 1
            else:
                canvas[j][col] = 0
                counter -= 1
print(counter)
