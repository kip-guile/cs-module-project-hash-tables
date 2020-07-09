def no_dups(s):
    # Your code here
    newArr = []
    newArr.append(s)
    sArr = newArr[0].split()
    obj = {}
    newStr = ''
    for i in range(len(sArr)):
        obj[sArr[i]] = True
    for key in obj.keys():
        if newStr == '':
            newStr = newStr + str(key)
        else:
            newStr = newStr + ' ' + str(key)

    return newStr


if __name__ == "__main__":
    # print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
