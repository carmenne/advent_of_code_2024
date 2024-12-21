inputs = []
games = {}
with open("input.txt", "r") as file:
    for line in file:
        line_strip = line.strip()
        idx = line_strip.index(":")
        game = line_strip[idx + 2:]
        game_id = int(line_strip[:idx].replace("Game", "").strip())
        sets = game.replace("'", "").split(";")
        inputs.append(sets)

        parsed_set = []
        for game_set in sets:
            rbg = game_set.split(",")
            r, b, g = 0, 0, 0
            for bal in rbg:
                if "red" in bal:
                    r = int(bal.replace("red", "").strip())
                if "blue" in bal:
                    b = int(bal.replace("blue", "").strip())
                elif "green" in bal:
                    g = int(bal.replace("green", "").strip())
            parsed_set.append((r, b, g))
        games[game_id] = parsed_set


RED, GREEN, BLUE = 12, 13, 14
all_possible = 0
for game_id, game in games.items():
    game_possible = True

    for game_set in game:
        r,b,g = game_set
        if r > RED or b > BLUE or g > GREEN:
            game_possible = False
            break

    all_possible += game_id * game_possible

print(all_possible) # 2551
