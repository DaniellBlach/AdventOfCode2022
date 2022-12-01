from fastapi import APIRouter

# APIRouter creates path operations for item module
router = APIRouter(
    prefix="/AdventOfCode",
    tags=["Advent of Code"],
    responses={404: {"description": "Not found"}},
)