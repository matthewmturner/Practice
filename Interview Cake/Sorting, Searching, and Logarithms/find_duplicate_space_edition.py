def find_duplicate(values):

    previous = None
    for val in sorted(values):
        current = val
        if current == previous:
            return val
        else:
            previous = current


l = [4, 2, 2, 3]
print(find_duplicate(l))
print(l)
