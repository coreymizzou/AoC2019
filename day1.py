f = open('input.txt')
data = f.read().splitlines()


def fuelNeeded(mass):
    fuel = int(mass) // 3 -2
    return fuel
    
#part 1
def fuelPartOne(mass):
    fuel = 0
    for x in mass:
        fuel += fuelNeeded(x)
    return fuel
    
#part 2
def fuelPartTwo(mass):
    fuelList = []
    for x in mass:
        newFuel = fuelNeeded(x)
        totalFuel = 0
        while newFuel > 0:
            totalFuel += newFuel
            newFuel = fuelNeeded(newFuel)
        fuelList.append(totalFuel)
    return sum(fuelList)
    

print(fuelPartOne(data))
print(fuelPartTwo(data))
