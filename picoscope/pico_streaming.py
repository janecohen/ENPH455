# PS4000 Series streaming test
# This example demonstrates how to call the ps4000 driver API functions in order to open a device, setup 2 channels and collects streamed data (1 buffer).
# This data is then plotted as mV against time in ns.

import ctypes # provides # provides C compatible data types
import numpy as np
from picosdk.ps4000 import ps4000 as ps
import matplotlib.pyplot as plt
from picosdk.functions import adc2mV, assert_pico_ok
import time # provides various time-related functions

# Initialize the PicoScope
ps4000a = ps.Device()

# Open the PicoScope device
status = ps4000a.openUnit()
if status != ps.PICO_OK:
    raise Exception("Failed to open the PicoScope: " + str(status))

# Set up the channel
channel = ps.PS4000A_CHANNEL_A
status = ps4000a.setChannel(channel, enabled=True, coupling=ps.PS4000A_DC, range=ps.PS4000A_5V)
if status != ps.PICO_OK:
    raise Exception("Failed to set up the channel: " + str(status))

# Set up the data collection parameters
sample_interval = 1e-6  # Sample interval in seconds (1 µs)
sample_count = 1000  # Number of samples
status = ps4000a.setSimpleTrigger(channel, threshold_mv=100, direction=ps.PS4000A_RISING, delay=0, timeout_ms=100)
if status != ps.PICO_OK:
    raise Exception("Failed to set up trigger: " + str(status))

# Create a buffer to store the data
buffer = np.zeros(sample_count, dtype=np.int16)

# Start data collection
status = ps4000a.runBlock(sample_count, sample_interval)
if status != ps.PICO_OK:
    raise Exception("Failed to start data collection: " + str(status))

# Wait for the data collection to complete
while True:
    ready = ps4000a.isReady()
    if ready:
        break

# Retrieve the data
status, samples = ps4000a.getDataV(channel, buffer, sample_count, downSampleMode=ps.PS4000A_RATIO_MODE_NONE)
if status != ps.PICO_OK:
    raise Exception("Failed to get data: " + str(status))

# Print or process the data as needed
print("Collected data:")
print(samples)

# Close the PicoScope
ps4000a.closeUnit()

