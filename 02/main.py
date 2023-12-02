INPUT = "input.txt"
SAMPLE = "sample.txt"
SAMPLE_PART1 = 8 # Add Results of part1 sample
SAMPLE_PART2 = 2286 # Add Results of part2 sample
R, G, B = 12, 13, 14

def rgb(set):
    cubes = set.split(", ")
    r, g, b = 0, 0, 0
    for cube in cubes:
        match cube.split(" "):
            case [n, "red"]:
                r = int(n)
            case [n, "green"]:
                g = int(n)
            case [n, "blue"]:
                b = int(n)
    return r, g, b

def isValid(sets):
    valid = True
    for st in sets:
        vals = rgb(st)
        if vals[0] > R or vals[1] > G or vals[2] > B:
            valid = False
    return valid

def getData(line):
    data = line.strip().split(": ")
    game_id = int(data[0].split(" ")[1])
    sets = data[1].split("; ")
    return game_id, sets

def getMinimum(sets):
    r, g, b = 0, 0, 0
    for st in sets:
        cubes = st.split(", ")
        for cube in cubes:
            match cube.split(" "):
                case [n, "red"]:
                    if int(n) > r:
                        r = int(n)
                case [n, "green"]:
                    if int(n) > g:
                        g = int(n)
                case [n, "blue"]:
                    if int(n) > b:
                        b = int(n)
    return r, g, b

def part1(filename):
    # ADD PART1 HERE
    sum = 0
    with open(filename, "r") as f:
        for line in f.readlines():
            game_id, sets = getData(line)
            if isValid(sets):
                sum += game_id
    return sum

def part2(filename):
    # ADD PART2 HERE
    sum = 0
    with open(filename, "r") as f:
        for line in f.readlines():
            game_id, sets = getData(line)
            r, g, b = getMinimum(sets)
            power = r*g*b
            sum += power
    return sum

def test_part1():
    assert part1(SAMPLE) == SAMPLE_PART1

def test_part2():
    assert part2(SAMPLE) == SAMPLE_PART2

def main():
    print(f"part 1: {part1(INPUT)}")
    print(f"part 2: {part2(INPUT)}")


if __name__ == "__main__":
    main()
