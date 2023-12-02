MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

result = 0

games = []

lines = []
with open('input.txt', 'r') as f:
    lines = f.readlines()

for line in lines:
    line = line.replace("\n", "")

    game_id = line[5:line.find(": ")]
    game_values = line[line.find(": ")+2:]
    game_obj = { "id": game_id, "sets": [], "valid": True }
    for set in game_values.split("; "):
        game_set = { "red": 0, "green": 0, "blue": 0, "valid": True }
        for value in set.split(", "):
            nb = int(value.split(" ")[0])
            color = value.split(" ")[1]
            color_max = MAX_RED if color == "red" else MAX_GREEN if color == "green" else MAX_BLUE
            game_set[color] = nb
            game_set["valid"] = game_set["valid"] and nb <= color_max 
        game_obj["sets"].append(game_set)

    for s in game_obj["sets"]:
        game_obj["valid"] = game_obj["valid"] and s["valid"]
    games.append(game_obj)

valid_games = list(filter(lambda x: x["valid"] == True, games))
for g in valid_games:
    result += int(g["id"])
print(result)