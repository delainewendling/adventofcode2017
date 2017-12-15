file = open('day6.txt')
input = file.read()

def getNumRedistributionCycles(input):
    record = []
    check = []
    startingMemoryBank = list(map(int, input.replace("\t", " ").split(" ")))
    record.append(startingMemoryBank)
    check.append("".join(str(e) for e in startingMemoryBank))
    noMatches = True
    count = 0
    secondCount = 0
    toFind = ''
    currentRow = record[count]
    print("current row ", currentRow)
    while (noMatches):
        maxNum = 0
        for num in currentRow:
            if num >= maxNum:
                maxNum = num
        index = currentRow.index(maxNum)
        currentRow[index] = 0
        print("max num ", maxNum, " index ", index)
        counter = 1
        while (maxNum > 0):
            if index+counter < len(currentRow):
                currentRow[index+counter] += 1
            else:
                currentRow[(index+counter)%len(currentRow)] += 1
            maxNum -= 1
            counter += 1
        print("current row now", currentRow)
        currentRowString = "".join(str(e) for e in currentRow)
        if currentRowString in check:
            toFind = currentRowString
            record = [currentRow]
            check = []
            secondCount += 1
            count += 1
        else:
            record.append(currentRow)
            check.append(currentRowString)
            count += 1
            secondCount += 1 if toFind else 0
        if toFind:
            if toFind in check:
                noMatches = False
                return secondCount


print(getNumRedistributionCycles(input))