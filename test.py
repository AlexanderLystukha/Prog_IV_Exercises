# p1 = (3, 5)
# p2 = [4, 6, 0]
#
# def dist(p1: tuple[int, int], p2: list[int]):
#     x1, y1 = p1
#     x2, y2 = p2
#
#
# dist(p1, p2)


# list of tuples

a = [(1, "one"), (6, "six"), (2, "two")]

a.sort()

print(a)

#################

# l = [1, 2, 3, 4]

# the * auto unpacks a list or tuple
# print(*l)
#
# n = ["one", "two", "three", "four"]
#
# for name, value in zip(l, n):
#     print(name, value)
#
# for t in zip(l, n):
#     print(t)

##################

# a, *b = l
#
# print(a)
# print(b)


###################

# some things for assignment 1 maybe (just cool stuff i think)

# hi = "add 3 5"
# hey = "query 6"
#
# # "*" basically takes the rest and puts it into a list
# cmd, *options = hi.split()
#
# #splicing, works with lists, works with strings (because it is a list of characters)
# #works with tuples, if you dont modify the amount.
#
# file_name = "blabla.py"
#
# if(file_name[-3:] == ".py"):
#     print("its a python file ip ip oora!")

##############################

a = [1,2,3]
print(*a)





