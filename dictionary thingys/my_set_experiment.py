from binary_search import binary_search
from time import time_ns


class WordList_NoOptimization:
    def __init__(self, filename):
        """Reads words from filename and stores them"""
        fh = open(filename, "r")
        self._list = [line for line in map(str.strip, fh)]
        fh.close()

    def __contains__(self, value) -> bool:
        """
        function that allows this class to use:

        all_words = WordList_NoOptimization("wordlist.txt")
        if word in all_words:
        """

        for innerList in self._list:
            if value in innerList:
                return True
            else:
                return False


class WordList_BinarySearch:
    def __init__(self, filename):
        """Reads words from filename and stores them"""
        fh = open(filename, "r")
        self._list = [line for line in map(str.strip, fh)]
        self._list.sort()
        fh.close()

    def __contains__(self, value) -> bool:
        """
        function that allows this class to use:

        all_words = WordList_BinarySearch("wordlist.txt")
        if word in all_words:
        """

        index: int = binary_search(self._list, 0, len(self._list) - 1, value)
        return index is not None


class WordList_WithHash:
    def __init__(self, filename):
        """Reads words from filename and stores them"""

        fh = open(filename, "r")
        self.number_buckets: int = 1 << 5

        self._set = [[] for _ in range(self.number_buckets)]
        for word in map(str.strip, fh):
            index: int = self._hash(word)
            self._set[index].append((word, ''))

        fh.close()

    def _hash(self, key: str) -> int:
        """convert key into an integer"""
        h: int = 0
        for c in key:
            h = h * 10 + (ord(c) - ord("a"))

        return h % self.number_buckets

    def __contains__(self, value: str):
        """
        function that allows this class to use:

        all_words = WordList_WithHash("wordlist.txt")
        if word in all_words:
        """

        index: int = self._hash(value)
        return value in self._set[index]



# =============================================================================
# time it
# =============================================================================
if __name__ == "__main__":
    print(f"{'init':>10}   "
          f"{'search':>10}   "
          f"{'total':>10}   "
          "class")

    for search_class in (
            #WordList_NoOptimization,
            WordList_BinarySearch,
            WordList_WithHash,
    ):
        fh_words_to_find = open("words_to_find.txt", "r")

        now_all = time_ns()
        all_words = search_class("wordlist.txt")
        contained = 0
        setup_time = (time_ns() - now_all) / 1_000_000_000

        now_search_only = time_ns()
        for word in map(str.strip, fh_words_to_find):
            if word in all_words:
                contained += 1
        total_time = (time_ns() - now_all) / 1_000_000_000
        search_time = (time_ns() - now_search_only) / 1_000_000_000
        print(f"{setup_time:10.5f}   "
              f"{search_time:10.5f}   "
              f"{total_time:10.5f}   "
              f"{search_class.__name__}")
