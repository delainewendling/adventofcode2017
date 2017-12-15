file = open('day5.txt')
numList = list(map(int, file.read().split("\n")))

# Parts 1 and 2
def getNumSteps(input):
    count = 0
    nextIndex = 0
    nextValue = 0
    insideLoop = True
    while(insideLoop):
        if count == 0:
            nextIndex = input[0]
            count += 1
            input[0] += 1 if nextIndex < 3 else (-1)
            # input[0] += 1
            if abs(nextIndex) < len(input):
                nextValue = input[nextIndex]
            else:
                insideLoop = False
                return count
        else:
            nextIndex += nextValue
            if abs(nextIndex) < len(input):
                count += 1
                nextValue = input[nextIndex]
                input[nextIndex] += 1 if nextValue < 3 else (-1)
                # input[nextIndex] += 1
            else:
                print("Are we out yet?")
                insideLoop = False
                return count
    return count

print(getNumSteps(numList))