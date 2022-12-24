#! /usr/bin/python

from Prettier import *
from Solution_Checker import *
from Words_List_Prep import *
from Scorer import *
from Word_Processor import *
from Box_Maker import *


def main():
    """
    Main IBM Puzzle
    find boxes that have between 2 and 5 solutions
    """

    ### Intro Box Text
    introPrinter()

    ### Start a recording text file for boxes that are good
    f = open("AnswerBoxes", "w")

    ### Creates a list of possible boxes
    # matrixBoxes = all possible boxes
    # abcdefghijklmnopqrstuvwxyz
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    matrixBoxes = makeReadableBoxes(makeScrambledPartition(alphabet))

    ### Loop through Boxes and print if there is exactly one solution
    for iSidedBox in matrixBoxes:
        solutions = solve(iSidedBox)
        if solutions == 1:
            message = str(iSidedBox) + "\n"
            print(message)
            f.write(message)

    ### Close text file when Done
    f.close()

    ### Outro Box Line
    outroPrinter()

    return None


def solve(sidedBox):
    """
    Main solution initiator
    """

    ### Initialize entry parameters:
    combinedLetters = str()
    for iSide in sidedBox:
        combinedLetters += iSide
    nSides = len(sidedBox)
        
    ### Make set of useful words specific to Box
    entireWords = initializeDictionary()
    usefulWords = wordsReducer(sidedBox, entireWords)
    usefulWords = removeUnwantedCharacter(usefulWords)

    ### Make list of Playable Words from usefulWords
    # EntireWords = all words in word list
    # UsefulWords = words that have all letters from box
    # PlayableWords = words that can actually be played in game
    playableWords = list()
    for iWord in usefulWords:
        if playableCheck(iWord, sidedBox):
            playableWords += [iWord]

    ### Scoring to optimize word choice
    # Make a dictionary of scores:
    dictWordScores = makeScoredWords(playableWords)
    
    ### TOGGLE FOR SOLUTION PRINTING
    ### Show top scoring words from scorer.py:
    #topScoringWords(combinedLetters, dictWordScores)

    ### Combine two words into new dictionary:
    dictTwoSolves =  wordCombiner(combinedLetters, playableWords)

    ### TOGGLE FOR SOLUTION PRINTING
    #for iTwoSolution in dictTwoSolves:
    #    print(iTwoSolution)

    ### Prints the number of TwoSolutions
    #print("Number of 2-Solves: ", len(dictTwoSolves))

    return dictTwoSolves 
    #return len(dictTwoSolves)


if __name__ == "__main__":
    sidedBox = ["tqy","rua","exw","nif"]
    print(solve(sidedBox))
    #main()


