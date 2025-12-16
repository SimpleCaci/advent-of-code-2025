# Advent of Code 2025 - Day 4, Part 1
#file_name = r'C:\Users\Ediku\Escritorio\MISC\CS Programming\Personal Projects\Github\SimpleCaci\advent-of-code-2025\day 6\testInput.txt'
file_name = r'C:\Users\Ediku\Escritorio\MISC\CS Programming\Personal Projects\Github\SimpleCaci\advent-of-code-2025\day 6\input.txt'

with open(file_name) as file:
    mathHW = [list(line) for line in file]

#print(mathHW)
column = len(mathHW[0]) - 1 - 1 #to avoid the newline character at the end and to get the last column index before the /n
equationList = []
while (column >= 0):
    equationString = ""
    for line in mathHW:
        equationString += line[column]   
    equationList.append(equationString)

    column -= 1
grandTotal = 0
op = ""
for eq in reversed(equationList):
    if (op == ""):
        op = eq[-1]  #operation to perform
        result = 1 if op == "*" else 0

    if (eq.strip() != ""): #if it isnt empty
        if op == "*":
            result *= int(eq.rstrip("*+"))
        elif op == "+":
            result += int(eq.rstrip("*+"))
        print(f"Equation: {eq}")
    else:
        op = "" #reset operation for next equation"
        grandTotal += result
        print(f"Result: {result}")

grandTotal += result
print(f"Result: {result}")

print (grandTotal)