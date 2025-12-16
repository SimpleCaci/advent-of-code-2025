#Advent of Code 2025 - Day 5, Part 2

#it's simple to just think of brute forcing
#creating a hash set of avaliable ingredients
#using the set() function for O(1) lookup time
#however this requires that we add each number in all the range
#it might be more efficient to just combine the ranges
#then, using part 1 logic, we can count how many ingredients are fresh

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

#in this case, we wouldn't need to worry about the list_of_inputs having duplicates

#combine the ranges
pairs.sort()  # sort ranges by starting point
combined_ranges = []
#an for loop by range might be better but
#it feels more clean to have a seperate index
#after consideration, index is still needed but to track the combined_ranges list

index = 0
for current in pairs:
    if not combined_ranges: #  first range
        combined_ranges.append(current)
        previousRange = current
        index = 1
        continue
        #print("First Range Added:", current)

    else:
        if (previousRange[1] >= current[0]-1): #overlapping
            try:
                #print("attempting to combine:\032", previousRange, "and", current)
                combined_ranges[index-1] = (previousRange[0], max(previousRange[1],current[1])) #FIXME: this only works if current is fully inside previousRange
                #print("no issue with combining")
                previousRange = combined_ranges[index-1]
                #print("Combined Range:\032", combined_ranges[index-1])
            except IndexError:
                print ("\030Index Error at Index:\032", index-1)
                #print("\031Previous Range:\032", previousRange )
                #print ("\032Current Range:\032", current)
                #print ("list of combined ranges:\032", combined_ranges)
        else:
            combined_ranges.append(current)
            previousRange = current
            index += 1 #index was tracking the wrong list
        #print("Combined Ranges So Far:", combined_ranges)

#count fresh ingredients
sumIngredientIDs = 0
for ranges in combined_ranges:
    sumIngredientIDs += ranges[1] - ranges[0] + 1 #inclusive range

print("Total Sum of Fresh Ingredient IDs:", sumIngredientIDs)