# Lab 3: Crowd dynamics simulation - a multi-agent system based on CA

1. [In class Board in method initialize() initialize neighbors for all cells.](https://github.com/evemorgen/SMaDA-AGH/blob/feature/abm/lab3/AgentBasedModelling/lab3/Pedestrians/src/Board.java#L54)
2. In class Board in method calculateField():
    - [Create list of points that need recalculation of its static field](https://github.com/evemorgen/SMaDA-AGH/blob/feature/abm/lab3/AgentBasedModelling/lab3/Pedestrians/src/Board.java#L65). Please note that initially the value of staticField is set to 100000.
    - [For each cell type 2 (exit)](https://github.com/evemorgen/SMaDA-AGH/blob/feature/abm/lab3/AgentBasedModelling/lab3/Pedestrians/src/Board.java#L68) [set 0 as a value of its staticField](https://github.com/evemorgen/SMaDA-AGH/blob/feature/abm/lab3/AgentBasedModelling/lab3/Pedestrians/src/Board.java#L69), [each neighbor of such cell should be added to list toCheck](https://github.com/evemorgen/SMaDA-AGH/blob/feature/abm/lab3/AgentBasedModelling/lab3/Pedestrians/src/Board.java#L70)
    - [Unlit list toCheck is empty:](https://github.com/evemorgen/SMaDA-AGH/blob/feature/abm/lab3/AgentBasedModelling/lab3/Pedestrians/src/Board.java#L75)
        - [verify if its first element changes its staticField](https://github.com/evemorgen/SMaDA-AGH/blob/feature/abm/lab3/AgentBasedModelling/lab3/Pedestrians/src/Board.java#L77) (use method calcStaticField() for this cell) if so, [add all neighbors of this cell to list toCheck](https://github.com/evemorgen/SMaDA-AGH/blob/feature/abm/lab3/AgentBasedModelling/lab3/Pedestrians/src/Board.java#L78)
        - [remove first element from the list.](https://github.com/evemorgen/SMaDA-AGH/blob/feature/abm/lab3/AgentBasedModelling/lab3/Pedestrians/src/Board.java#L76)

3. In class Point:
    - [Implement method calcStaticField().](https://github.com/evemorgen/SMaDA-AGH/blob/feature/abm/lab3/AgentBasedModelling/lab3/Pedestrians/src/Point.java#L26)

4. Crowd dynamics - naive implementation
    - In class Point in method [move()](https://github.com/evemorgen/SMaDA-AGH/blob/feature/abm/lab3/AgentBasedModelling/lab3/Pedestrians/src/Point.java#L36):
        - Check if there is a pedestrian in given cell
        - [If so, move the pedestrian to the not occupied, neighbor cell with smallest static floor field.](https://github.com/evemorgen/SMaDA-AGH/blob/feature/abm/lab3/AgentBasedModelling/lab3/Pedestrians/src/Point.java#L43)

5. Crowd dynamics - improvements 
    - Agents that reach exit should be removed from the simulation. [If pedestrian enters cell type 2 (exit) do not set its variable isPedestrian on true.](https://github.com/evemorgen/SMaDA-AGH/blob/feature/abm/lab3/AgentBasedModelling/lab3/Pedestrians/src/Point.java#L46)
    - No synchronization of cells. One should note, that agents moving down, and right can reach destination in one iteration. In order to fix this issue, [create in class Point variable `boolean blocked = false;`](https://github.com/evemorgen/SMaDA-AGH/blob/feature/abm/lab3/AgentBasedModelling/lab3/Pedestrians/src/Point.java#L13). If cell is blocked, agent on this cell can't make a move. Cell is blocked is some pedestrian enters it. Remember to unblock all cells at the beginning of each iteration.
