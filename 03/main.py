from functools import reduce
from typing import ClassVar, List, Tuple
from math import sqrt
from operator import mul


INPUT, SAMPLE = "input.txt", "sample.txt"
SAMPLE_PART1, SAMPLE_PART2 = 4361, 467835 # Add Results of part1 and part2 sample

class Coords:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x, self.y = x, y

    def __repr__(self):
        return f"Coords{self.__str__()}"
    
    def __str__(self):
        return f"(x: {self.x}, y: {self.y})"

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Coords(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Coords(x, y)

    def norm(self):
        return sqrt(self.x*self.x + self.y*self.y)

class Symbol:
    value: str
    coords: Coords

    def __init__(self, value: str = "", coords: Coords = Coords(0, 0)):
        self.value, self.coords = value, coords

    def __repr__(self):
        return f"Symbol({self.__str__()})"

    def __str__(self):
        return f"value: {self.value}, coords: {self.coords}"

class Number:
    value: int
    coords: List[Coords]

    def __init__(self):
        self.value = 0
        self.coords = []

    def __repr__(self):
        return f"Number({self.__str__()})"

    def __str__(self):
        return f"value: {self.value}, coords: {self.coords}"

    def isCloseTo(self, other:Coords) -> bool:
        for coord in self.coords:
            if (coord - other).norm() < 2:
                return True
        return False

def getNumberCoords(lines: List[str]) -> List[Number]:
    coords = []
    nums = []
    num = Number()
    isNumber = False
    for j, line in enumerate(lines):
        for i, c in enumerate(line):
            if c.isdigit() and not isNumber:
                isNumber = True
                coords.append(Coords(i, j))
            elif c.isdigit() and isNumber:
                coords.append(Coords(i, j))
            elif not c.isnumeric() and isNumber:
                isNumber = False
                num.value = int(line[coords[0].x:coords[-1].x + 1])
                num.coords = coords
                nums.append(num)
                coords = []
                num = Number()
    return nums

def getSymboCoords(lines: List[str]) -> List[Symbol]:
    sym = []
    for j, line in enumerate(lines):
        for i, c in enumerate(line):
            if c.isprintable() and not (c.isnumeric() or c == "."):
                sym.append(Symbol(c, Coords(i, j)))
    return sym

def part1(filename):
    # ADD PART1 HERE
    includedNums = []
    with open(filename, "r") as f:
        lines = f.readlines()
        nums = getNumberCoords(lines)
        syms = getSymboCoords(lines)
        for num in nums:
            for sym in syms:
                if num.isCloseTo(sym.coords):
                    includedNums.append(num)
    return sum(map(lambda n: n.value, includedNums))

def part2(filename):
    # ADD PART2 HERE
    gears: List[List[Number]] = []
    with open(filename, "r") as f:
        lines = f.readlines()
        nums = getNumberCoords(lines)
        syms = getSymboCoords(lines)
        for sym in syms:
            if sym.value == "*":
                ratios = []
                for num in nums:
                    if num.isCloseTo(sym.coords):
                        ratios.append(num)
                if len(ratios) == 2:
                    gears.append(ratios)
    return sum(map(lambda ratios: reduce(mul, list(map(lambda ratio:ratio.value, ratios))), gears))

def test_part1():
    assert part1(SAMPLE) == SAMPLE_PART1

def test_part2():
    assert part2(SAMPLE) == SAMPLE_PART2

def main():
    print(f"part 1: {part1(INPUT)}")
    print(f"part 2: {part2(INPUT)}")


if __name__ == "__main__":
    main()
