include "alldifferent.mzn";
include "inverse.mzn";

int: N = 100;
set of int: indexes = 1..N;

array[indexes] of var indexes: rows;
array[indexes] of var indexes: cols;

constraint alldifferent(rows);
constraint alldifferent([rows[i] + i | i in indexes]);
constraint alldifferent([rows[i] - i | i in indexes]);

constraint alldifferent(cols);
constraint alldifferent([cols[i] + i | i in indexes]);
constraint alldifferent([cols[i] - i | i in indexes]);

constraint inverse(rows,cols);

solve satisfy; 
  
output [ if fix(rows[j]) == i then "Q" else "_" endif ++
  if j == N then "\n" else "" endif | i,j in 1..N];