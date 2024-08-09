#Complexity Analysis : T O(n) | S O(1)
def isPalindrome(string):
    leftIdx = 0
    rightIdx = len(string) - 1
    while leftIdx < rightIdx:
        if string[leftIdx] != string[rightIdx]:
            return False
        leftIdx += 1
        rightIdx -= 1
    return True

#Complexity Analysis : T O(n) | S O(n)
# def isPalindrome(string):
#     return string == string[::-1]

#Complexity Analysis : T O(n^2) | S O(n)
# def isPalindrome(string):
#     reversedString = ""
#     for i in reversed(range(len(string))):
#         reversedString += string[i]
#     return string == reversedString

#Complexity Analysis : T O(n) | S O(n)
# def isPalindrome(string):
#     reversedChars = []
#     for i in reversed(range(len(string))):
#         reversedChars.append(string[i])
#     return string == "".join(reversedChars)

#Recursive solution
#Complexity Analysis : T O(n) | S O(n)
# def isPalindrome(string, i = 0):
#     j = len(string) - 1 - i
#     return True if i >= j else string[i] == string[j] and isPalindrome(string, i + 1)

# def isPalindrome(string, i = 0):
#     j = len(string) - 1 - i
#     if i >= j:
#         return True
#     if string[i] != string[j]:
#         return False
#     return isPalindrome(string, i + 1)
    
print(isPalindrome("abcdcba"))
