#! /usr/bin/python

from Scorer import *


def opposingSides(allSides: list[str]) -> dict:
    """
    Finds the other sides (available letters) and combines them into one string
    {
    "hou":"wcrtkanbl",
    "wcr":"houtkanbl",...
    }
    """
    
    dictOpposingSides = dict()

    for iSide in allSides:
        tempSide = ""
        for jSide in allSides:
            if iSide != jSide:
                tempSide += jSide
        dictOpposingSides[iSide] = tempSide

    return dictOpposingSides


def sameSideChecker(sidedBox: list[str], testLetterIndex: int, testWord: str) -> bool:
    """
    Checks if the next letter is on the same side as the initial letter 
    True = next letter is on the same side!!
    """

    ### Locates the same side of the testLetter
    # TODO list comprehension
    testLetter = testWord[testLetterIndex]
    nextTestLetter = testWord[testLetterIndex + 1]
    sameSideLetters = str()
    for iSide in sidedBox:
        if testLetter in iSide:
            sameSideLetters = iSide

    if nextTestLetter in sameSideLetters:
        return True 
    return False


def lastLetterChecker(testLetterIndex: int, testWord: str) -> bool:
    """
    Checks if the test letter is the last letter 
    True = Last letter 
    """

    if testLetterIndex + 1 == len(testWord):
        return True
    return False


def playableCheck(testWord: str, sidedBox: list[str]) -> bool:
    """
    Tests if a word has all crossing letters; a playable word 
    True = Playable
    """
    
    for idxLetter, iLetter in enumerate(testWord):
        if lastLetterChecker(idxLetter, testWord):
            return True
        if sameSideChecker(sidedBox, idxLetter, testWord):
            return False


def wordCombiner(combinedLetters: str, playableWords: list[str]) -> bool:
    """
    Combines n words (starting with two) into a single playable 
    """

    maxScore = len(combinedLetters)
    dictTwoSolves = []

    for iWord in playableWords:
        for jWord in playableWords:
            if iWord[-1] == jWord[0] and scoreValue(iWord + jWord) >= maxScore:
                dictTwoSolves += [[iWord, jWord]]

    return dictTwoSolves


def main():
    return None

if __name__ == "__main__":
    main()
