def string_permutation_palindrome(word):

    char_counts = dict()
    for char in word:
        ct = char_counts.setdefault(char, 0)
        char_counts[char] += 1

    length = len(char_counts)
    if length % 2 == 0:
        checks = [ct % 2 == 0 for ct in char_counts.values()]
        return all(checks)
    else:
        checks = [ct % 2 for ct in char_counts.values()]
        return sum(checks) == 1


def has_palindrome_permutation_solution(the_string):
    # Track characters we've seen an odd number of times
    unpaired_characters = set()

    for char in the_string:
        if char in unpaired_characters:
            unpaired_characters.remove(char)
        else:
            unpaired_characters.add(char)

    # The string has a palindrome permutation if it
    # has one or zero characters without a pair
    return len(unpaired_characters) <= 1


print(string_permutation_palindrome("civiccc"))
