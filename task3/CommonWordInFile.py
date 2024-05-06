import sys
file = open(sys.argv[1],"r")
N = int(sys.argv[2])
words = file.read().split()
file.close()
wordsDict = dict()

for x in words:
    if x in wordsDict:
        wordsDict[x] = wordsDict[x] + 1
    else:
        wordsDict[x] = 1

sorted_words = [x[0] for x in sorted(wordsDict.items(), key=lambda x: x[1], reverse=True)]

for key in sorted_words[:N]:
    print("word '" + str(key) + "' " + str(wordsDict[key]) + " times")
   