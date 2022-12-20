#! /usr/bin/python

from itertools import combinations

def makeReadableBoxes(matrixBoxes):
    """
    Takes Scrambled Partitions and returns a list of solve readable lists
    """

    returnMatrix = []

    for iBox in matrixBoxes:
        returnMatrix += interpreter(iBox)

    return returnMatrix


def interpreter(listBoxLetter: list) -> list:
    """
    Takes a list ('a','b','c','d','e','f','g','h'...)
    Returns a list ["abc","def","hij","klm"]
    that can be interpreted by solve.py
    """

    l = listBoxLetter
    returnList = [[l[0]+l[1]+l[2], l[3]+l[4]+l[5], l[6]+l[7]+l[8], l[9]+l[10]+l[11]]]

    return returnList


def makeScrambledPartition(stringAlphabet: str) -> list:
    """
    Partition a string into four substrings
    [ ['a','b','c', ...] , ... , ['d','f','g', ...]]
    """

    matrixBoxes = []
    listAlphabet = [*stringAlphabet]
    
    allCombinations = combinations(listAlphabet, 12)

    for combination in allCombinations:
        matrixBoxes += [combination]
   
    return matrixBoxes


def run():
    print(interpreter(('a','b','c','d','e','f','g','h','i','j','k','l')))
    return None

if __name__ == "__main__":
    run()
