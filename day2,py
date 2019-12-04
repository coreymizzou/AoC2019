#open input file
f = open('input.txt')
data = f.readline()

#splits list by comma
splitData = data.split(",")

#converts items in list to integer type
for y in range(len(splitData)):
    splitData[y] = int(splitData[y])
    
i = 0

#op add
while (splitData[i] != 99):
    if (int(splitData[i]) == 1):
        a = splitData[i+1]
        b = splitData[i+2]
        c = splitData[i+3]
        splitData[c] = splitData[a] + splitData[b]
        i += 4
    elif (int(splitData[i]) == 2):
        a = splitData[i+1]
        b = splitData[i+2]
        c = splitData[i+3]
        splitData[c] = splitData[a] * splitData[b]
        i += 4
print(splitData[0])
