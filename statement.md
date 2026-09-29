# Cricket Team Selector - Statement

## Problem Statement
Selecting the best cricket team from a group of available players can be difficult when multiple performance factors such as batting, bowling, and current form need to be considered together. Manual selection may lead to biased or unbalanced team composition. This project solves that problem by creating a Python-based Cricket Team Selector that calculates a performance score for each player and automatically generates a balanced Playing 11 based on role requirements and player positions.

## Scope of the Project
The scope of this project is limited to a console-based cricket team selection system. It allows the user to enter player details such as role, batting position, runs, strike rate, wickets, economy rate, and form factor. Based on these inputs, the program computes player ratings, selects a team according to predefined role constraints, and displays the final lineup.

The project covers:
- Input of player performance details
- Score calculation using batting and bowling metrics
- Role-based team selection
- Position-wise lineup arrangement
- Final team rating display

The project does not currently include:
- Graphical user interface
- Database or file storage
- Real-time match statistics
- Advanced analytics or machine learning models

## Target Users
This project is mainly intended for:
- Cricket fans interested in team analysis
- Students learning Python programming
- Beginners practicing data structures and logic building
- Teachers or evaluators reviewing mini-projects
- Anyone who wants a simple automated cricket team selection tool

## High-Level Features
- Accepts player details through user input
- Stores player records in lists and dictionaries
- Calculates a performance-based score for each player
- Sorts players according to their scores
- Selects a balanced Playing 11 based on required roles
- Applies maximum limits for each role category
- Organizes selected players into batting and bowling sections
- Randomizes order within sections for lineup variety
- Displays individual player ratings
- Shows total team rating
