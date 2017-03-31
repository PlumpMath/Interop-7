#!/usr/bin/bash
# Run the summary and index-summary scripts for a flowcell

fname=`basename $1`
/data/apps/interop-buld/src/apps/summary /data/BaseSpace/Runs/$fname/Files | sed 's/ \+//g'  | grep -A 100 "Total" > /data/basemount-processing/$fname.summary.csv
/data/apps/interop-buld/src/apps/index-summary /data/BaseSpace/Runs/$fname/Files | sed 's/ \+/\t/g' |  grep -A 2 "Lane"  > /data/basemount-processing/$fname.index-summary.csv

python uploader.py $fname $2




