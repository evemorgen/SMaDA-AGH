for node in $(cat graf1.txt | tr '\t' '\n' | grep -v '\.' | grep -v ' ' | grep -v 10 | sort | uniq); do
    ./ENV/bin/python ff.py graf1.txt 10 $node
done
