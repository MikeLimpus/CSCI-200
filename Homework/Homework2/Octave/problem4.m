# Jonathan Limpus
# Homework 2, Problem 4
# Validate PS 2.6 2a, 4b, 18

# 2a 
disp("Problem 2a\n A + B")
A = [1 0 4; -1 2 2; 0 -2 -3]
B = [-1 3 5; 2 2 -3; 2 -3 0]
A + B
clear

# 4b
disp("Problem 4b\n AB")
A = [1 -3 0; 1 2 2; 2 1 -1]
B = [1 -1 2 3; -1 0 3 -1; -3 -2 0 -2] 
A * B
clear

# 18
disp("Problem 18\n B is the inverse of A") 
A = [7 -8 5; -4 5 -3; 1 -1 1]
B = inv(A) 
