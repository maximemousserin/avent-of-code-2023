import re

result = 0

lines = []
with open('input.txt', 'r') as f:
    lines = f.readlines()

for line in lines:
    line = re.sub("[^0-9]", "", line)
    
    justnumbers = re.sub("[^0-9]", "", line)
    number = int(justnumbers[0] + justnumbers[-1])

    result += number

print(result)
