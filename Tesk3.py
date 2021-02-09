# Abiz3530 Assignment 1 tesk 3
# Mini farm management app
# Name: Zuhao Fang. Student Number: 7876277
import math
# get name from user
firstName = str(input("Whats your first name: "))
lastName = str(input("Whats you last name: "))
farmName = "Welcome " + firstName + " " + lastName + "'s mini farm"

# get each spot on farm
spotOne = int(input("How many plant you wanna set in your first Spot?"))
spotTwo = int(input("How many plant you wanna set in your second Spot?"))
spotThree = int(input("How many plant you wanna set in your third Spot?"))
spotFour = int(input("How many plant you wanna set in your fourth Spot?"))
farmSpot = [spotOne, spotTwo, spotThree, spotFour]
totalplant = spotOne + spotTwo + spotThree + spotFour # get total number of plant

# each spot fill what kind of plant
spotDict = {'Spot 1':'Apple tree', 'Spot 2':'Banana tree', 'Spot 3':'Orange tree', 'Spot 4':'Peach tree'}

print(spotDict)
print(farmName)

for x in farmSpot:
     for key in spotDict.keys():
        print(key + " have ", x, " " + spotDict[key])


print("--------------------------------")
print("Only break line to finnish integer part")
print(66 + 77)
print(3 ** 5 )
print(7 * 6 / 45)
print(abs(4))
print(math.sqrt(81))





