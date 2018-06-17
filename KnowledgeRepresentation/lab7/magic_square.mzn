include "globals.mzn";

% constants
int: N = 3;

% variables
array [1..N, 1..N] of var 1..N*N: board;

% constraints
% all numbers must be different
constraint alldifferent([board[i,j] | i,j in 1..N]);
% all rows must have same sum
constraint forall(i,j in 1..N where j > i)(sum(row(board,i)) == sum(row(board,j)));
% all cols mush have same sum
constraint forall(i,j in 1..N where j > i)(sum(col(board,i)) == sum(col(board,j)));
% rows and cols have same sum
constraint sum(row(board,1)) == sum(col(board, 1));
% diagonals has same sum as rest
constraint sum([board[i,i] | i in 1..N]) == sum(row(board, 1));
constraint sum([board[N+1-i,i] | i in 1..N]) == sum(row(board, 1));

% solve
solve satisfy;

% output
output [show(board[i,j]) ++ "|" ++ if j mod N == 0 then "\n" else "" endif | i,j in 1..N ]
