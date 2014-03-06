import scipy.io.wavfile as wavfile
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def loadShow(WAV):
    #Load WAV files
    rate, data = wavfile.read(WAV)

    #Plot WAV data
    t = np.arange(len(data[:,0]))*1.0/rate

    plt.plot(t, data[:,0])
    plt.show()

    #Power Spectrum
    p = 20*np.log10(np.abs(np.fft.rfft(data[:2048, 0])))
    f = np.linspace(0, rate/2.0, len(p))

    plt.plot(f, p)
    plt.xlabel("Frequency(Hz)")
    plt.ylabel("Power(dB)")
    plt.show()

    return data

#datascale = loadShow('whistle.wav')

rate, data = wavfile.read('scale.wav')
time = np.arange(len(data[:,0]))*1.0/rate

#Loading in a .txt file, almost the same for csv
spectrum = pd.read_csv('longscalespectrum.txt',delimiter='\t')

x = spectrum['Frequency (Hz)']
y = spectrum['Level (dB)']

#plt.plot(x,y)
#plt.show()


#for i in data[:,0]:
#    #now use i
#    print i


maximums = []
tm = []

for index, value in enumerate(data[:,0]):
    #i = index, j = value
    #print time[index], value

    #Figure out what if statements to use
    try:
        if value<data[index+1, 0] and value>100:
            #print data[index+1, 0]
            maximums.append(data[index+1,0])
            tm.append(time[index+1])
    except IndexError:
        pass


def findMax(maximums,time):
    Max = []
    tm = []

    for index, value in enumerate(maximums):
        try:
            if value<maximums[index+1]:
                Max.append(maximums[index+1])
                tm.append(time[index+1])
        except IndexError:
            pass

    return Max,tm

from scipy.signal import argrelextrema
def findMax2(maximums,tm):
    ind = argrelextrema(maximums,np.greater)
    maximums = maximums[ind]
    tm = tm[ind]

    return maximums, tm


Max, tm = findMax2(data[:,0], time)
for i in xrange(5):
    Max, tm = findMax2(Max, tm)
#Max, tm = findMax(maximums,tm)
#for i in xrange(40):
#    Max, tm = findMax(Max,tm)
#    #Max, tm = findMax(data[:,0],time)
#
#for i in xrange(1):
#    Max, tm = findMax(Max[::-1],tm[::-1])
#
#Max = Max[::-1]
#tm = tm[::-1]

plt.plot(time,data[:,0],'o')
plt.plot(tm,Max,'ro')
#plt.plot(tm4,max4)
plt.show()


