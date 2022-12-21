#! /usr/bin/python

from Words_List_Prep import *
from solver import *

def boxify(twoSolve: str) -> list[str]:
    """
    interprets the string "abcdefghijkl" into ["abc","def","ghi","jkl"]
    """

    outgoing = []
    for side in [0,3,6,9]:
        outgoing += [twoSolve[side : side + 3]]

    return outgoing


def main():
    """
    prints the two-solve for each of the boxes imported from file
    """

    f = open("solutions", "w")

    twoSolves = openTwoWordSolutions()
    for solution in twoSolves:
        pSolution = solve(boxify(solution))
        L = solution + "  " + str(pSolution) + "\n"
        f.write(L)
        print(L)

    return None

if __name__ == "__main__":
    #print(boxify("abcdefghijkl"))
    main()
