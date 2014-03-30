import numpy as np
import re

note = 'c6'

m = re.search('\w\d', note)
m = m.group(0)


if m[-1]=='0':
    note = m[0].upper()+ m[0].upper()+ m[0].upper()

if m[-1]=='1':
    note = m[0].upper()+ m[0].upper()

if m[-1]=='2':
    note = m[0].upper()

if m[-1]=='3':
    note = m[0]

if m[-1]=='4':
    note = m[0]+"'"

if m[-1]=='5':
    note = m[0]+2*"'"

if m[-1]=='6':
    note = m[0]+3*"'"

if m[-1]=='7':
    note = m[0]+4*"'"

if m[-1]=='8':
    note = m[0]+5*"'"

if m[-1]=='9':
    note = m[0]+6*"'"

if m[-1]=='10':
    note = m[0]+7*"'"


print note
