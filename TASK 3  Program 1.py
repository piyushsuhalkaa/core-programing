inputString = input("Enter String ")
lenOfString = len(inputString)
reversedString = []
if lenOfString%2==0:
    for i in range(lenOfString+1):
        if i%2==1:
            reversedString.append(inputString[i])
            reversedString.append(inputString[i-1])
    print("".join(reversedString))
else:
    firstElementsOfString = inputString[0:lenOfString-1]
    lastElementOfString = inputString[-1]
    for i in range(len(firstElementsOfString)+1):
        if i%2==1:
            reversedString.append(inputString[i])
            reversedString.append(inputString[i-1])
    reversedString.append(lastElementOfString)
    print("".join(reversedString))