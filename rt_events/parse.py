#!/usr/bin/python3

import numpy as np
import sys

EVENT_TYPE_TABLE = ('irq_off', 'irq_on')
def parse_rawdata(binfile):
	print("parsing raw data... ", end='')
	events = []
	with open(binfile, 'rb') as f:
		events_pack = np.fromfile(f, dtype='<Q, <Q, <I, <H, <B, <B')
	for event_pack in events_pack:
		time_stamp = event_pack[3] << 32 | event_pack[2]
		event=(event_pack[4], event_pack[5], time_stamp, event_pack[0], event_pack[1])
		events.append(event)
	print("Done")
	
	return events

def gen_txt(events):
	print("generating readable txt file... ", end='')
	txtfile = open("events.txt",'w')
	for event in events:
		txtfile.write("C%d \t%d \t%s  \t%#x <- %#x\n" %event)
	txtfile.close()
	print("Done")

if len(sys.argv) > 2:
	events = parse_rawdata(sys.argv[1])

# generate readable txt file
if "-txt" in sys.argv:
	gen_txt(events)
