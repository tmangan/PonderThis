#! /usr/bin/python


def wordsReducer(sidedBox: list[str], entireWords: list[str]) -> str:
    """
    Takes the entire dictionary, and removes all words that contain 
    letters not in the available letters category
    """

    ### Initialize parameters:
    cAlphabet = "abcdefghijklmnopqrstuvwxyz"
    nonAvailableLetters = cAlphabet
    lettersBox = str()
    usefulWords = list()
    matrixTruths = dict()

    ### Combine sides of box into one list
    # TODO list comp
    for iSide in sidedBox:
        lettersBox += iSide

    ### Create a list of letters that are not used in the puzzle
    # TODO list comp
    for iLetter in lettersBox:
        if iLetter in cAlphabet:
            nonAvailableLetters =  nonAvailableLetters.replace(iLetter, "")

    ### Initialize Truth Matrix with "word":list(empty)
    for iWord in entireWords:
        matrixTruths[iWord] = True

    ### Verify truth matrix for each word
    ### False if prohibited letter appears in word
    for dictWord in matrixTruths:
        for iLetter in nonAvailableLetters:
            if iLetter in dictWord:
                matrixTruths.update({dictWord:False})

    ### Remove words that contain a prohibited letter from dictionary
    #
    for dictWord in matrixTruths:
        if matrixTruths[dictWord]:
            usefulWords += [dictWord] 

    return usefulWords


def initializeDictionary() -> list[str]:
    """
    Takes the words.txt file, opens it, and assigns it to a list called entireWords 
    """
        
    words = open("/usr/share/dict/american-english", "r")
    #words = open("words", "r")
    entireWords = list()

    ### Make the words list easier to use
    # TODO list comp
    for iWord in words:
        if len(iWord.strip()) > 2:
            entireWords += [iWord.strip().lower()]

    return entireWords
        

def removeUnwantedCharacter(usefulWords: list[str]) -> list[str]:
    """
    Removes words with weird characters from usefulWords 
    """

    returnWords = []
    for iWord in usefulWords:
        if not "'" in iWord:
            returnWords += [iWord]

    return returnWords


def openTwoWordSolutions() -> list[str]:
    """
    Opens AnswerBoxes_00 and gives as a list of strings
    ["asdfhjkasdfhjk","asdjfklasdh", ...]
    """
    
    rawBoxes = open("AnswerBoxes_00", "r")
    twoSolveBoxes = list()

    for iBox in rawBoxes:
        twoSolveBoxes += [iBox.strip()]
    
    return twoSolveBoxes


def run():
    return None


if __name__ == "__main__":
    run()
