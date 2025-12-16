#wrong answer (come back later)

#should jusst be the same plus multiplying each layers

file_name = r'C:\Users\Ediku\Escritorio\MISC\CS Programming\Personal Projects\Github\SimpleCaci\advent-of-code-2025\day 7\input.txt'

with open(file_name) as file:
    manifold = [list(line.strip()) for line in file]

currentLayer = manifold[0]
currentLayer[currentLayer.index("S")] = "|"

splitCount = 0
timeline = 1

for layer in manifold[1:]:
    nextLayer = ["." for _ in currentLayer]

    for i in range(len(layer)):
        if currentLayer[i] == "|":
            if layer[i] == "^":
                splitCount += 1
                timeline *= 2
                if i > 0:
                    nextLayer[i-1] = "|"
                if i < len(layer) - 1:
                    nextLayer[i+1] = "|"
            else:
                nextLayer[i] = "|"

    currentLayer = nextLayer

print("".join(currentLayer))
print("Total Splits:", splitCount)
print("Total Timelines:", timeline)
