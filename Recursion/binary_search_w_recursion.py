def binary_search(a_list: list, start: int, stop: int, value):
    m = (start + stop) // 2
    if value == a_list[m]:
        return True
    if start > stop:
        return False
    if value < a_list[m]:
        return binary_search(a_list, start, m - 1, value)
    else:
        return binary_search(a_list, m + 1, stop, value)


def search(a_list, value):
    return binary_search(a_list, 0, len(a_list - 1), value)


a = [1, 2, 3, 4, 5]

print(search(a, 1))
