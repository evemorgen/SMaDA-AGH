include "globals.mzn";
int: N = 10;

array [1..N] of var 1..N: board;

constraint alldifferent(board);
constraint forall(i,j in 1..N where j > i)(board[i] + i != board[j] + j);
constraint forall(i,j in 1..N where j > i)(board[i] - i != board[j] - j);

solve satisfy;

output [ if fix(board[j]) == i then "Q" else "_" endif ++
  if j == N then "\n" else "" endif | i,j in 1..N];