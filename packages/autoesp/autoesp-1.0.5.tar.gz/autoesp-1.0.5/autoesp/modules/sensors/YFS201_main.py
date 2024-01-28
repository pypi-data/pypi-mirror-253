# Program to read flow sensor and display flow rate in Serial Monitor.
from machine import Pin
import time

print("Running as main code.")

flow_frequency=0
flow_rate=0
lastcallTime=0
pin_number = 1

pin = Pin(pin_number, Pin.IN, Pin.PULL_UP)

def callback(pin):
    global flow_frequency
    flow_frequency=flow_frequency+1

pin.irq(trigger=Pin.IRQ_RISING, handler=callback)

while True:
    if ((time.ticks_ms()-lastcallTime) > 1000):     #if time interval is more a than 1 second
        flow_rate = (flow_frequency * 60 / 7.5)     #flowrate in L/hour= (Pulse frequency x 60 min) / 7.5 
        flow_frequency = 0                          # Reset Counter
        lastcallTime=time.ticks_ms()
        print(f"Flow Rate={flow_rate} Litres/Hour") #print(flow_rate)
