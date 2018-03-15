% sudoku

int: N = 3;
array[1..N,1..N] of int: board;

constraint all_different(row(board));
constraint all_different(col(board));

solve satisfy;

output [ show(puzzle[i,j]) ++ " " ++
  if j mod S == 0 then " " else "" endif ++ if j == N /\ i != N then
  if i mod S == 0 then "\n\n" else "\n" endif else "" endif
    | i,j in PuzzleRange ] ++ ["\n"];