def reverse_inplace(list_to_reverse):

    i = 0
    for element in list_to_reverse[::-1]:
        list_to_reverse[i] = element
        i += 1


stuff = [1, 2, 4]

reverse_inplace(stuff)

print(stuff)


def reverse_solution(list_of_chars):

    left_index = 0
    right_index = len(list_of_chars) - 1

    while left_index < right_index:
        # Swap characters
        list_of_chars[left_index], list_of_chars[right_index] = (
            list_of_chars[right_index],
            list_of_chars[left_index],
        )
        # Move towards middle
        left_index += 1
        right_index -= 1
