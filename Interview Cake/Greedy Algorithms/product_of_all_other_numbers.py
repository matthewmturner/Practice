def get_products_of_all_ints_except_at_index(ints_list):

    product = 1
    products = list()
    for n in ints_list[1:]:
        product = product * n
        products.append(n)
        print(product)

    # prods = list()
    # for i, n in ints_list:
    # prods[i] =


nums = [1, 2, 3]
get_products_of_all_ints_except_at_index(nums)
