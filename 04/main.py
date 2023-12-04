from typing import List, Tuple


INPUT = "input.txt"
SAMPLE = "sample.txt"
SAMPLE_PART1 = 13 # Add Results of part1 sample
SAMPLE_PART2 = 30 # Add Results of part2 sample

def getNumbers(line: str) -> Tuple[int, List[int], List[int]]:
    [card, numbers] = line.replace("   ", " ").replace("  ", " ").split(": ")
    card = int(card.split(" ")[1])
    [winning, owned] = numbers.split(" | ")
    winning = list(map(lambda n: int(n), winning.strip().split(" ")))
    owned = list(map(lambda n: int(n), owned.strip().split(" ")))
    return card, winning, owned
    

def part1(filename):
    # ADD PART1 HERE
    sum = 0
    with open(filename, "r") as f:
        for line in f.readlines():
            card, winning, owned = getNumbers(line)
            score = 0
            for n in owned:
                if n in winning:
                    if score == 0:
                        score += 1
                    else:
                        score *= 2
            sum += score
    return sum

def part2(filename):
    # ADD PART2 HERE
    cards = []
    with open(filename, "r") as f:
        lines = f.readlines()
        cards = [1 for i in range(len(lines))]
        for line in lines:
            card, winning, owned = getNumbers(line)
            cards_won = 0
            for n in owned:
                if n in winning:
                    cards_won += 1
            for i in range(cards_won):
                cards[card+i] += cards[card-1]
    return sum(cards)

def test_part1():
    assert part1(SAMPLE) == SAMPLE_PART1

def test_part2():
    assert part2(SAMPLE) == SAMPLE_PART2

def main():
    print(f"part 1: {part1(INPUT)}")
    print(f"part 2: {part2(INPUT)}")


if __name__ == "__main__":
    main()
