#File about merging separate intervals into non intersecting intervals
#Isaac Lee

InputFile = open("Intervals.txt", "r")
InputContents = InputFile.readlines()
FileList = []
FilterList = []

def Difference(Tuple):
	return abs(Tuple[1] - Tuple[0])

for i in range(len(InputContents)):
	InputNoWhitespace = InputContents[i].split()
	Number1 = int(InputNoWhitespace[0])
	Number2 = int(InputNoWhitespace[1])
	FileList.append((Number1, Number2))

FileList.sort()
print("All Intervals Sorted in Ascending Order:")
for i in range(len(FileList)):
	print(FileList[i])

count = 0
while count < len(FileList) - 1:
	smboundary = FileList[count][0]
	lgboundary = FileList[count][1]
	while(lgboundary >= FileList[count + 1][0]):
		if(FileList[count + 1][1] >= lgboundary):
			lgboundary = FileList[count + 1][1]
		if(count >= len(FileList) - 2):
			break
		else:
			count += 1
	FilterList.append((smboundary, lgboundary))
	count += 1
print("\nAll Non-Intersecting Intervals:")
for i in range(len(FilterList)):
	print(FilterList[i])

SizeList = FilterList
SizeList.sort(key = Difference)
print("\nAll Non-Intersecting Intervals in Order of Size:")
for i in range(len(SizeList)):
	print(SizeList[i])
