# EA - lab 1

## JClec tutorial
  - to run it:
      - simply import project to intellij
      - copy `Rastrigin.cfg` to project root directory
      - set runtime class to `RunExperiment` one
      - add `Rastrigin.cfg` as run argument
      - fix all weird errors occuring because `Rastrigin.cfg` bad values
  - report from first run is available in [here](lab1/jclec4-base/Rastrigin-report.txt)
  - to select only valuable output use this fancy oneliner:   
    `cat jclec4-base/Rastrigin-report.txt | grep Best | grep -o 'value=\d\+\.\d\+' | sed -e 's/value=//g'`
  - some charts are comming soon
