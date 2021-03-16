numList = []
numCount=int(input("Enter The No of Elements: "))
for i in range (1, numCount+1 ):
    listElement=int(input("Enter Elements "))
    numList.append(listElement)
print("Largest Element is ",(max(numList)))
