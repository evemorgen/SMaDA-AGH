# Lab 4 - mutate all the things

1. prepare your environment and run as in the first laboratory class, optimization of Rastrigin function in 30 dimensions,
2. check the simple inheritance structure structure: 
  - `UniformMutation`,
  - `Random Mutator`,
  - `Random Range Mutator with range`
3. Start with comparing these two with two modal mutations (discrete and continuous) check [this pdf](https://pdfs.semanticscholar.org/f515/e4719cb13d7bf837a77a22a1c6ea5517055a.pdf?fbclid=IwAR2XcXrNEg2SNTJ5FmzII3Ox4zJR3Ht3wDcygezCeGt23-O9HkqIPL81nWI) for description (in particular distributions)
4. focus on `Random Mutator` and check its efficiency for different probability of mutation (default `Locus Mut Prob`), they may be, 
  - 0.01,
  - 0.1,
  - 0.2,
  - 0.5, 
  - 0.8
5. pick the best value of the probability set it for `RandomRange Mutator` and check the efficiency of this mutator for different ranges
  - +- 0.1,
  - +- 0.01,
  - +-0.2 etc.
do the same for `NonUniformMutator`.
