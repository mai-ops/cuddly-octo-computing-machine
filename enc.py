# enc.py MM June 2017
import sys
import time

t0 = time.clock()

file1_b = bytearray(open(sys.argv[1], 'rb').read())
file2_b = bytearray(open(sys.argv[2], 'rb').read())

sizeM = len(file1_b)
sizeK = len(file2_b)
print "M file size: %i K file size: %i\n"%(sizeM,sizeK)
xord_byte_array = bytearray(sizeM)

for i in range(sizeM):
	xord_byte_array[i] = file1_b[i] ^ file2_b[i%sizeK]

open(sys.argv[3], 'wb').write(xord_byte_array)

t1 = time.clock() - t0
print "Time used: {:10.10f}".format(t1)

    
