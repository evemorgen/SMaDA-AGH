RUN='./run.sh'
CONFIGS=$(ls configs | grep xml | grep -v pom)

for CFG in $CONFIGS; do
    for i in {1..5}; do
        $RUN configs/$CFG
        LOGFILE=$(ls | grep Rastrigin | grep '.report.txt')
        mv "$LOGFILE" "${CFG}-${i}.txt"
        sleep 5
    done;
done;
