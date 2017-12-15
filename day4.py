file = open('day4.txt')
lines = file.readlines()
from collections import Counter

# # Part 1
# def countValid(passphrases):
#     validCount = 0
#     for passphrase in passphrases:
#         words = passphrase.replace("\n", "").split(" ")
#         count = 0
#         for word in words:
#             for otherWord in words:
#                 if word == otherWord:
#                     count += 1
#         if count == len(words):
#             validCount += 1
#     return validCount

# Part 2
def countValid(passphrases):
    validCount = 0
    for passphrase in passphrases:
        words = passphrase.replace("\n", "").split(" ")
        count = 0
        for word in words:
            for otherWord in words:
                if word == otherWord:
                    count += 1
                elif Counter(word) == Counter(otherWord):
                    count += 1
        if count == len(words):
            validCount += 1
    return validCount


print(countValid(lines))