#exercise
import itertools

letters = ["A", "B", "C", "D", "E", "F"]

#prints needs to be

#(A, B)
#(B, C)
#...
#(E, F)

oldLetter = ""

for letter in letters:
    if letter != "A":
        print(tuple(oldLetter, letter))
    oldLetter = letter

###################

for t in zip(letters[:-1], letters[1:]):
    print(t)

# or use this, it does the same thing

for t in itertools.pairwise(letters):
    print(t)