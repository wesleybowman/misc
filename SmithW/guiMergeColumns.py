from PySide.QtCore import *
from PySide.QtGui import *
import numpy as np
import sys
import os

app = QApplication(sys.argv)

# ----- start your widget test code ----
caption = 'Open File'

# use current/working directory
directory = './'
filenames = QFileDialog.getOpenFileNames(None, caption, directory)[0]

''' For all the files chosen, import them and save them as a txt file '''
for filename in filenames:

    saveAs, ext=os.path.splitext(filename)
    saveAs = '{}.txt'.format(saveAs)

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

''' Close '''
sys.exit( app.processEvents())
