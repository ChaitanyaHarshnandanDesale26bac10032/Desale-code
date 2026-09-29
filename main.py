import random
players = []
print("**************************************************")
print("CRICKET TEAM SELECTOR")
print("*************************************************")

num_players_input = input("Enter total number of players to add: ")
num_players = int(num_players_input)
for i in range(num_players):
    print(f"\n--- Enter details for Player {i + 1} ---")
    name = input("Player Name: ").strip()
    role = input("Role (BAT, WK, AR, BOWL): ").upper().strip()
    pos = input("Position (OPENER, MIDDLE, FINISHER, BOWLER): ").upper().strip()
    runs = float(input("Runs scored: ").strip())
    sr = float(input("Strike Rate (SR): ").strip())
    wickets = int(input("Wickets taken: ").strip())
    econ = float(input("Economy rate: ").strip())
    form = float(input("Form factor (e.g., 1.1): ").strip())
    player = {"name": name,"role": role,"pos": pos,"runs": runs,"sr": sr,"wickets": wickets,"econ": econ,"form": form}
    players.append(player)
    
def calculation_of_score(player):
    batting_pts = (player["runs"] * (player["sr"] / 100)) * 0.4
    bowling_pts = 0
    if player["wickets"] > 0:
        econ_bonus = 12 - player["econ"]
        bowling_pts = (player["wickets"] * 25 + econ_bonus * 5) * 0.6
    total = (batting_pts + bowling_pts) * player["form"]
    return round(total, 2)
for p in players:
    p["score"] = calculation_of_score(p)
players.sort(key=lambda x: x["score"], reverse=True)
playing_11 = []
selected_players = []
required_roles = [("WK", 1), ("BAT", 3), ("AR", 1), ("BOWL", 3)]
for role_name, count in required_roles:
    picked_count = 0
    for p in players:
        if p["role"] == role_name and p["name"] not in selected_players:
            playing_11.append(p)
            selected_players.append(p["name"])
            picked_count += 1
            if picked_count == count:
                break

max_role_limits = {"BAT": 5, "WK": 2, "AR": 4, "BOWL": 5}
for p in players:
    if len(playing_11) == 11:
        break
    
    if p["name"] not in selected_players and p["role"] in max_role_limits:
        current_count = 0
        for m in playing_11:
            if m["role"] == p["role"]:
                current_count += 1
                
        if current_count < max_role_limits[p["role"]]:
            playing_11.append(p)
            selected_players.append(p["name"])
openers = []
middle_order = []
finishers = []
bowlers = []
for p in playing_11:
    if p["pos"] == "OPENER":
        openers.append(p)
    elif p["pos"] == "MIDDLE":
        middle_order.append(p)
    elif p["pos"] == "FINISHER":
        finishers.append(p)
    elif p["pos"] == "BOWLER":
        bowlers.append(p)
random.shuffle(openers)
random.shuffle(middle_order)
random.shuffle(finishers)
random.shuffle(bowlers)
print("\n" + "*******************************************")
print("NEXT SERIES PLAYING 11 LINEUP")
print("******************************************")
batting_number = 1
def show_section(title, player_group):
    global batting_number
    if len(player_group) > 0:
        print(f"\n--- {title} ---")
        for p in player_group:
            print(f"{batting_number}. {p['name']} (Role: {p['role']}) - Rating: {p['score']}")
            batting_number += 1
show_section("OPENERS", openers)
show_section("MIDDLE ORDER", middle_order)
show_section("FINISHERS", finishers)
show_section("BOWLING ATTACK / TAIL", bowlers)
total_score = 0
for p in playing_11:
    total_score += p["score"]
print("\n" + "************************************************")
print("Total Team Rating:", round(total_score, 2))
print("********************************************")