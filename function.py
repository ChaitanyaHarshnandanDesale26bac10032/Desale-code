# function.py

import random


def calculate_score(player):
    bat = (player["runs"] * (player["sr"] / 100)) * 0.4
    bowl = 0
    if player["wickets"] > 0:
        bowl = (player["wickets"] * 25 + (12 - player["econ"]) * 5) * 0.6
    return round((bat + bowl) * player["form"], 2)


def add_players():
    players = []
    n = int(input("\nEnter total number of players: "))

    for i in range(n):
        print(f"\nPlayer {i+1}:")
        name = input("Name: ")
        role = input("Role (BAT/WK/AR/BOWL): ").upper()
        pos = input("Position (OPENER/MIDDLE/FINISHER/BOWLER): ").upper()
        runs = float(input("Runs: "))
        sr = float(input("Strike Rate: "))
        wickets = int(input("Wickets: "))
        econ = float(input("Economy: "))
        form = float(input("Form: "))

        player = {
            "name": name, "role": role, "pos": pos,
            "runs": runs, "sr": sr, "wickets": wickets,
            "econ": econ, "form": form
        }
        player["score"] = calculate_score(player)
        players.append(player)

    print("All players added successfully!\n")
    return players


def select_team(players):
    players.sort(key=lambda p: p["score"], reverse=True)
    playing_11 = []
    used = []

    # Minimum required
    for role, need in [("WK",1), ("BAT",3), ("AR",1), ("BOWL",3)]:
        count = 0
        for p in players:
            if p["role"] == role and p["name"] not in used:
                playing_11.append(p)
                used.append(p["name"])
                count += 1
                if count == need: 
                    break

    # Fill remaining slots
    limits = {"BAT":5, "WK":2, "AR":4, "BOWL":5}
    for p in players:
        if len(playing_11) == 11:
            break
        if p["name"] not in used:
            if limits[p["role"]] > sum(1 for x in playing_11 if x["role"] == p["role"]):
                playing_11.append(p)
                used.append(p["name"])

    print("Playing 11 selected successfully!\n")
    return playing_11


def show_team(playing_11):
    # Group players
    openers = [p for p in playing_11 if p["pos"] == "OPENER"]
    middle = [p for p in playing_11 if p["pos"] == "MIDDLE"]
    finishers = [p for p in playing_11 if p["pos"] == "FINISHER"]
    bowlers = [p for p in playing_11 if p["pos"] == "BOWLER"]

    random.shuffle(openers)
    random.shuffle(middle)
    random.shuffle(finishers)
    random.shuffle(bowlers)

    print("\n" + "*" * 43)
    print("NEXT SERIES PLAYING 11 LINEUP")
    print("*" * 42)

    num = 1
    for group, title in [(openers, "OPENERS"), (middle, "MIDDLE ORDER"), 
                        (finishers, "FINISHERS"), (bowlers, "BOWLING ATTACK / TAIL")]:
        if group:
            print(f"\n--- {title} ---")
            for p in group:
                print(f"{num}. {p['name']} ({p['role']}) - Rating: {p['score']}")
                num += 1

    total = round(sum(p["score"] for p in playing_11), 2)
    print("\n" + "*" * 48)
    print(f"Total Team Rating: {total}")
    print("*************************************************")
