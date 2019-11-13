def encrypt(string):
    multiplier = 1
    while(multiplier * multiplier < len(string)):
            multiplier += 1
    EncryptGrid = [['*']*multiplier for i in range(multiplier)]
    row = 0
    col = 0
    for letter in string:
        if col < multiplier:
            EncryptGrid[row][col] = letter
            col += 1
        else:    
            row += 1
            col = 0
            EncryptGrid[row][col] = letter
            col += 1
    #begin encryption process
    Grid = [['*']*multiplier for i in range(multiplier)]
    for i in range(multiplier):
        for j in range(multiplier):
            Grid[j][multiplier - 1 - i] = EncryptGrid[i][j]
    EncryptGrid = Grid
    EncString = ""
    for i in range(multiplier):
        for j in range(multiplier):
            if(str(EncryptGrid[i][j]) != "*" and str(EncryptGrid[i][j]) != "\n"):
                EncString += str(EncryptGrid[i][j])
    return EncString
def decrypt(string):
    multiplier = 1
    while(multiplier * multiplier < len(string)):
            multiplier += 1
    DecryptGrid = ['*']*multiplier
    for i in range(multiplier):
        DecryptGrid[i] = ['*']*multiplier
    row = 0
    col = 0
    for letter in string:
        if col < multiplier:
            DecryptGrid[row][col] = letter
            col += 1
        else:
            row += 1
            col = 0
            DecryptGrid[row][col] = letter
            col += 1
        #begin decryption process
    Grid = [['*']*multiplier for i in range(multiplier)]
    for i in range(multiplier):
        for j in range(multiplier):
            Grid[multiplier - 1 - j][i] = DecryptGrid[i][j]
#           print(multiplier - 1 - j, i, str(DecryptGrid[i][j]))
#   for i in range(multiplier):
#       for j in range(multiplier):
#           print(Grid[i][j])
    DecryptGrid = Grid
    DecString = ""
    for i in range(multiplier):
        for j in range(multiplier):
            if(str(DecryptGrid[i][j]) != "*" and str(DecryptGrid[i][j]) != "\n"):
                DecString += str(DecryptGrid[i][j])        
    return DecString
def main():
    InputEncrypt = open("Encrypt.txt", "r")
    InputDecrypt = open("Decrypt.txt", "r")
    EncryptContent = InputEncrypt.readlines() 
    DecryptContent = InputDecrypt.readlines() 
    EncryptSize = int(EncryptContent[0])
    DecryptSize = int(DecryptContent[0])

    print("Encryptions:")
    for EncCount in range(1, EncryptSize + 1):
        EncString = encrypt(EncryptContent[EncCount])
        print(EncString)
    print("Decryptions:")
    for DecCount in range(1, DecryptSize + 1):
        DecString = decrypt(DecryptContent[DecCount])
        print(DecString)
main()
