int: N = 20;
array[0..N] of var int: magic;

constraint forall(i in 0..N)(magic[i] == sum([1 | x in 0..N where i == magic[x]]));
  
solve satisfy;
  
output [ "magic sequence = ", show(magic),";\n"];
