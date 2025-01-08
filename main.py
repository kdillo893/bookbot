

def main():

    print(countWords("books/frankenstein.txt", None))

    print(countWords("books/frankenstein.txt", "Frankenstein"))

    charCount = countCharacters("books/frankenstein.txt")
    # raw printing
    # for key in charCount:
    #     print(f"The '{key}' character was found {charCount[key]} times")

    sorted = charDictToSortedList(charCount)
    for item in sorted:
        print(f"The '{item["char"]}' character was found {item["count"]} times")

    pass


def sortOn(d):
    return d["count"]


def charDictToSortedList(d):
    sorted = []
    for ch in d:
        sorted.append({"char": ch, "count": d[ch]})
    sorted.sort(reverse=True, key=sortOn)

    return sorted


def getFileText(filename):
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents


def countCharacters(filename):

    fileText = getFileText(filename).lower()
    charDict = {}

    for c in fileText:

        if not c.isalpha():
            continue

        if c not in charDict:
            charDict[c] = 1
        else:
            charDict[c] += 1

    return charDict


def countWords(filename, checkWord):
    fileText = getFileText(filename)

    words = fileText.split()

    if checkWord is not None:
        # remove words not matching, filter array
        words = list(filter(lambda word: checkWord == word, words))

    return len(words)


main()
