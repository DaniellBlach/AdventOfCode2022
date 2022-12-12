from inputFiles import file_path as fp
from fastapi import APIRouter

# APIRouter creates path operations for item module
router = APIRouter(
    prefix="/AdventOfCode",
    tags=["Day 8"],
    responses={404: {"description": "Not found"}},
)

file = open(fp.file_path + 'day_08.txt', "r")
input = file.read()
formattedInput = [list(x) for x in input.split('\n')]


@router.get("/day8/part1")
async def Solve_Part_One():
    return [
        {"result": solvePart1()}
    ]


@router.get("/day8/part2")
async def Solve_Part_Two():
    return [
        {"result": solvePart2()}
    ]


def solvePart1():
    x = len(formattedInput)
    y = len(formattedInput[0])
    result = 0
    for i in range(0, x):
        for j in range(0, y):
            column = [formattedInput[y][j] for y in range(x)]

            if i == 0 or i == x - 1 or j == 0 or j == y - 1:  # BORDER
                result += 1
                continue

            if formattedInput[i][0:j] and max(formattedInput[i][0:j]) < formattedInput[i][j]:  # LEFT
                result += 1
                continue

            if formattedInput[i][j + 1:x] and max(formattedInput[i][j + 1:x]) < formattedInput[i][j]:  # RIGHT
                result += 1
                continue

            if column[i + 1:y] and max(column[i + 1:y]) < formattedInput[i][j]:  # BOTTOM
                result += 1
                continue

            if column[0:i] and max(column[0:i]) < formattedInput[i][j]:  # TOP
                result += 1
                continue
    return result


def solvePart2():
    x = len(formattedInput)
    y = len(formattedInput[0])
    maxValue = 0
    for i in range(x):
        for j in range(y):
            #RIGHT
            rightR = 0
            z = j
            while True:
                if z == y - 1:
                    break
                rightR += 1
                if formattedInput[i][j] <= formattedInput[i][z + 1]:
                    break
                z += 1
            #LEFT
            leftR = 0
            z = j
            while True:
                if z == 0:
                    break
                leftR += 1
                if formattedInput[i][j] <= formattedInput[i][z - 1]:
                    break
                z -= 1

            column = [formattedInput[q][j] for q in range(x)]
            #TOP
            topR = 0
            z = i
            while True:
                if z == 0:
                    break
                topR += 1
                if formattedInput[i][j] <= column[z - 1]:
                    break
                z -= 1

            #BOTTOM
            bottomR = 0
            z = i
            while True:
                if z == x - 1:
                    break
                bottomR += 1
                if formattedInput[i][j] <= column[z + 1]:
                    break
                z += 1

            value = leftR * rightR * topR * bottomR
            if value > maxValue:
                maxValue = value


    return maxValue
