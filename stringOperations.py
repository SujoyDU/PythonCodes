from functools import reduce

def removeCharToMakeAnagram(str1,str2):
    print(f'{str1} {str2}')
    frequencyStr1 = [0]*26
    frequencyStr2 = [0]*26
    
    for ch in str1:
        frequencyStr1[ord(ch)-ord('a')] +=1
    for ch in str2:
        frequencyStr2[ord(ch) - ord('a')] +=1
    
    print(frequencyStr1)
    print(frequencyStr2)
    sum1 = reduce((lambda x,y : x+y),frequencyStr1)
    sum2 = reduce((lambda x,y: x+y),frequencyStr2)
    print(sum1)
    print(sum2)

    for index, value in enumerate(frequencyStr1):
        if(frequencyStr1[index]>frequencyStr2[index]):
            ch = chr(index+ ord('a'))
            print(f"remove {ch} from {index}")
            frequencyStr1[index] -= 1
        elif (frequencyStr1[index]<frequencyStr2[index]):
            ch = chr(index+ ord('a'))
            print(f"remove {ch} from {index}")
            frequencyStr2[index] -= 1
    
    getAnagram1 = ''
    for i in range(len(frequencyStr1)):
        if frequencyStr1[i] != 0:
            getAnagram1 += chr(i + ord('a'))
    
    getAnagram2 = ''
    for i in range(len(frequencyStr2)):
        if(frequencyStr2[i] != 0):
            getAnagram2 += chr(i + ord('a'))


    print(getAnagram1 + " " + getAnagram2)






def isPalindrome(str1):
    print(str1)
    if(str1 == str1[::-1]):
        print(str1+" is palindrome")
    else: print(str1 + " is not palindrome")


def isAnagram(str1,str2):
    print(str1)
    print(str2)
    list_str1 = list(str1)
    list_str2 = list(str2)
    list_str1.sort()
    list_str2.sort()
    
    if(list_str1 == list_str2):
        print(str1 + " and "+ str2 + " are anagrams")
    else: print (str1 + " and "+ str2 + " are not anagrams")
    


if __name__ == ("__main__"):
    # isPalindrome("hannah")
    # isAnagram('list','split')
    removeCharToMakeAnagram('abcdcetts','bbccddt')
