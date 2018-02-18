import bitalino
import numpy
import time
from utils import procACC


macAddress = "/dev/tty.BITalino-13-54-DevB"
   
device = bitalino.BITalino(macAddress)
time.sleep(1)

srate = 100
nframes = 100
threshold = 5
acc_idx = -1
lux_idx = -2

device.start(srate, [4,5])
print ("START")


try:
    while True:
        
        state = device.state()
        
        data = device.read(nframes)        
        if numpy.mean(data[:, 1]) < 1: break

        acc_data = data[:, acc_idx]


        lux_data = data[:, lux_idx]
        
        processing = procACC(acc_data,lux_data)
        
        toggle = 1-state['digitalChannels'][2]
        
        if processing in ['True']:
            device.trigger([toggle, 0])
       

finally:
    print ("STOP")
    device.stop()
    device.close()