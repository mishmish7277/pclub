def FindLongestWord(str):
    str += ' '
    max = 0
    count = 0
    word = ''
    maxWord =""
    for i in str:
        if i != " ":
            count += 1
            word += i
        else:
            if (count > max):
                max = count
                count = 0
                maxWord = word
                word = ''
    print(maxWord)


