file = open('day8.txt')
lines = file.readlines()

def readRegister(instructions):
    record = {}
    highest = []
    for instruction in instructions:
        parts = instruction.split(" ")
        register = parts[0]
        comparatorRegisterName = parts[4]
        record[register] = record.get(register, 0)
        comparatorRegisterValue = record.get(comparatorRegisterName, 0)
        comparison = str(comparatorRegisterValue) + parts[5] + parts[6]
        if eval(comparison):
            record[register] += int(parts[2]) if parts[1] == 'inc' else (-int(parts[2]))
        highest.append(max(record.values()))
    return max(highest)

print(readRegister(lines))