from obspy.clients.fdsn import Client
from obspy import UTCDateTime
from obspy import read
import matplotlib.pyplot as plt   # matplotlib and its pyplot sub-package is used for plotting
import numpy as np                # numpy is used for numerical computing and with arrays


NIEP_client = Client("NIEP")

t1 = UTCDateTime.now()

start = t1 - 60*60*12
endtime = start + 60*60*12

wave1 = NIEP_client.get_waveforms('RO', 'BUR01', '--', 'HNZ', start.replace(minute=0, second=1), endtime)
wave1.filter('highpass', freq=0.62, corners=1, zerophase=True)
#wave1.filter("bandpass", freqmin=0.62, freqmax=25.00, corners=3, zerophase=False)
wave1.detrend(type='demean')
wave1.detrend(type='linear')
wave1.plot(type='dayplot', interval=60, right_vertical_labels=True,
           vertical_scaling_range=1600,
           one_tick_per_line=True,
           color=['k', 'r', 'b', 'g'],
           show_y_UTC_label=False, outfile='public/waveforms/RO/RO_12H_BUR01_HNZ.png')
