LAB 5. Parallel Algorithms

Implement the algorithm which computes in parallel a matrix product of N  matrices:  
![](pic1.png)  

where matrix sizes are given inside square brackets. The main task (T) i.e.,  multiplication of matrices, has to be split into subtask (T1,T2,…Tm) to be proceeded in parallel. For example:  
![](pic2.png)

After completing T1,T2,T3, the algorithm proceeds with the main task, T.
