import sys
import linecache

#Define all of your variables



file1 = sys.argv[1]


def getL5CV(filen):
    return linecache.getline(filen,24)


def parse(filen):
    # get file length
    gth = sum(1 for line in open(filen))
    #rapid files are 45 lines while the highoutput is 90 lines(separating them)
    if gth == 45:
        rap1 = linecache.getline(filen, 13) 
        rap2 = linecache.getline(filen, 16) 
        return rap1,rap2
    #highoutput
    else: 
        lane1 = linecache.getline(filen,12)
        lane2 = linecache.getline(filen,15)
        lane3 = linecache.getline(filen,18) 
        lane4 = linecache.getline(filen,21)
        lane5 = linecache.getline(filen,24)
        lane6 = linecache.getline(filen,27)
        lane7 = linecache.getline(filen,30)
        lane8 = linecache.getline(filen,33)
        return lane1,lane2,lane3,lane4,lane5,lane6,lane7,lane8




print parse(file1)[0].split(",")[0:5]
