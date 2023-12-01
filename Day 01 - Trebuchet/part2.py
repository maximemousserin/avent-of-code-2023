numberWords = { "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9" }

result = 0

lines = []
with open('input.txt', 'r') as f:
    lines = f.readlines()

for line in lines:
    line = line.replace("\n", "")

    lineNumbers = []
    # pour chaque caractère
    for i, c in enumerate(line):
        # on checke si c'est un chiffre        
        if c.isdigit():
            lineNumbers.append(c)
        
        for numberWord in numberWords:
            # on checke si la ligne (en partant de l'index du caractère en cours) commence par un chiffre écrit en lettre
            if line[i:].startswith(numberWord):
                lineNumbers.append(numberWords[numberWord])

    result += int(lineNumbers[0] + lineNumbers[-1])

print(result)