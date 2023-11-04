# Sketching for level 4
## Thing in common with Level 2
In a single frame, Pac-man is stationary, monster is also stationary. 
Pacman need food, so do monsters.
## Thing that are different.
Food of pacman is fruit, while which of monster in Pac-man.
Pac-man have many food. 

# Thing to change in sight
1. The algorithm is for pacman only since there is no parameter for where to search. 
2. Have to seach nearest food exciplitly.
3. Pac-man position has to be known too -> ghost position must be processed after update of Pacman position.
4. Ghost algorithm must treat ghost differently.

# The insight
- Pac-man should still do its job with food position varying
- Ghost should chase Pac-man by Pacman's known position

# Psuedo code:
Intialize foods position, score, ghost position -> all done in matrix initialization

while true:
	die?
	food?
	outOfFood?
	# Pacman do his job: eat food, avoid monsters -> update_pacman_position(matrix, pacman-postion)
	# Monsters do their job: chasing pacman
