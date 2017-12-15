import math

test1 = 12
test2 = 23
test3 = 1024
num = 361527
# Part 1
# def findDistance(number):
#     sqRoot = math.sqrt(number)
#     if sqRoot.is_integer() and sqRoot % 2 != 0:
#         sizeOfSquare = int(sqRoot)
#     elif int(sqRoot) % 2 != 0:
#         sizeOfSquare = int(sqRoot) + 2
#     else:
#         sizeOfSquare = int(sqRoot) + 1
#
#     lastNumInSmallSquare = (sizeOfSquare - 2)**2
#     lastNumInThisSquare = sizeOfSquare ** 2
#     difference = number - lastNumInSmallSquare
#     topRight = lastNumInSmallSquare + sizeOfSquare-1
#     topLeft = lastNumInSmallSquare + 2*(sizeOfSquare-1)
#     bottomLeft = lastNumInSmallSquare + 3*(sizeOfSquare-1)
#     distanceFromCenter = (sizeOfSquare - 1) / 2
#     if number < topRight:
#         yPos = abs(difference-distanceFromCenter)
#         xPos = distanceFromCenter
#     elif number > topRight and number < topLeft:
#         yPos = distanceFromCenter
#         xPos = abs(number - topRight - distanceFromCenter)
#     elif number > topLeft and number < bottomLeft:
#         xPos = distanceFromCenter
#         yPos = abs(number - topLeft - distanceFromCenter)
#     elif number > bottomLeft and number < lastNumInThisSquare:
#         yPos = distanceFromCenter
#         xPos = abs(number-bottomLeft-distanceFromCenter)
#     else:
#         xPos = distanceFromCenter
#         yPos = distanceFromCenter
#     return int(xPos + yPos)

# Part 2
# def findLargerNumber(number):
#
#
#
# print(findDistance(num))