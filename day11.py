import math

file = open('day11.txt')
directions = file.read()

def getDistance(input):
    directions= input.split(',')
    x = 0
    y = 1
    for direction in directions:
        print(direction)
        if direction == 'n':
            y += 1
        elif direction == 's':
            y -= 1
        elif direction == 'nw':
            x -= 0.5
            y += 0.5
        elif direction == 'ne':
            x += 0.5
            y += 0.5
        elif direction == 'sw':
            x -= 0.5
            y -= 0.5
        else:
            x += 0.5
            y -= 0.5
    print(" x ", x, " y ", y)
    numSteps = math.sqrt(x**2 + y**2)
    return numSteps

print(getDistance(directions))