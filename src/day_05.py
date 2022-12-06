from inputFiles import file_path as fp
from fastapi import APIRouter

# APIRouter creates path operations for item module
router = APIRouter(
    prefix="/AdventOfCode",
    tags=["Day 5"],
    responses={404: {"description": "Not found"}},
)

file = open(fp.file_path + 'day_05.txt', "r")
parts = file.read()[:-1].split('\n\n')

cratesStack = parts[0].split('\n')
moves = parts[1].split('\n')

# prepare stacks
numberOfStacks = int(cratesStack[len(cratesStack) - 1][-2])
maxHeightOfStack = len(cratesStack) - 1
stacks = [[] for _ in range(numberOfStacks)]
for i in range(maxHeightOfStack):
    line = cratesStack[i]
    crates = line[1::4]
    for s in range(len(crates)):
        if crates[s] != " ":
            stacks[s].append(crates[s])
stacks = [stack[::-1] for stack in stacks]


@router.get("/day5/part1")
async def Solve_Part_One():
    return [
        {"result": solvePart1()}
    ]


@router.get("/day5/part2")
async def Solve_Part_Two():
    return [
        {"result": solvePart2()}
    ]


def solvePart1():
    for move in moves:
        moveSplit = move.split(" ")
        number = int(moveSplit[1])
        stackFrom = int(moveSplit[3])
        stackTo = int(moveSplit[5])

        for n in range(number):
            elem = stacks[stackFrom - 1].pop()
            stacks[stackTo - 1].append(elem)
    res = [stack[-1] for stack in stacks]
    result = ""
    for stack in stacks:
        result += stack[-1]
    return result


def solvePart2():
    for move in moves:
        moveSplit = move.split(" ")
        number = int(moveSplit[1])
        stackFrom = int(moveSplit[3])
        stackTo = int(moveSplit[5])
        temp = []
        for n in range(number):
            temp.append(stacks[stackFrom - 1].pop())
        for x in temp[::-1]:
            stacks[stackTo - 1].append(x)
    result = ""
    for stack in stacks:
        result += stack[-1]

    return result
