
# Lab 2: more constraint programming with miniZinc
Lab webpage: <https://ai.ia.agh.edu.pl/wiki/en:dydaktyka:csp:lab1>

## N Queens problem
```
%declare variables
int: N=16;
array[1..N] of var 1..N: column;

%constranits
constraint forall(i, j in 1..N, where j < i)(column[i] != column[j]);
constraint forall(i, j in 1..N, where j < i)(column[i] + i != column[j] + j);
constraint forall(i, j in 1..N, where j < i)(column[i] - i != column[j] - j);

%solve stuff
solve satisfy;

%output stuff
output [ if fix(column[j]) == i then "H" else "." endif ++
  if j == N then "\n" else "" endif | i,j in 1..N]%
```

## Coloring graphs problem
```
% load parameters
int: nodesNumber;
array[1..nodesNumber,1..nodesNumber] of bool: edges;

% declare variables
array[1..nodesNumber] of var 1..nodesNumber: colors;

% add some constraints
constraint forall(i,j in 1..nodesNumber where edges[i,j] /\ i < j)(colors[i] != colors[j]);
var int: colorsNumber = max(colors);

% solve the shit out of it
solve minimize colorsNumber;

% output results
output [show(colorsNumber), " colors\n",] ++
       [show(colors[i]) ++ " " | i in 1..nodesNumber]%
```

## Solving sudoku
```
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
```

## And finally magic numbers
```
int: N = 20;
array[0..N] of var int: magic;

constraint forall(i in 0..N)(magic[i] == sum([1 | x in 0..N where i == magic[x]]));

solve satisfy;

output [ "magic sequence = ", show(magic),";\n"];
```

