inputFile = open("palindrome.txt", "r")
fileLines = inputFile.readlines()
for i in fileLines:
    stringSize = len(i)
    stack = []
    newPalin = ""
    for j in range(stringSize - 1):
        stack.append(i[j])
    while len(stack) > 0:
        popChar = stack.pop()
        if i[0] != popChar:
            newPalin += str(popChar)
        else:
            break
    newPalin += str(i.strip('\n'))
    print(newPalin)
