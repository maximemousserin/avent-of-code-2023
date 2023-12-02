result = 0

games = []

lines = []
with open('input.txt', 'r') as f:
    lines = f.readlines()

for line in lines:
    line = line.replace("\n", "")

    game_id = line[5:line.find(": ")]
    game_values = line[line.find(": ")+2:]
    game_obj = { "id": game_id, "max": { "red": 0, "green": 0, "blue": 0 }, "power": 0 }
    for set in game_values.split("; "):
        game_set = { "red": 0, "green": 0, "blue": 0, "valid": True }
        for value in set.split(", "):
            nb = int(value.split(" ")[0])
            color = value.split(" ")[1]
            game_obj["max"][color] = nb if nb > game_obj["max"][color] else game_obj["max"][color]

    game_obj["power"] = game_obj["max"]["red"] * game_obj["max"]["green"] * game_obj["max"]["blue"] 
    games.append(game_obj)

for g in games:
    result += int(g["power"])

print(result)