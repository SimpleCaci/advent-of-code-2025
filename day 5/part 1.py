#Advent of Code Day 5, Part 1
#this reminds me of the previous days where we had to parse a range
#so I will start from there
file_name = r'C:\Users\Ediku\Escritorio\MISC\CS Programming\Personal Projects\Github\SimpleCaci\advent-of-code-2025\day 5\input.txt'
#file_name = r'C:\Users\Ediku\Escritorio\MISC\CS Programming\Personal Projects\Github\SimpleCaci\advent-of-code-2025\day 5\testInputs.txt'

file = open(file_name, 'r')

pairs = [] #fresh ingredient ID ranges
list_of_inputs = [] #avaliable ingredients IDs
isAfterSpace = False
for line in file.readlines():
    segments = line.strip().split('\n')

    for seg in segments:
        if (seg == ""):
            isAfterSpace = True
            continue  # skip empty segments

        if not (isAfterSpace):
            a, b = map(int, seg.split('-'))
            pairs.append((a, b))
        else: #after the space
            if seg.isdigit():
                list_of_inputs.append(int(seg))
            else:
                print("Invalid Input:", seg)
                continue  # skip invalid inputs


#count fresh ingredients
freshCount = 0
for avaliableIngredientId in list_of_inputs:
    for ingredientRange in pairs:
        if (ingredientRange[0] <= avaliableIngredientId <= ingredientRange[1]):
            print(f"Ingredient ID {avaliableIngredientId} is within range {ingredientRange}")
            freshCount += 1
            break #to avoid double counting

print("Total Fresh Ingredients:", freshCount)