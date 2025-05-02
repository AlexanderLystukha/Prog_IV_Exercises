def all_elements(l1: list, l2: list) -> list:
    return list(set(l1).intersection(set(l2)))

    # results: list = []
    #
    # for x in l1:
    #     results.append(x)
    #
    # for x in l2:
    #     found: bool = False
    #     for y in l1:
    #         if x == y:
    #             found = True
    #             break
    #     if not found:
    #         results.append(x)
    #
    # return set(results)

print(all_elements([3, 2, 7, 4], [1, 2, 3]))
