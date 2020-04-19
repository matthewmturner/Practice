def is_fifo(take_out, dine_in, served):

    t = []
    d = []
    for i in served:
        if i in take_out:
            t.append(i)
        else:
            d.append(i)

    if (t == take_out) and (d == dine_in):
        return True
    else:
        return False


def is_fifo2(take_out, dine_in, served):

    t_len = len(take_out)
    d_len = len(dine_in)

    t_idx = 0
    d_idx = 0
    for i in served:
        if (t_idx < t_len) and (i == take_out[t_idx]):
            t_idx += 1
        elif (d_idx < d_len) and (i == dine_in[d_idx]):
            d_idx += 1
        else:
            return False

    if (t_idx == t_len) and (d_idx == d_len):
        return True
    else:
        return False


to = [1, 3, 5]
di = [2, 4, 6]
s = [1, 2, 3, 5, 4, 6]

print(is_fifo2(to, di, s))
