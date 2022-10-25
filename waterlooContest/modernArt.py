rows, columns = int(input()), int(input())
canvas = [0]*columns*rows
for i in range(int(input())):
    string = input().split(" ")
    index = int(string[1])-1
    if string[0] == 'R':
        for i in range(columns):
            ind = i + (index * columns)
            canvas[ind] += 1
    else:
        for i in range(rows):
            ind = index + (i * columns)
            canvas[ind] += 1
print(sum([1 for i in canvas if i % 2 == 1]))


# row, col, numOfChanges = int(input()), int(input()), int(input())
# rows = set()
# columns = set()
# for i in range(numOfChanges):
#     change = input().split(" ")
#     (rows.remove(change[1]) if change[1] in rows else rows.add(
#         change[1])) if change[0] == 'R' else (columns.remove(change[1]) if change[1] in columns else columns.add(change[1]))
#     # Number of changes in rows + Number of actual changes in columns -
# print(row * len(columns) + col * len(rows) - 2 * len(columns) * len(rows))
