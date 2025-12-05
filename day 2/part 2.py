#Advant of Code 2025 Day 2 Solution pt 2

file_name = r'C:\Users\Ediku\Escritorio\MISC\CS Programming\Personal Projects\Github\SimpleCaci\advent-of-code-2025\day 2\inputs.txt'
file = open(file_name, 'r')
list_of_inputs = []

pairs = []
for line in file.readlines():
    segments = line.strip().split(',')

    for seg in segments:
        a, b = map(int, seg.split('-'))
        pairs.append((a, b))


def getInvalidNumbersSum(input):
    total = 0
    a, b = input

    for num in range(a, b + 1):
        s = str(num)
        n = len(s)

        # Test all possible chunk sizes d
        for d in range(1, n // 2 + 1):
            if n % d != 0:
                continue

            chunk = s[:d]
            if chunk * (n // d) == s:
                total += num
                break   # No need to check other chunk sizes

    return total


total_sum = 0
for input in pairs:
    total_sum += getInvalidNumbersSum(input)

print("Total Sum of Invalid Numbers:", total_sum)