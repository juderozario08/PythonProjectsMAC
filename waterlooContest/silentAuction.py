numOfCandidates = int(input())
votes = []
names = []
maxVotes = 0
index = 0
for i in range(numOfCandidates):
    name = input()
    vote = int(input())
    names.append(name)
    votes.append(vote)
    if maxVotes < vote:
        maxVotes = vote
        index = i
print(names[index])
