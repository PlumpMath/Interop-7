# UB-GBC Quarterly Report
Parsing illumina Interop files for loading into UB-GBC RequestTracker.
Not for public consumption. Please contact jbard@buffalo.edu for more information.

To Run:

Connect to nextgenlab02 as correct user
change directory to /data....Interop
submit shell upload_wrapper.sh

upload_wrapper.sh [path to BaseSpace/Runs] [RT-Number]


This calls rt_submit.py to process.

###Required:

illumina/Interop commands : https://github.com/Illumina/interop
1. interop-buld/src/apps/summary
2. interop-buld/src/apps/index-summary


TODO:
Add a user in RequestTracker with sequencing queue write only



