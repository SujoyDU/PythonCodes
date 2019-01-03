#Bubble sort 

def bubbleSort(listOfElements):
    print ("Unsorted List:", end=" ")
    print(listOfElements)
    for i in range(len(listOfElements)):
        for j in range(len(listOfElements)-i-1):

            if (listOfElements[j]>listOfElements[j+1]):
                temp = listOfElements[j]
                listOfElements[j]=listOfElements[j+1]
                listOfElements[j+1] = temp
    
    print ("After Bubble Sort", end=" ")
    print(listOfElements)


def mergeSort(listOfElements):
    if(len(listOfElements)>1):
        mid = len(listOfElements)//2
        leftElements = listOfElements[:mid]
        rightElements= listOfElements[mid:]
        
        mergeSort(leftElements)
        mergeSort(rightElements)

        i=j=k=0

        while (i<len(leftElements) and j<len(rightElements)):

            if leftElements[i] < rightElements[j]:
                listOfElements[k]=leftElements[i]
                i += 1
            else: 
                listOfElements[k] =rightElements[j]
                j += 1
            k +=1
        
        while i< len(leftElements):
            listOfElements[k] = leftElements[i]
            i += 1
            k += 1

        while j < len(rightElements):
            listOfElements[k] = rightElements[j]
            j += 1
            k += 1

    print (listOfElements)

def selectionSort(arrList,startIndex=0):
    if startIndex < len(arrList):
        minVal,index = min((val, idx) for idx, val in enumerate(arrList[startIndex:]))
        index += startIndex
        arrList[index] = arrList[startIndex]
        arrList[startIndex] = minVal
        selectionSort(arrList,startIndex+1)



if __name__ == ('__main__'):
    listOfItems = [48,27,22,90,100,33,67]
    # bubbleSort(listOfItems)
    # mergeSort(listOfItems)
    selectionSort(listOfItems)
    print(listOfItems)

