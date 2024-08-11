#First Solution
#Complexity Analysis : T O(n * m) | S O(c)
def commonCharacters(strings):
    characterCounts = {}
    for string in strings:
        uniqueStringCharacters = set(string)
        for character in uniqueStringCharacters:
            if character not in characterCounts:
                characterCounts[character] = 0
            characterCounts[character] += 1
    
    finalCharacters = []
    for character, count in characterCounts.items():
        if count == len(strings):
            finalCharacters.append(character)
    
    return finalCharacters

#Second Solution
# #Complexity Analysis : T O(n * m) | S O(m)
# def commonCharacters(strings):
#     smallestString = getSmallestString(strings)
#     potentialCommonCharacters = set(smallestString)

#     for string in strings:
#         removeNonExistantCharacters(string, potentialCommonCharacters)

#     return list(potentialCommonCharacters)

# def getSmallestString(strings):
#     smallestString = strings[0]
#     for string in strings:
#         if len(string) < len(smallestString):
#             smallestString = string
    
#     return smallestString

# def removeNonExistantCharacters(string, potentialCommonCharacters):
#     uniqueStringCharacters = set(string)

#     for character in list(potentialCommonCharacters):
#         if character not in uniqueStringCharacters:
#             potentialCommonCharacters.remove(character)
          
print(commonCharacters(["abc", "bcd", "cbaccd"]))
