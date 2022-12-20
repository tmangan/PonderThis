#! /usr/bin/python


def solutionOneChecker(combinedLetters: str, testWord: str, dictWordScores: dict) -> bool:
    """
    Check if a word uses all letters of the box 
    True = Valid Solution
    """

    fullScore = len(combinedLetters)
    #fullScore = 7

    if dictWordScores[testWord] > fullScore:
        return True
    return False


def topScoringWords(combinedLetters: str, dictWordScores: dict) -> bool:
    """
    Prints the top scoring words above or equal to 8 points
    """

    fullScore = len(combinedLetters)
    for iScore in range(fullScore, 7, -1):
        for iWord in dictWordScores:
            if dictWordScores[iWord] == iScore:
                print(iWord, iScore)

    return True


def run():
    return None


if __name__ == "__main__":
    run()
