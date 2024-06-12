def isValidSubsequence(array, sequence):
    # Write your code here.
    pointer_array = 0
    pointer_sequence = 0

    while pointer_array < len(array) and pointer_sequence < len(sequence):
        if array[pointer_array] == sequence[pointer_sequence]:
            pointer_sequence += 1
        pointer_array += 1

    return pointer_sequence == len(sequence)

print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))
