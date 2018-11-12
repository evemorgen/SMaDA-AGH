# Lab 3/4 - Algorithms in Computer Graphics

After course site:
> In this exercise you will implement functions being frequently used in computer graphics, CAD systems, design software etc.  
> We deal with a 3D solid which is assumed to be given as an array, say F, of triangles (faces) forming its surface:  

> F[1....N], where N is a number of faces. In turn, each face F[i] (of the type Face) is a triple of points [x,y,z]  (of the type Point) of 3D space. Additionally we define the Edge structure holding solid/face edges.  
  
  
Implemented functions:
  - [import and parse data](https://github.com/evemorgen/SMaDA-AGH/blob/master/AdvancedAlgorithmsAndDataStructures/lab4/distances.py#L10)
  - point:
    - [Distance between points](https://github.com/evemorgen/SMaDA-AGH/blob/master/AdvancedAlgorithmsAndDataStructures/lab4/distances.py#L24)
    - [Distance between point and edge](https://github.com/evemorgen/SMaDA-AGH/blob/master/AdvancedAlgorithmsAndDataStructures/lab4/distances.py#L96)
    - [Distance between point and triangle](https://github.com/evemorgen/SMaDA-AGH/blob/master/AdvancedAlgorithmsAndDataStructures/lab4/distances.py#L55)
  - edges:
    - [Distance between edges](https://github.com/evemorgen/SMaDA-AGH/blob/master/AdvancedAlgorithmsAndDataStructures/lab4/distances.py#L117)
    - [Distance between edge and triangle](https://github.com/evemorgen/SMaDA-AGH/blob/master/AdvancedAlgorithmsAndDataStructures/lab4/distances.py#L159)
  - triangles:
    - [Distance between triangles](https://github.com/evemorgen/SMaDA-AGH/blob/master/AdvancedAlgorithmsAndDataStructures/lab4/distances.py#L30)
  - solids:
    - [Distance between solids](https://github.com/evemorgen/SMaDA-AGH/blob/master/AdvancedAlgorithmsAndDataStructures/lab4/distances.py#L90)
