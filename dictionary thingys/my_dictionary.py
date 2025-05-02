from typing import Any

KEY_VALUE = tuple[str, Any]


class MyDictionary:
    def __init__(self, filename):
        """read in a list of words, set translation of word to "None" """

        fh = open(filename, "r")
        self.number_buckets: int = 1 << 5
        self._set = [[] for _ in range(self.number_buckets)]
        for line in map(str.strip, fh):
            index: int = self._hash(line)
            self._set[index].append((line, ''))

        fh.close()

    def _hash(self, key: str) -> int:
        """convert key into an integer"""

        h = 0
        for c in key:
            h = h * 10 + (ord(c) - ord("a"))

        return h % self.number_buckets

    def get_value(self, word: str) -> Any:
        """
        gets the description for 'word'
        raises 'KeyError' if word is not found in your dictionary
        """
        index = self._hash(word)
        for wordTuple in self._set[index]:
            if wordTuple[0] == word:
                return wordTuple[1]

        raise KeyError(f"${word} not in the dictionary!")

    def set_description(self, word: str, description: Any):
        """
        sets the description for 'word'
        raises 'KeyError' if word is not found in your dictionary
        """
        index = self._hash(word)
        if word in self._set[index]:
            input()


    def __contains__(self, key: str):
        """
        function that allows this class to use:
        'if word in my_dictionary:'
        """
        index: int = self._hash(key)
        return key in self._set[index]


# =============================================================================
# validation
# =============================================================================
if __name__ == "__main__":

    my_dict = MyDictionary("wordlist.txt")

    print("Test Getting Values:")
    for this_word in ("tennessee", "exploit", "sagitta", "printer"):
        print(f"Current description of {this_word} is '{my_dict.get_value(this_word)}'")

    print()
    print("Test Setting Values:")
    for this_word in ("tennessee", "exploit", "sagitta", "printer"):
        value = input(f"Enter description for {this_word}: ")
        my_dict.set_description(this_word, value)

    print()
    for this_word in ("tennessee", "exploit", "sagitta", "printer"):
        print(f"Updated description of {this_word} is '{my_dict.get_value(this_word)}'")
