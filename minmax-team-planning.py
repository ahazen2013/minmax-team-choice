

# Contestants:
# - ID: 5-digit integer, no 2 contestants have the same ID          32-bit int
# - Capacity: a value in range [0.0, 200.0]                         64-bit double
# - Happy A, B: happiness about captain A, B in range [0.0, 1.0]    64-bit double
# - State: 0 if not picked, 1 if on your team, 2 if on Bob's

class Contestant:
    ID = 0
    cc = 0.0
    power_A = 0.0
    power_B = 0.0
    team = 0
    last_digit = 0

    def __init__(self, ID, cc, happy_A, happy_B, team):
        self.ID = int(ID)
        self.cc = float(cc)
        self.power_A = float(happy_A) * self.cc
        self.power_B = float(happy_B) * self.cc
        self.team = int(team)
        self.last_digit = int(ID) % 10


# sort contestants by ID
def sort_contestants(contestants_sort):
    for s in range(0, len(contestants_sort)):
        for t in range(0, (len(contestants_sort)-s-1)):
            if contestants_sort[t].ID > contestants_sort[t+1].ID:
                sort_temp = contestants_sort[t]
                contestants_sort[t] = contestants_sort[t+1]
                contestants_sort[t+1] = sort_temp


# calculates final score
def final_score(first_team, second_team):
    tp_A, dt_A, tp_B, dt_B = 0, 0, 0, 0
    A_IDs = list()
    B_IDs = list()
    for d in range(0, 5):
        if first_team[d].last_digit not in A_IDs:
            dt_A = dt_A + 24
            A_IDs.append(first_team[d].last_digit)
        if second_team[d].last_digit not in B_IDs:
            dt_B = dt_B + 24
            B_IDs.append(second_team[d].last_digit)
        tp_A = tp_A + first_team[d].power_A
        tp_B = tp_B + second_team[d].power_B
    if dt_A == 120:
        tp_A = tp_A + 120
    if dt_B == 120:
        tp_B = tp_B + 120
    return tp_A - tp_B


# minimax algorithm
def recursive_minimax(A_team, B_team, available_contestants, prechosen, captain):
    if captain == 1:
        new_best_score = -1001
        best_contestant = available_contestants[0]
        for i in range(0, len(available_contestants)):
            sort_contestants(available_contestants)
            temp_val = available_contestants[i]
            A_team.append(temp_val)
            available_contestants.remove(temp_val)
            if len(A_team) <= 5:
                possible_best_score = recursive_minimax(A_team, B_team, available_contestants, prechosen, 2)
                if possible_best_score > new_best_score:
                    new_best_score = possible_best_score
                    best_contestant = temp_val
            A_team.remove(temp_val)
            available_contestants.append(temp_val)
        if len(A_team) > prechosen:
            return new_best_score
        return best_contestant
    if captain == 2:
        new_best_score = 1001
        for i in range(0, len(available_contestants)):
            sort_contestants(available_contestants)
            temp_val = available_contestants[i]
            B_team.append(temp_val)
            available_contestants.remove(temp_val)
            if len(B_team) < 5:
                possible_best_score = recursive_minimax(A_team, B_team, available_contestants, prechosen, 1)
                if possible_best_score < new_best_score:
                    new_best_score = possible_best_score
            else:
                temp_score = final_score(A_team, B_team)
                if temp_score < new_best_score:
                    new_best_score = temp_score
            available_contestants.append(temp_val)
            B_team.remove(temp_val)
        return new_best_score


# ab
def recursive_ab(A_team, B_team, available_contestants, prechosen, captain, compval):
    if captain == 1:
        new_best_score = -1001
        best_contestant = available_contestants[0]
        for i in range(0, len(available_contestants)):
            if new_best_score > compval:
                break
            sort_contestants(available_contestants)
            temp_val = available_contestants[i]
            A_team.append(temp_val)
            available_contestants.remove(temp_val)
            if len(A_team) <= 5:
                possible_best_score = recursive_ab(A_team, B_team, available_contestants, prechosen, 2, new_best_score)
                if possible_best_score > new_best_score:
                    new_best_score = possible_best_score
                    best_contestant = temp_val
            available_contestants.append(temp_val)
            A_team.remove(temp_val)
        if len(A_team) > prechosen:
            return new_best_score
        return best_contestant
    if captain == 2:
        new_best_score = 1001
        for i in range(0, len(available_contestants)):
            if new_best_score < compval:
                break
            sort_contestants(available_contestants)
            temp_val = available_contestants[i]
            B_team.append(temp_val)
            available_contestants.remove(temp_val)
            if len(B_team) < 5:
                possible_best_score = recursive_ab(A_team, B_team, available_contestants, prechosen, 1, new_best_score)
                if possible_best_score < new_best_score:
                    new_best_score = possible_best_score
            else:
                temp_score = final_score(A_team, B_team)
                if temp_score < new_best_score:
                    new_best_score = temp_score
            available_contestants.append(temp_val)
            B_team.remove(temp_val)
        return new_best_score


input_file = open("input.txt", "r")  # read input file always named input.txt
parameters = input_file.readlines()
input_file.close()

n = int(parameters[0])   # number of contestants
a = parameters[1]        # algorithm to be used
contestants = list()     # list of contestants to be populated
team_A = list()          # list of team A's members
team_B = list()          # list of team B's members

for r in range(2, n + 2):    # populate list of contestants, Team A, Team B
    temp_p = parameters[r]
    temp_person = temp_p.split(',')
    temp_contestant = Contestant(temp_person[0], temp_person[1], temp_person[2], temp_person[3], temp_person[4])
    if temp_contestant.team == 1:
        team_A.append(temp_contestant)
    elif temp_contestant.team == 2:
        team_B.append(temp_contestant)
    else:
        contestants.append(temp_contestant)

# Branching: iterate through nodes in ascending order of ID
sort_contestants(contestants)
ret_ID = contestants[0]   # ID to be printed in output.txt

if a == "minimax" + '\n':
    ret_ID = recursive_minimax(team_A, team_B, contestants, len(team_A), 1)

if a == "ab" + '\n':
    ret_ID = recursive_ab(team_A, team_B, contestants, len(team_A), 1, 1001)

output_file = open("output.txt", "w")  # Output to output.txt a single line = ID of your first pick
output_file.write(str(ret_ID.ID))
output_file.close()
