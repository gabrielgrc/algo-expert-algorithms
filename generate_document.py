# Complexity Analysis : T O(n + m) | S O(c)
def generateDocument(characters, document):
    characterCounts = {}

    for character in characters:
        if character not in characterCounts:
            characterCounts[character] = 0

        characterCounts[character] += 1
    
    for character in document:
        if character not in characterCounts or characterCounts[character] == 0:
            return False

        characterCounts[character] -= 1
    
    return True

#Complexity Analysis : T O(m * (n + m)) | S O(1)
# def generateDocument(characters, document):
#     for character in document:
#         documentFrequency = countCharacterFrequency(character, document)
#         charactersFrequency = countCharacterFrequency(character, characters)
#         if documentFrequency > charactersFrequency:
#             return False
        
#     return True

# def countCharacterFrequency(character, target):
#     frequency = 0
#     for char in target:
#         if char == character:
#             frequency += 1
    
#     return frequency

# Complexity Analysis : T O(c * (n + m)) | S O(c)
# def generateDocument(characters, document):
#     alreadyCounted = set()

#     for character in document:
#         if character in alreadyCounted:
#             continue

#         documentFrequency = countCharacterFrequency(character, document)
#         charactersFrequency = countCharacterFrequency(character, characters)
#         if documentFrequency > charactersFrequency:
#             return False
        
#         alreadyCounted.add(character)
        
#     return True

# def countCharacterFrequency(character, target):
#     frequency = 0
#     for char in target:
#         if char == character:
#             frequency += 1
    
#     return frequency

print(generateDocument("Bste!hetsi ogEAxpelrt x ", "AlgoExpert is the Best!"))
