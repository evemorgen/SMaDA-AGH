include "globals.mzn";

int: S;
int: N = S*S;

array[1..N, 1..N] of var 1..N: puzzle;

array[1..N, 1..N] of 0..N: board;

constraint forall(i, j in 1..S where board[i, j] != 0)(puzzle[i,j] == board[i,j]);

constraint forall(i in 1..N)(alldifferent(row(puzzle, i)));
constraint forall(i in 1..N)(alldifferent(col(puzzle, i)));
constraint forall(x, y in 1..S)(alldifferent([puzzle[i,j] | i in ((x-1)*S+1)..(x*S), j in ((y-1)*S+1)..(y*S)]));

solve satisfy;

output [ show(puzzle[i,j]) ++ " " ++
  if j mod S == 0 then " " else "" endif ++ if j == N /\ i != N then
  if i mod S == 0 then "\n\n" else "\n" endif else "" endif
    | i,j in 1..N ] ++ ["\n"];
