"""imposter"""
import json
def main():
    """main"""
    players = {}
    dead_players = {}
    while True:
        line = input().strip()
        if line == "Start":
            break
        if line:
            player_dict = json.loads(line)
            players.update(player_dict)
    while True:
        line = input().strip()
        if line == "End":
            break
        if line:
            dead_name = line
            if dead_name in players:
                role = players.pop(dead_name)
                dead_players[dead_name] = role
    impostor_remains = list(players.values()).count("Impostor")
    print(f"{impostor_remains} Impostor Remains")
    print("***Alive***")
    for name in sorted(players.keys()):
        print(f"{name} : {players[name]}")
    print("***Dead***")
    for name in sorted(dead_players.keys()):
        print(f"{name} : {dead_players[name]}")

main()
