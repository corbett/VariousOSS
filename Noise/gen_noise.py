import wave
import random
import math
#setup
duration=10 #seconds
samplerate = 41000 #Hz
noisefile=wave.open('noise.wav','wb')
#(nchannels, sampwidth, framerate, nframes, comptype, compname),
noisefile.setparams((1, 2, samplerate*4, duration*samplerate, 'NONE', 'noncompressed'))

#generating signal
signal=map(lambda x: random.random(),range(duration*samplerate))
output=''.join(map(lambda x: wave.struct.pack('d',x),signal))

#writing file
noisefile.writeframes(output)

