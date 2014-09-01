#!/usr/bin/python

import sys
import os
'''
Usage: python parse_csnap.py <brick_path> [<destination-path>]
'''
def parse (csnapFile, desPath = None):
    # open csnap file
    fToParse = open(csnapFile, 'r')
    destFile = None
    if desPath == None:
        destFile = "CHANGELOG.SNAP"
    else:
        destFile = os.path.join(desPath, "CHANGELOG.SNAP")

    print "Parsing CSNAP file %s to location %s" % (csnapFile, desPath)
    try:
        fParsed = open (destFile, 'w')
    except OSError :
        print "Unable to open: ", destFile
        sys.exit(0)
    header = fToParse.readline()
    #print "HEADER:", header

    while (True):
        try:
            fopDetail = fToParse.read(38)
            if len (fopDetail) == 0:
                break
            #print "fop Detail: ", fopDetail
            parsedDetail = ".gfid/" + fopDetail[1:-1] + '\n'
            #print "parsed Detail : ", parsedDetail
            fParsed.write (parsedDetail)
        except OSError:
            print "Unable to update Parsed CSNAP file"
            sys.exit(0)

def main ():
    if len (sys.argv) < 2:
        print "Usage: python parse_csnap.py <brick_path> [<destination-path>]"
        sys.exit(0)
    brickPath = str (sys.argv[1])
    csnapFile = os.path.join (brickPath,\
                ".glusterfs/changelogs/csnap/CHANGELOG.SNAP")
    print "Cnapath : ", csnapFile
    if len (sys.argv) == 3:
        desPath = str (sys.argv[2])
        parse (csnapFile, desPath)
    else:
        parse (csnapFile)

if __name__ == "__main__":
    main()
