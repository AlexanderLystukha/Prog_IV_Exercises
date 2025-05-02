import sys


def word_count(texts: list[str]) -> dict:
    word_dic: dict = {}

    # TODO modify as needed
    for text in texts:
        fh = open(text)
        for line in map(str.strip, fh):
            for word in line.lower().split():
                word = word.strip('"!“”#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ ')

                if word not in word_dic:
                    word_dic[word] = 1
                else:
                    word_dic[word] = word_dic[word] + 1
        fh.close()

    return word_dic


def main(texts: list[str]):
    words: dict = generating_text(texts)
    # TODO

    for k, v in words.items():
        print(f'{k}, {v}')


def generating_text(texts: list[str]) -> dict:
    words: dict = {}
    word1: str = None
    word2: str = None
    word3: str = None


    for text in texts:
        fh = open(text)
        for line in map(str.strip, fh):
            for word in line.lower().split():
                word = word.strip('"!“”#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ ')

                word1, word2, word3 = word2, word3, word

                if (word1, word2) not in words:
                    words[(word1, word2)] = []

                words[(word1, word2)].append(word3)

        fh.close()

    return words


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        main(["pg1497.txt"])
