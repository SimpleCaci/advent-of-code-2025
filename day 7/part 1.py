file_name = r'C:\Users\Ediku\Escritorio\MISC\CS Programming\Personal Projects\Github\SimpleCaci\advent-of-code-2025\day 7\input.txt'

with open(file_name) as file:
    manifold = [list(line.strip()) for line in file]

#set up layer 1
currentLayer = manifold[0]
#replace the S first
i = currentLayer.index("S")
currentLayer[i] = "|"

splitCount = 0
for layer in manifold:
    for i in range(len(layer)):
        if currentLayer[i] == "|":
            if layer[i] == "^":
                splitCount += 1
                try:
                    currentLayer[i+1] = "|"
                except:
                    pass
                try:
                    currentLayer[i-1] = "|"
                except:
                    pass
                currentLayer[i] = "."

print("".join(currentLayer))
print("Total Splits:", splitCount)