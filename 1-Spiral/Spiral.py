#File: Spiral.py
#A Practice Project by Isaac Lee
from array import *
inputfile = open("Spiral.txt", "r")

inputcontents = inputfile.readlines()

size = int(inputcontents[0])
print("The Dimensions of the Spiral is:", size)

spiralgrid = [0]*size
for i in range(size):
	spiralgrid[i] = [0] * size

total = size * size
count = 0
while total >= 1:
	for i in range(size - count - 1, count, -1):
		spiralgrid[count][i] = total
		total -= 1
	for j in range(count, size - count, 1):
		spiralgrid[j][count] = total
		total -= 1
	
	for k in range(count + 1, size - count - 1, 1):
		spiralgrid[size - count - 1][k] = total
		total -= 1
	for l in range(size - count - 1, count, - 1):
		spiralgrid[l][size - count - 1] = total
		total -= 1
	count += 1

for i in range(0, size):
		for j in range(0, size):
			print(spiralgrid[i][j], end = " ")
		print("\n")
row = 0
col = 0
for argcount in range(1, len(inputcontents)):
	for i in range(0, size):
		for j in range(0, size):
			if int(inputcontents[argcount]) == spiralgrid[i][j]:
				row = i
				col = j
				break
	sum = 0
	print("location is ", row, col)
	for i in range(row - 1, row + 2):
		for j in range(col - 1, col + 2):
			if i < size and i >= 0 and j < size and j >= 0:
						sum += spiralgrid[i][j]
	sum -= spiralgrid[row][col]
	print("Sum of ", inputcontents[argcount], "is: ", sum) 
