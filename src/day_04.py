from inputFiles import file_path as fp
from fastapi import APIRouter

# APIRouter creates path operations for item module
router = APIRouter(
    prefix="/AdventOfCode",
    tags=["Day 4"],
    responses={404: {"description": "Not found"}},
)

file = open(fp.file_path + 'day_04.txt', "r")
assignments = file.read().split()


@router.get("/day4/part1")
async def Solve_Part_One():
    return [
        {"result": solvePart1()}
    ]


@router.get("/day4/part2")
async def Solve_Part_Two():
    return [
        {"result": solvePart2()}
    ]


def solvePart1():
    score = 0
    for assignment in assignments:
        x, y = assignment.split(',')
        a, b = map(int, x.split('-'))
        c, d = map(int, y.split('-'))
        if a >= c and b <= d or a <= c and b >= d:
            score += 1
    return score


def solvePart2():
    score = 0
    for assignment in assignments:
        x, y = assignment.split(',')
        a, b = map(int, x.split('-'))
        c, d = map(int, y.split('-'))
        if not (b < c or d < a):
            score += 1
    return score
