num_of_friends = int(input())
Pi = []
Wi = []
Di = []
C = 0
final_time = []
for i in range(num_of_friends):
    string = str(input()).split(" ")
    Pi.append(int(string[0]))
    Wi.append(int(string[1]))
    Di.append(int(string[2]))
    C += int(string[0])
C /= num_of_friends
C_copy = C
diff_of_friends = num_of_friends - 1
C -= diff_of_friends
while C <= C_copy + diff_of_friends:
    result = 0
    for i in range(num_of_friends):
        min_dist = C - Di[i]
        max_dist = C + Di[i]
        if Pi[i] < min_dist:
            result += (min_dist - Pi[i]) * Wi[i]
        elif Pi[i] > max_dist:
            result += (Pi[i] - max_dist) * Wi[i]
        else:
            result = 0
    final_time.append(result)
    C += 1
print(int(min(final_time)))
