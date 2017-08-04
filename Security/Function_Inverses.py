# Enter your code here. Read input from STDIN. Print output to STDOUT
numInputs = input().split(" ")
inputsList = input().split(" ")


i = 0
count = 1
outputList = [0] * int(numInputs[0])

# insert inverses into output list
for i in inputsList:
    if count < int(numInputs[0]) + 1:
        outputList[int(i)-1] = count
        count += 1

# print output list
j = 0
for j in outputList:
    print(j)


    
