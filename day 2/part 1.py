#Advant of Code 2025 Day 2 Solution

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
    sum = 0
    print("Range:", input)
    for i in range(input[0], input[1] + 1):
        if (len(str(i)) % 2 == 1):
            #print("This Number Has Odd Digits Hence: Skipped")
            continue
        else:
            #print("This Number Has Even Digits Hence: Processed")
            mid = len(str(i)) // 2
            first_half = str(i)[:mid]
            second_half = str(i)[mid:]
            if (first_half == second_half):
                print(i)
                sum += i
    return sum

total_sum = 0
for input in pairs:
    total_sum += getInvalidNumbersSum(input)

print("Total Sum of Invalid Numbers:", total_sum)