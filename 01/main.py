INPUT = "input.txt"
SAMPLE = "sample.txt"
SAMPLE2 = "sample2.txt"
SAMPLE_PART1 = 142 # Add Results of part1 sample
SAMPLE_PART2 = 281 # Add Results of part2 sample

NUMBERS = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

def first(line: str) -> str | None:
    for i, c in enumerate(line):
        if c.isdigit():
            return c

def last(line: str) -> str | None:
    for i, c in enumerate(line[::-1]):
        if c.isdigit():
            return c

def convertL2R(line: str) -> str:
    newline = ""
    for char in line:
        newline += char
        for i, num in enumerate(NUMBERS):
            if num in newline:
                newline = newline.replace(num, str(i+1))
    return newline

def convertR2L(line: str) -> str:
    newline = ""
    for char in line[::-1]:
        newline += char
        for i, num in enumerate(NUMBERS):
            if num[::-1] in newline:
                newline = newline.replace(num[::-1], str(i+1))
    return newline[::-1]

def part1(filename: str) -> int:
    # ADD PART1 HERE
    sum = 0
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            number = first(line) or exit(1)
            number += last(line) or exit(1)
            sum += int(number)
    return sum

def part2(filename):
    # ADD PART2 HERE
    sum = 0
    with open(filename, "r") as f:
        for line in f.readlines():
            line_l2r = convertL2R(line.strip())
            line_r2l = convertR2L(line.strip())
            number = first(line_l2r) or exit(1)
            number += last(line_r2l) or exit(1)
            sum += int(number)
    return sum

def test_part1():
    assert part1(SAMPLE) == SAMPLE_PART1

def test_part2():
    assert part2(SAMPLE2) == SAMPLE_PART2

def main():
    print(f"part 1: {part1(INPUT)}")
    print(f"part 2: {part2(INPUT)}")


if __name__ == "__main__":
    main()
