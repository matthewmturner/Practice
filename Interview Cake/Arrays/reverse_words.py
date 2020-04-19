def reverse_words(message):

    rev_msg = []
    current_word = []
    for c in message[::-1]:
        if c != " ":
            current_word.insert(0, c)
        else:
            rev_msg.extend(current_word)
            rev_msg.append(" ")
            current_word = []

    rev_msg.extend(current_word)

    for i, c in enumerate(rev_msg):
        message[i] = c


def reverse_words2(msg):

    left_idx = 0
    right_idx = len(msg) - 1

    while left_idx <= len(msg) - 1:
        left_c = msg[left_idx]
        right_c = msg[right_idx]
        msg.pop(0)
        msg.insert(0, right_c)
        msg.pop(right_idx)
        msg.insert(right_idx, left_c)
        left_idx += 1
        right_idx -= 1


def reverse_words3(message):
    left_index = 0
    right_index = len(message) - 1

    # Walk towards the middle, from both sides
    while left_index < right_index:
        # Swap the left char and right char
        message[left_index], message[right_index] = (
            message[right_index],
            message[left_index],
        )
        left_index += 1
        right_index -= 1


message = [
    "c",
    "a",
    "k",
    "e",
    " ",
    "p",
    "o",
    "u",
    "n",
    "d",
    " ",
    "s",
    "t",
    "e",
    "a",
    "l",
]

reverse_words3(message)
print(message)
