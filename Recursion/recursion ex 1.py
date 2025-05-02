def fact(n):
    if n == 0:
        return 1
    y = n * fact(n - 1)
    return y


def is_even(n):
    if n == 0:
        return True
    elif n == 1:
        return False
    else:
        return is_even(n - 1)


# def is_odd(n):
#     if n==0:
#         return False
#     else:
#         return is_even(n-1)

# print(fact(5))
# print(is_even(6))

a = [5, 6, 4, 10000, 2, 9999999]


def max_recursion(a: list, i: int, big: int):
    if len(a) < i + 1:
        return big

    return max_recursion(a, i + 1, big if big > a[i] else a[i])


# youre thing only works with numbers because you set m = 0,

print(max_recursion(a, 0, 0))


def palindrome(brandon: str, l: int, r: int):
    if l > r or l == r:
        return True

    if brandon[l] != brandon[r]:
        return False

    return palindrome(brandon, l + 1, r - 1)


print(palindrome("anna", 0, len("anna") - 1))
