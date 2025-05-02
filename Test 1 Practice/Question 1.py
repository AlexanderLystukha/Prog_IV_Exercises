def prefixes(words: list[str]) -> dict:
    prefixes: dict = {}


    for word in words:
        old_smth: str = ""
        for letter in word:

            old_smth += letter

            if old_smth not in prefixes:
                prefixes[old_smth] = 1
            else:
                prefixes[old_smth] += 1

    return prefixes


print(prefixes(["abc", "ca", "cab"]))
