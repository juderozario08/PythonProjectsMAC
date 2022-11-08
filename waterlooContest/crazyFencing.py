N = int(input())
fenceHeights = str(input()).split(" ")
fenceWidths = str(input()).split(" ")
result = 0
for i in range(N):
    result += int(fenceWidths[i]) * \
        (int(fenceHeights[i])+int(fenceHeights[i+1]))/2
print(result)
