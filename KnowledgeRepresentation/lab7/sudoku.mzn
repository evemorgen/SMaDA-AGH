% sudoku
include "globals.mzn";

% parameters
int: N = 4;

% variables
array [1..N*N, 1..N*N] of var 1..N*N: board;

predicate check_box(int: startx, int: starty, array[int,int] of var int: board) = 
  alldifferent([board[i,j] | i in startx..startx+N-1, j in starty..starty+N-1]);

% constraints
constraint forall(i in 1..N*N)(alldifferent(row(board, i)));
constraint forall(i in 1..N*N)(alldifferent(col(board, i)));
constraint forall(i,j in 0..N-1)(check_box(i*N+1, j*N+1, board));

% solve
solve satisfy;

output [
  show(board[i,j]) ++ if (j mod N == 0) then " " else "" endif ++ if (j mod (N*N)) == 0 then "\n" else "" endif ++ if (i mod N == 0 /\ j == N*N) then "\n" else "" endif | i,j in 1..N*N
];