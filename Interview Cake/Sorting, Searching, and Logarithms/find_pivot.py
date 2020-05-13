def find_pivot(rotated_list):

    left_idx = 0
    right_idx = len(rotated_list) - 1

    while left_idx < right_idx:
        adj = (right_idx - left_idx) // 2
        mid_idx = left_idx + adj
        if rotated_list[mid_idx] < rotated_list[mid_idx - 1]:
            return mid_idx
        elif rotated_list[mid_idx] > rotated_list[right_idx]:
            left_idx = mid_idx
        else:
            right_idx = mid_idx


words = [
    "pandas",
    "petrol",
    "ptolemaic",
    "retrograde",
    "supplant",
    "undulate",
    "xenoepist",
    "asymptote",  # <-- rotates here!
    "babka",
    "banoffee",
    "cat",
    "dentist",
    "dog",
    "engender",
    "karpatka",
    "othellolagkage",
]

print(find_pivot(words))
