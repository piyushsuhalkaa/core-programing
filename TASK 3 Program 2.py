inputString = str(input("Enter String: "))
lenOfString = len(inputString)
reversedString = []
skipCount = int(input("Skip Count: "))
lastElementOfString = inputString[-1]
firstElementsOfString = inputString[0:len(inputString)-1]
if lenOfString%2==0:
    if(skipCount == 2):
        for i in range(len(firstElementsOfString)+1):
            if i%2==1:
                reversedString.append(inputString[i])
                reversedString.append(inputString[i-1])
        print("".join(reversedString))
    elif (skipCount == 3):
        for i in range(lenOfString+1):
            if i%3==1:
                reversedString.append(inputString[i+1])
                reversedString.append(inputString[i])
                reversedString.append(inputString[i-1])
        print("".join(reversedString))
    elif (skipCount == 4):
        for i in range(len(firstElementsOfString)+1):
            if i%4==1:
                reversedString.append(firstElementsOfString[i+2])
                reversedString.append(firstElementsOfString[i+1])
                reversedString.append(firstElementsOfString[i])
                reversedString.append(firstElementsOfString[i-1])
        print("".join(reversedString))
    else:
        print("Bye Bye")
else:
    if(skipCount == 2):
        for i in range(len(firstElementsOfString)+1):
            if i%2==1:
                reversedString.append(inputString[i])
                reversedString.append(inputString[i-1])
        reversedString.append(lastElementOfString)
        print("".join(reversedString))
    elif(skipCount == 3):
        for i in range(lenOfString+1):
            if i%3==1:
                reversedString.append(inputString[i+1])
                reversedString.append(inputString[i])
                reversedString.append(inputString[i-1])
        print("".join(reversedString))
    elif(skipCount == 4):
        for i in range(len(firstElementsOfString)+1):
            if i%4==1:
                reversedString.append(firstElementsOfString[i+2])
                reversedString.append(firstElementsOfString[i+1])
                reversedString.append(firstElementsOfString[i])
                reversedString.append(firstElementsOfString[i-1])
        reversedString.append(inputString[-1])
        print("".join(reversedString))
    else:
        print("Bye Bye")