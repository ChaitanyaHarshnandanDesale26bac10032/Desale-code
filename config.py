# config.py
"""
Configuration file for Cricket Team Selector (Beginner Level).
All fixed values used in the main program are stored here.
Uses only basic Python — no imports, no JSON, no CSV.
"""

# ---------------------------------------------------------
# PROGRAM TITLES AND LINES
# ---------------------------------------------------------
LINE = "*" * 50
LINE2 = "*" * 43

PROGRAM_NAME = "CRICKET TEAM SELECTOR"
LINEUP_TITLE = "NEXT SERIES PLAYING 11 LINEUP"

# ---------------------------------------------------------
# TEAM SIZE
# ---------------------------------------------------------
TEAM_SIZE = 11

# ---------------------------------------------------------
# REQUIRED ROLES (minimum players needed per role)
# ---------------------------------------------------------
REQUIRED_ROLES = [
    ("WK", 1),
    ("BAT", 3),
    ("AR", 1),
    ("BOWL", 3)
]

# ---------------------------------------------------------
# MAXIMUM PLAYERS ALLOWED PER ROLE
# ---------------------------------------------------------
MAX_ROLE_LIMITS = {
    "BAT": 5,
    "WK": 2,
    "AR": 4,
    "BOWL": 5
}

# ---------------------------------------------------------
# SCORING VALUES
# ---------------------------------------------------------
BATTING_WEIGHT = 0.4
BOWLING_WEIGHT = 0.6
ECON_BASE = 12
ECON_BONUS_MULTIPLIER = 5
WICKET_POINTS = 25
BATTING_SR_DIVISOR = 100
SCORE_ROUND = 2

# ---------------------------------------------------------
# INPUT PROMPTS
# ---------------------------------------------------------
PROMPT_NUM_PLAYERS = "Enter total number of players to add: "

PLAYER_HEADER = "--- Enter details for Player"

PROMPT_NAME = "Player Name: "
PROMPT_ROLE = "Role (BAT, WK, AR, BOWL): "
PROMPT_POSITION = "Position (OPENER, MIDDLE, FINISHER, BOWLER): "
PROMPT_RUNS = "Runs scored: "
PROMPT_SR = "Strike Rate (SR): "
PROMPT_WICKETS = "Wickets taken: "
PROMPT_ECON = "Economy rate: "
PROMPT_FORM = "Form factor (e.g., 1.1): "

# ---------------------------------------------------------
# OUTPUT SECTION TITLES
# ---------------------------------------------------------
SECTION_OPENERS = "OPENERS"
SECTION_MIDDLE = "MIDDLE ORDER"
SECTION_FINISHERS = "FINISHERS"
SECTION_BOWLERS = "BOWLING ATTACK / TAIL"

# ---------------------------------------------------------
# OUTPUT MESSAGES
# ---------------------------------------------------------
MSG_TOTAL = "Total Team Rating: "
MSG_TEAM_SELECTION = "Playing 11 selected successfully!\n"