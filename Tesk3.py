import math

#Get two number from keyboard
inputNumberA = int(input("Enter Number A: "))
inputNumberB = float(input("Enter Number B: "))

#Integer cal
print("A + B =" , inputNumberA + inputNumberB)
print("A * B =" , inputNumberA * inputNumberB)
print("A ** B =" , inputNumberA ** inputNumberB)
print("A % B =" , inputNumberA % inputNumberB)
print("Abs of A =", abs(inputNumberA))
print("Abs of B =", abs(inputNumberB))
print("Sqrt of A =" , math.sqrt(inputNumberA))
print("Sqrt of B =" , math.sqrt(inputNumberB))
print("----------------------------------") # break line

#Variable - Integer
print("Number of A:" , inputNumberA)
print(type(inputNumberA))
print("----------------------------------") #break line

#Variable - Float
print("Number of B:" , inputNumberB)
print(type(inputNumberB))
print("----------------------------------") #break line