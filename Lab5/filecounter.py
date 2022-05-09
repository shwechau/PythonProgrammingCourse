from print_me_first import *
print_me_time()

def counter(filename, lineList):
    fileContents = open(filename, "r")
    lineList = fileContents.readlines()
    lineCount = len(lineList)
    fileContents.close()
    wordCount = 0
    charCount = 0
    for line in lineList:
        outputLine = line.rstrip("\n")
        words = line.split()
        wordCount += len(words)
        for ch in outputLine:
            if ch:
                charCount += 1
    return(lineCount, wordCount, charCount, lineList)
def countandprint(noOfLines, noOfWords, noOfChar, lineList):
    count = 0
    charUpper = 0
    charLower = 0
    charSpace = 0
    charDigits = 0
    specialChars = [".", "!", "?"]
    charSentences = 0
    for line in lineList:
        outputLine = line.rstrip("\n")
        count += 1
        print("Line  {:3d} : {}".format(count, outputLine))

        for ch in outputLine:
            if ch.isupper():
                charUpper += 1
            if ch.islower():
                charLower += 1
            if ch.isspace():
                charSpace += 1
            if ch.isdigit():
                charDigits += 1
            if ch in specialChars:
                charSentences += 1
    print("Total number of lines: {:5d}".format((noOfLines)))
    print("Total number of words: {:5d}".format(noOfWords))
    print("Total number of characters: {:5d}".format(noOfChar))
    print("Total number of uppercase letters: {:5d}".format(charUpper))
    print("Total number of lowercase letters: {:5d}".format(charLower))
    print("Total number of spaces: {:5d}".format(charSpace))
    print("Total number of digits: {:5d}".format(charDigits))
    print("Total number of sentences: {:5d}".format(charSentences))


fileName = "test.txt"
lineList = []

(noOfLines, noOfWords, noOfChar, lineList) = counter(fileName,lineList)

countandprint(noOfLines, noOfWords, noOfChar, lineList)


