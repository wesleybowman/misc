import numpy as np

filename='GdVO4_0pcYbSmp1_11June2013.MDI'

with open('filename') as f:
    lines=f.readlines()

c=[]

''' this is crap, fix it '''
for line in lines:
    x=line.split('\r\n')
    c.append(x)


