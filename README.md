This program uses a minmax algorithm to determine which of the provided candidates is the ideal first pick, in a scenario where two team captains
(the user, who captains Team A, and Bob, with Team B) alternate choosing team members from a pool of candidates.

Both team captains have the same information, given in input.txt:
- their ID (each team member's 5-digit unique identifier)
- their "capacity" (their ability to do well in their task, with a higher capacity indicating a more desirable candidate)
- their "Happy_A" value (an amount describing how happy they would be to be on Team A, with a higher value indicating a more happy candidate)
- their "Happy_B" value (the same concept as Happy_A, but describing how happy they would be on Team B)
- their "pick state" (0 if not already on a team, 1 if on Team A, 2 if on Team B)

The ideal first pick candidate is determined by comparing the combined value of all of team A's candidates with the combined value of all of team B's candidates (with each candidate's value being their capacity * the "Happy" value of the team they're on), and maximizing the difference between the two.

### Input (input.txt):

[number of contestants] (positive, even integer)

[algorithm] ("minmax" for a standard minmax algorithm, or "ab", for alpha-beta pruning)

(next (number of contestants) lines) [contestant information] (in format [ID],[capacity],[happy_a],[happy_b],[pick state])

### Output (output.txt):

[ID of chosen contestant] (5-digit integer specific to the user's ideal first pick)

### Example:

input.txt:

14

minimax

75201,92.192554,0.822285,0.134675,0

64504,193.537866,0.239586,0.572906,0

83601,10.631835,0.547191,0.251238,1

87705,111.105311,0.931969,0.653667,1

25202,23.053795,0.075295,0.993499,0

39202,87.595928,0.208003,0.255219,0

42904,168.518783,0.426926,0.432817,0

12703,75.011463,0.456201,0.037517,2

55502,168.823333,0.127049,0.159396,0

82301,82.524738,0.755311,0.406141,0

46902,142.316246,0.511181,0.217463,1

98403,83.132871,0.236225,0.612434,2

79802,118.762381,0.880846,0.579115,2

88903,187.685198,0.277158,0.679969,0

output.txt:

88903
