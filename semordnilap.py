#Complexity Analysis : T O(n * m) | S O(n * m)
def semordnilap(words):
    wordsSet = set(words)
    semordnilapPairs = []

    for word in words:
        reverse = word[::-1]
        if reverse in wordsSet and reverse != word:
            semordnilapPairs.append([word, reverse])
            wordsSet.remove(word)
            wordsSet.remove(reverse)

    return semordnilapPairs

print(semordnilap(["diaper", "abc", "test", "cba", "repaid"]))
