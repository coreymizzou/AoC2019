#open input file
f = open('input.txt')
data = f.readline()

#splits list by comma
splitData = data.split(",")

#converts items in list to integer type
for y in range(len(splitData)):
    splitData[y] = int(splitData[y])

#op add
def opcode(data):
    i = 0
    while (data[i] != 99):
        if (int(data[i]) == 1):
            a = data[i+1]
            b = data[i+2]
            c = data[i+3]
            data[c] = data[a] + data[b]
            i += 4
        elif (int(data[i]) == 2):
            a = data[i+1]
            b = data[i+2]
            c = data[i+3]
            data[c] = data[a] * data[b]
            i += 4
    return data[0]

def part2(data):
    for noun in range(100):
        for verb in range(100):
            if part1(data, noun, verb) == 19690720:
                return 100 * noun + verb

print(opcode(splitData))
print(part2(splitData))
