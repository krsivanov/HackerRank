from collections import Counter
arguments = input().split()
n = int(arguments[0])
m = int(arguments[1])

queries = []

for _ in range(m):
    queries.append(list(map(int, input().rstrip().split())))

def arrayManipulation(n,queries):
    c = Counter()
    for a,b,k in queries:
        c[a]  +=k
        c[b+1]-=k
    arrSum = 0
    maxSum = 0
    for i in sorted(c)[:-1]:
        arrSum+= c[i]
        maxSum = max(maxSum,arrSum)
    return maxSum

print(arrayManipulation(n,queries))
