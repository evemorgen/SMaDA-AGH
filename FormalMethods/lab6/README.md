
(Probably) usefull info:
  - State space show us all the possible states
  - Subset of state space is called "strong connected". This allows us to minimize state space by removing loops and stuff

Things to do:
  - take already built model and check if its valid (generate state space and report, check for no dead transitions and markings)
  - and then break it with some stupid "mistake" (lecturer won't accept obvious one, lol)

Solution:
  - working stuff:
      - (easier_crossing.cpn - working example)[easier_crossing.cpn]
      - (easier crossing state space)[ec_ss.png]
      - (easier crossing report - 0 dead markings)[ec_report]
  - not working stuff:
      - (bad_easier_crossing.cpn - example with 2 bad transitions)[bad_easier_crossing.cpn]
      - (bad easier crossing state space)[bec_ss.png]
      - (bad easier crossing report - 4 dead markings)[bec_report]
