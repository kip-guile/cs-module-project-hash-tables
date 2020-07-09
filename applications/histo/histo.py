# Your code here
from operator import itemgetter


def wordcount(s):
    words = s.lower()
    whitespace = '\n \t \r'.split(' ')
    for i in whitespace:
        words = words.replace(i, ' ')
    chars = '" : ; , . - + = / \ | [ ] ( ) { } * ^ &'.split(' ')
    for i in chars:
        words = words.replace(i, '')
    words.split(' ')
    seen = {}
    for word in words:
        if word == '':
            continue
        if word in seen:
            seen[word] += 1
        else:
            seen[word] = 1
    return seen


def histo(fpath):
    with open(fpath) as file:
        text = file.read()

    times = wordcount(text)

    tArray = times.items()
    tArray = sorted(tArray, key=itemgetter(1, 0), reverse=True)

    longestword = len(tArray[0][0])

    for t in tArray:
        if len(t[0]) > longestword:
            longestword = len(t[0])

    for t in tArray:
        formatted = t[0] + (longestword - len(t[0])) * ' '
        histobar = '#' * t[1]
        historow = formatted + '  ' + histobar

        print(historow)


histo("applications/histo/robin.txt")
