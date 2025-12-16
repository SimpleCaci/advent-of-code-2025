# Advent of Code 2025 - Day 4, Part 1
#file_name = r'C:\Users\Ediku\Escritorio\MISC\CS Programming\Personal Projects\Github\SimpleCaci\advent-of-code-2025\day 6\testInput.txt'
file_name = r'C:\Users\Ediku\Escritorio\MISC\CS Programming\Personal Projects\Github\SimpleCaci\advent-of-code-2025\day 6\input.txt'

with open(file_name) as file:
    mathHW = [line.strip().split() for line in file]

lineNum =  1 #which line we are at
grandTotal = 0
for column in range(len(mathHW[0])):
    #print(column)
    op = mathHW[-1][column]  #operation to perform
    result = 1 if op == "*" else 0
    for line in mathHW:
        item = line[column]
        if (item != "+" and item != "*"):
            if op == "*":
                result *= int(item)
            elif op == "+":
                result += int(item)

    grandTotal += result
    #print(result)

print("Grand Total:", grandTotal)
#print(mathHW)


