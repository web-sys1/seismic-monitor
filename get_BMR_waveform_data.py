from obspy.clients.fdsn import Client
from obspy import UTCDateTime
from obspy import read
import matplotlib.pyplot as plt   # matplotlib and its pyplot sub-package is used for plotting
import numpy as np                # numpy is used for numerical computing and with arrays


NIEP_client = Client("NIEP")

t1 = UTCDateTime.now()

start = t1 - 60*60*12

endtime = start + 60*60*12

wave1.filter("lowpass", freq=0.1, corners=2)
wave1 = NIEP_client.get_waveforms('RO', 'BMR', '--', 'BHZ', start.replace(minute=0, second=1), endtime)
wave1.plot(type='dayplot', interval=60, right_vertical_labels=True, vertical_scaling_range=3e3,
           one_tick_per_line=True, color=['k', 'r', 'b', 'g'], show_y_UTC_label=True, outfile='public/waveforms/RO/RO_12H_BMR_BHZ.png')
