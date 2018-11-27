RUN='./run.sh'
CONFIGS=$(ls | grep xml | grep -v pom)

for CFG in $CONFIGS; do
    for i in {1..5}; do
        $RUN $CFG
        LOGFILE=$(ls | grep Rastrigin | grep '.report.txt')
        mv "$LOGFILE" "${CFG}-${i}.txt"
        sleep 5
    done;
done;
