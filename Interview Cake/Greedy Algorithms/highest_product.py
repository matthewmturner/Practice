from math import inf


def highest_product(input_list):

    sorted_list = sorted(input_list, key=abs, reverse=True)

    product = sorted_list[0] * sorted_list[1] * sorted_list[2]

    if product > 0:
        return product
    else:
        neg_nums = [i for i, n in enumerate(sorted_list[:3]) if n < 0]
        neg_nums_ct = len(neg_nums)

        if neg_nums_ct == 3:
            for i, n in enumerate(sorted_list, 3):
                if n > 0:
                    sorted_list[2] = n
                    break
        elif neg_nums_ct == 1:
            for i, n in enumerate(sorted_list, 3):
                if n > 0:
                    sorted_list[neg_nums[0]] = n
                    break

    product = sorted_list[0] * sorted_list[1] * sorted_list[2]

    return product


n = [-10, -10, 1, 3, 2]

print(highest_product(n))
