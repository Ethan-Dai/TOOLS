#!/bin/python3
import sys
import os
import re

file1_ins = {}
file2_ins = {}
all_ins = []
ins_diff = {}

if len(sys.argv) < 3:
	print("usage: ./cmpins.py file1 file2")
	sys.exit(-1)

if os.path.exists(sys.argv[1]) and os.path.exists(sys.argv[1]) :
	file1 = sys.argv[1]
	file2 = sys.argv[2]
else:
	print("file not exist!")
	sys.exit(-1)

for line in open(file1):
	a_z = re.findall(r"^[a-z]+", line)
	if len(a_z) == 1:
		ins = a_z[0]
		nums = re.findall(r"[0-9]+$", line)
		file1_ins[ins] = int(nums[0])
		all_ins.append(ins)

for line in open(file2):
	a_z = re.findall(r"^[a-z]+", line)
	if len(a_z) == 1:
		ins = a_z[0]
		nums = re.findall(r"[0-9]+$", line)
		file2_ins[ins] = int (nums[0])
		if ins not in all_ins:
			all_ins.append(ins)

for ins in all_ins:
	times1 = file1_ins[ins] if ins in file1_ins else 0
	times2 = file2_ins[ins] if ins in file2_ins else 0
	ins_diff[ins] = times2 - times1

diff_sorted = sorted(ins_diff.items(), key=lambda x:x[1], reverse=True)
difffile = file1 + file2 + ".diff"
file=open(difffile,'w')
for ins_deta in diff_sorted:
	if ins_deta[0] not in file1_ins:
		file.write("{: <15}".format(ins_deta[0])+"\t" + str(ins_deta[1]) +" (new)\n" )
	elif ins_deta[0] not in file2_ins:
		file.write("{: <15}".format(ins_deta[0])+"\t" + str(ins_deta[1]) +" (disapper)\n" )
	else:
		file.write("{: <15}".format(ins_deta[0])+"\t" + str(ins_deta[1]) +"\n" )





