#! /usr/bin/python


def scoreValue(scorableWord: str) -> int:
    """
    Returns an integer number of how many unique letters are in scorableWord 
    This is a good measure of which words to use in the puzzle
    """

    listWord = list()
    for iLetter in scorableWord:
        listWord += [iLetter]
    setWord = set(listWord)

    score = len(setWord)

    return score


def makeScoredWords(playableWords: list[str]) -> dict:
    """
    Returns a dictionary of words and their associated scores 
    """

    dictWordScores = dict()
    for iWord in playableWords: 
        dictWordScores[iWord] = scoreValue(iWord)

    return dictWordScores


def run():
    return None


if __name__ == "__main__":
    run()
