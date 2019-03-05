% Matrices

M = [1 2 3 4; 9 8 7 6; 1 1 1 1] % make a matrix

M(:,1) % get the first column
M(1, :) % get the first row 
M(2, 1:2) 

M(end + 1, :) = [0 0 0 0] % add a row

M = transpose(M) % same as M'


rref(M)

N = [1 1 1 1; 2 2 2 2; 3 3 3 3; 4 4 4 4;]; 

M + N 

A = magic(3); %Create a magic square

clear
% Matrix multiplication
A = [1 0 4; 2 1 1; 3 1 0; 0 2 2] 
B = [2 4; 1 1 ;3 0] 

A * B % which =/= B * A 

% A .* B % Multiply corresponding elements rather than actual matrix mult 


