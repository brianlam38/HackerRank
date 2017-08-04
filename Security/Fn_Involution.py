# scan stdin
numInputs = input()
inputList = input().split(" ")

count = 1
i = 0
outputList = [0] * int(numInputs)

# add inverses to output list
for i in inputList:
    outputList[int(i)-1] = count
    count += 1

# check if function is an involution
k = 1
answer = 'NO'
for j in outputList:
    if outputList[int(j)-1] == k and outputList[k-1] == int(j):
        answer = 'YES'

# print result
print(answer)