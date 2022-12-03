from inputFiles import file_path as fp
from fastapi import APIRouter

# APIRouter creates path operations for item module
router = APIRouter(
    prefix="/AdventOfCode",
    tags=["Day 2"],
    responses={404: {"description": "Not found"}},
)

file = open(fp.file_path + 'day_02.txt', "r")
moves = file.read().split("\n")


@router.get("/day2/part1")
async def Solve_Part_One():
    return [
        {"result": solvePart1()}
    ]


@router.get("/day2/part2")
async def Solve_Part_Two():
    return [
        {"result": solvePart2()}
    ]


def solvePart1():
    matchResults = {"AX": 3, "BX": 0, "CX": 6,
                    "AY": 6, "BY": 3, "CY": 0,
                    "AZ": 0, "BZ": 6, "CZ": 3}
    scorePoints = {"X": 1, "Y": 2, "Z": 3}
    score = 0

    for move in moves:
        score += scorePoints[move.split()[1]]
        score += matchResults[move.replace(" ", '')]
    return score


def solvePart2():
    scorePoints = {"AX": 3, "BX": 1, "CX": 2,
                   "AY": 1, "BY": 2, "CY": 3,
                   "AZ": 2, "BZ": 3, "CZ": 1}
    matchResults = {"X": 0, "Y": 3, "Z": 6}
    score = 0

    for move in moves:
        score += matchResults[move.split()[1]]
        score += scorePoints[move.replace(" ", '')]
    return score
