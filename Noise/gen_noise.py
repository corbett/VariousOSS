import wave
import random
import math
import sys
import getopt

def write_noise(outfile,duration,samplerate):
	#generating signal
	signal=[random.random() for i in range(duration*samplerate)]
	output=''.join([wave.struct.pack('d',x) for x in signal])
	#writing output
	noisefile=wave.open(outfile,'wb')
	noisefile.setparams((1, 1, samplerate*8, duration*samplerate, 'NONE', 'noncompressed'))
	noisefile.writeframes(output)

if __name__ == '__main__':
	#defaults
	duration=10 #seconds
	samplerate = 41000 #Hz
	outfile='noise.wav'
	
	#demoing
	for power in range(2,5):
		samplerate=4*10**power
		outfile='noise'+str(samplerate)+'.wav'
		write_noise(outfile,duration,samplerate)
	
