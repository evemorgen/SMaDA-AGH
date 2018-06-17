human(X) :- between(1, 8, X).
initially_infected(X) :- human(X), X <3.
resistant(X) :- human(X), X = 3.
resistant(X) :- human(X), X = 4.

0.6::contact(X,Y) :- human(X), human(Y),  X \= Y.
0.1::breathing(X) :- human(X).
infected(X) :- initially_infected(X),human(X).
infected(X) :- breathing(X), human(X).
infected(X) :- contact(X,Y), infected(Y), human(X), human(Y), X \=Y.
0.5::\+infected(X):-contact(X,Y), X\=Y, initially_infected(Y), resistant(X).

query(infected(_)).