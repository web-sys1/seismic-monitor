
from obspy.clients.fdsn import Client
from obspy import UTCDateTime
import os

client = Client("NIEP")

t1 = UTCDateTime.now()

start = t1 - 60*60*12

endtime = start + 60*60*12

wave1 = client.get_waveforms('RO', 'BUR01', '--', 'HNZ', start.replace(minute=0, second=1), endtime)
wave1.filter("lowpass", freq=0.1, corners=2)
wave1.plot(type='dayplot', interval=60, right_vertical_labels=False, vertical_scaling_range=5e3,
           one_tick_per_line=True, color=['k', 'r', 'b', 'g'], show_y_UTC_label=False, outfile='public/waveforms/RO/RO_12H_BUR01_HNZ.png')
