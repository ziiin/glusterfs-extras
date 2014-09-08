
import sys
import os

'''
This script provides support functionalities while debugging
Gluster/geo-rep issues.

Features:
    getGfid (filePath) : gets gfid of filePath (where filePath is absolute 
                         wrt gluster).
    getXtime (filepath) : gets xtime of filePath.
    getStime (filePath) : gets stime of filePath.
    findGfidInChangelog (gfid) : Finds all fop entries wrt the given gfid in
                                 backend bricks.
'''
def glMount (vol):
    ''' Returns mount path on successful mount, else None. '''
    pass

def glGetBricks (vol):
    ''' Returns list of bricks associated to the volume, else None. '''
    pass

class volume:

    def __init__ (self, vol):
        self.mountPoint = glMount (vol)
        self.brickPaths = glGetBricks (vol)


    def getGfid (filePath):
        ''' Returns gfid of file un ascii uuid format. '''
        pass

    def getXtime (filePath):
        ''' Returns current Xtime of filePath. '''
        pass

    def findGfidInClog (gfid):
        ''' Returns: Info about fop entries corresponding to given gfid.
            
            dict with key as the changelog basename and value as list of
            fop entries.
        '''
        pass
