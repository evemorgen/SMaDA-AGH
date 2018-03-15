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
  if j == N then "\n" else "" endif | i,j in 1..N]