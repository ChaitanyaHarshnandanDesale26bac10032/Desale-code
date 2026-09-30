# Cricket Team Selector
 # Overview
Cricket Team Selector is a Python console application that helps build the best possible **Playing 11** from a pool of players entered by the user. It calculates a performance score for each player using batting, bowling, and form metrics, then automatically selects a balanced, role-based team lineup for the next series.


# Features
- Takes player details through interactive console input
- Stores data using Python lists and dictionaries
- Calculates a weighted performance score per player
- Sorts players by score (highest first)
- Selects a balanced Playing 11 using required role counts
- Enforces maximum role limits per team
- Groups players by batting position (Opener, Middle, Finisher, Bowler)
- Randomizes order within each section for lineup variety
- Displays the final lineup with player ratings
- Shows the total team rating


## Technologies Used
- **Python Python 3.14.7
- **random** module (for shuffling lineup order)
- **Command-line / Terminal**
- Any Python IDE (VS Code, PyCharm, IDLE)


## How to Run
### Step 1: Install Python 3
Check if Python is installed:

python(Python 3.14.7)

### Step 2: Save the Code
Save the program as:
cricket_team_selector.py

### Step 3: Run the Program
python cricket_team_selector.py

### Step 4: Enter Player Details
When prompted, enter:
Total number of players
Player name
Role: BAT, WK, AR, BOWL
Position: OPENER, MIDDLE, FINISHER, BOWLER
Runs scored
Strike Rate (SR)
Wickets taken
Economy rate
Form factor (e.g., 1.1)

### Step 5: View Output
The program prints:
Player scores
Selected Playing 11 by section
Total team rating

# How the Code Works
1. Player Input
The program asks for the number of players, then loops to collect each player's stats into a dictionary and appends it to the players list.
2. Score Calculation
The calculation_of_score() function computes:
batting_pts = (runs × (SR / 100)) × 0.4
bowling_pts = (wickets × 25 + econ_bonus × 5) × 0.6   [if wickets > 0]
econ_bonus  = 12 - economy
total       = (batting_pts + bowling_pts) × form
The final score is rounded to 2 decimals.

3. Team Selection
Players are sorted by score (descending).
The program first picks required roles:
WK: 1, BAT: 3, AR: 1, BOWL: 3
Then fills remaining slots up to 11 using max role limits:
BAT: 5, WK: 2, AR: 4, BOWL: 5
4. Lineup Organization
Selected players are grouped by position into:

Openers
Middle Order
Finishers
Bowling Attack / Tail
Each group is shuffled randomly, then printed with batting numbers and ratings.

5. Total Rating
The program sums all player scores in the Playing 11 and displays the total team rating.

Testing Instructions
Run with at least 11 players.
Include variety of roles:
1–2 Wicketkeepers
3–5 Batsmen
1–4 All-Rounders
3–5 Bowlers
Try different run/SR/wicket values to verify scoring.
Confirm highest-rated players are selected.
Run multiple times to see shuffled lineup order.
Verify role limits are never exceeded.

Project Structure


cricket-team-selector/
│── cricket_team_selector.py
│── README.md
└── screenshots/
Future Improvements
GUI using Tkinter or web interface
Save/load players from CSV or JSON
Captain & vice-captain selection
Export Playing 11 to file
Advanced analytics-based scoring
Author

CHAITANYA HARSHNANDAN DESALE 
