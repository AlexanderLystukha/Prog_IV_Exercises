def map_list(f, xs: list) -> list:
    ys: list = []
    for x in xs:
        ys.append(f(x))
    return ys

f =lambda x: x * 7

print(list(map_list(f, [3, 5, 7, 1, 2, 3, 7])))

