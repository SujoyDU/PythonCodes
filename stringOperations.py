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
    isPalindrome("hannah")
    isAnagram('list','split')