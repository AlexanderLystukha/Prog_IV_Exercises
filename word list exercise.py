
# using binary search, prompt user for a word and search for it
# inside the world list txt file.

from binary_search import binary_search

fh = open("wordlist.txt")

wordlist: list = []
print("Please input the word you want to find:")
word = input()

for line in fh:
    wordlist.append(line.strip("\n"))

index = binary_search(wordlist, 0, len(wordlist)-1, word)

if index is None:
    print("Your file does not exist!")
else:
    print(f"{word} exists in the word list! It is at index {index}")