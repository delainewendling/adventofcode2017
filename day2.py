file = open('day2.txt')
lines = file.readlines()

# Part 1

# def getCheckSum(input):
#     checksum = 0
#     for line in lines:
#         lineNums = line.replace("\t", ",").replace("\n", "").split(",")
#         lineDigits = list(map(int, lineNums))
#         difference = max(lineDigits) - min(lineDigits)
#         checksum += difference
#     print(checksum)


# Part 2
def getCheckSum(input):
    checksum = 0
    for line in lines:
        lineNums = line.replace("\t", ",").replace("\n", "").split(",")
        lineDigits = list(map(int, lineNums))
        for digit in lineDigits:
            for anotherDigit in lineDigits:
                dividend = anotherDigit/digit
                checksum += dividend if dividend != 1 and dividend % 1 == 0 else 0
    return checksum

print(getCheckSum(lines))