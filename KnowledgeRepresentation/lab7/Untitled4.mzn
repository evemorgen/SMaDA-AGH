include "all_different.mzn";

% Constants
int: num_of_queens = 4;
array [1..num_of_queens] of int: queens = 1..num_of_queens;

%%%%%%%%%%%%% 
% VARIABLES 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% add variables with correct domains 
% tip:                       
% var 1..N: x; declares a variable with domain 1..N   
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
array [1..num_of_queens] of var 1..num_of_queens: qcolumn;
array [1..num_of_queens] of var 1..num_of_queens: qrow;


%%%%%%%%%%%%%
% CONSTRAINTS 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
% add constraints
% tip:
% row_i = row_j (-/+) (j - i)                 
% matches queens placed on the same diagonal, where:
% - i,j - column index
% - row_n - queen's position in the nth col 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
constraint all_different(qrow);  
constraint all_different(qcolumn);  
constraint forall(i,j in 1..num_of_queens where j > i)()
  
  
solve satisfy; 
  
%%%%%%%%%%%%%%%%%%%
% OUTPUT EXAMPLE  
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% - rows[i] - queen's position in the ith row 
% - N - number of queens                     
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
output [ if fix(qrow[j]) == i then "H" else "." endif ++
  if j == num_of_queens then "\n" else "" endif | i,j in 1..num_of_queens]