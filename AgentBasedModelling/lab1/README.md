# Game of life exercises

Lab website: <http://home.agh.edu.pl/~porzycki/doku.php?id=sym:lab1>

1. [Basic game of life](exc1/src)
  - In class Board, in method initialize() initialize neighbors for each cell in table. Use Moore neighborhood. For basic version you don't have to initialize cells on the borders, however I encourage you implement periodic boundaries.
  - In class Point write method which returns number of alive neighbors.
  - In class Point, in method calculateNewState(), calculate new state of given cell - according to its actual state and number of alive neighbors. Remember to save cells new state in variable: nextState.
  - Run program, and analyze observed behavior of CA automata.

2. [Game of life with additional rules](exc2/src)
  - One can use different transition rules for Game of Life. Modify your program to use following rules.
  - 2345/45678 - cities
  - 45678/3 - coral
  - Try to find other interesting rules.

3. [Change game of life to rain simulation](exc3/src)
  - Set neighborhood of cells so that the only neighboor of given cell is the cell one step below.
  - In class Point, write method drop(), which change cell state to 6 with some small probability (e.q. 5%).
  - In class Board, in method iteration() use method drop() for cells in top row.
  - If cell state is higher than zero, set nextState = currentState -1
  - If cell state is equals to 0 and its neighbor is higher than 0 set nextState = 6
  - In class Board, in method drawNetting() change colors of cells, so that blue color becomes faded while its state number decrease. You can use method: `g.setColor(new Color(0.0f, 0.0f, 1.0f, 0.65f));` 
