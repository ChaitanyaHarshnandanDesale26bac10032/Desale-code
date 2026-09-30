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
##Screenshots 
#Code
<img width="1631" height="992" alt="CODE SS 1" src="https://github.com/user-attachments/assets/2f93b350-c937-4b56-a6d5-840b23063673" />
<img width="1432" height="897" alt="CODE SS 2" src="https://github.com/user-attachments/assets/78b83c9a-a277-44ad-9546-6c3f71797c0a" />
<img width="1606" height="467" alt="CODE SS 3 " src="https://github.com/user-attachments/assets/a3ab7b08-41c5-4f08-8282-7bd75a95786d" />
#Output 
<img width="1457" height="807" alt="OUTPUT SS 1 " src="https://github.com/user-attachments/assets/5bb4e93c-bf3f-4368-8ce4-87e1a3fff159" />
<img width="1312" height="872" alt="OUTPUT SS 2 " src="https://github.com/user-attachments/assets/8459190a-eacf-4446-b3bd-a7a9879810bd" />
<img width="1320" height="882" alt="OUTPUT SS 3" src="https://github.com/user-attachments/assets/ff11c232-d105-4efa-ba11-d1bee09e06a8" />
<img width="1260" height="837" alt="OUTPUT SS 4 " src="https://github.com/user-attachments/assets/36facd58-e115-4a69-aa7b-a04d8bb3435e" />

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


Future Improvements
GUI using Tkinter or web interface
Save/load players from CSV or JSON
Captain & vice-captain selection
Export Playing 11 to file
Advanced analytics-based scoring
Author

CHAITANYA HARSHNANDAN DESALE 
