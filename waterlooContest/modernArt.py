rows = int(input())
columns = int(input())
num_of_changes = int(input())
row_changes = []
column_changes = []
canvas = []
for i in range(num_of_changes):
    change = str(input())
    if change[0] == "R":
        change = int(change[2:])
        row_changes.append(change)
    else:
        change = int(change[2:])
        column_changes.append(change)
for i in range(rows):
    result = []
    for j in range(columns):
        result.append(True)
    canvas.append(result)
for i in row_changes:
    for j in range(columns):
        if canvas[i-1][j] is True:
            canvas[i-1][j] = False
        else:
            canvas[i-1][j] = True
for i in column_changes:
    for j in range(rows):
        if canvas[j][i-1] is True:
            canvas[j][i-1] = False
        else:
            canvas[j][i-1] = True
counter = 0
for i in range(rows):
    for j in canvas[i]:
        if j is False:
            counter += 1
print(counter)
