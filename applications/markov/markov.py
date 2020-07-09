import random

# Read in all the words in one go
with open("applications/markov/input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
whitespace = '\n \t \r'.split(' ')

for i in whitespace:
    words = words.replace(i, ' ')

words.replace('  ', ' ')
startWord = ''
endWOrd = ''
next = {}
punctuation = [".", "?", "!"]

wordArr = words.split(' ')

for i in range(len(wordArr)):
    word = wordArr[i]

    if i == len(wordArr) - 2:
        break

    if i + 1 < len(wordArr):
        nextWord = wordArr[i + 1]

    if word not in next:
        next[word] = []

    next[word].append(nextWord)

    isStartWord = (word[0].isalpha() and word[0] == word[0].upper()) or (
        len(word) > 1 and word[0] == '"' and word[1].isalpha() and word[1] == word[1].upper())

    if isStartWord:
        startWord = word

    isEndWord = (word[-1] in punctuation) or (len(word) >
                                              1 and word[-1] == '"' and word[-2:-1] in punctuation)

    if isEndWord:
        endWord = word


# TODO: construct 5 random sentences
# Your code here
