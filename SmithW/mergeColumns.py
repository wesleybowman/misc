from __future__ import division, print_function
import numpy as np
import sys

''' Get input file and output filenames from command line '''
filename=sys.argv[1]
saveAs=sys.argv[2]

''' Load the initial file '''
initialFile=np.loadtxt(filename,skiprows=2,delimiter='\s',dtype=np.str)

''' Manipulate the file so it can be worked with '''
newfile=np.core.defchararray.split(initialFile, sep=None, maxsplit=None)

final=np.array([])

for lists in newfile:
    for number in lists:
        final=np.append(final,number)

''' Convert the values to integers '''
final=final.astype(np.int)

''' Save the file '''
np.savetxt(saveAs,final,fmt='%d')


