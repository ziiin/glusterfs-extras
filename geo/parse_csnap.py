#!/usr/bin/python

import sys
import os

def parse (csnapFile, desPath = None):
    # open csnap file
    fToParse = open(csnapFile, 'r')
    destFile = None
    if desPath == None:
        destFile = "CHANGELOG.SNAP"
    else:
        destFile = os.path.join(desPath, "CHANGELOG.SNAP")

    fParsed = open (destFile, 'w')
    header = fToParse.readline()
    print "HEADER:", header

    while (True):
        fopDetail = fToParse.read(38)
        if len (fopDetail) == 0:
            break
        print "fop Detail: ", fopDetail
        parsedDetail = ".gfid/" + fopDetail[1:-1] + '\n'
        print "parsed Detail : ", parsedDetail
        fParsed.write (parsedDetail)

parse ("/export1/v1/b1/.glusterfs/changelogs/csnap/CHANGELOG.SNAP" , "/home/ajha")

# [TODO]
'''
Add usage-detail
Add errors, like existing csnap file or read write exceptions
Handle all exception
'''
