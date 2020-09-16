#!/bin/python3
import sys
import os
import re

file1_ins = {}
file2_ins = {}
all_ins = []
new_ins = []
dis_ins = []
ins_diff = {}

if len(sys.argv) < 3:
	print("usage: ./cmpins.py file1(without '.ins') file2")
	sys.exit(-1)

file1 = sys.argv[1] + ".ins"
file2 = sys.argv[2] + ".ins"

if not os.path.exists(file1):
	print(file1 + " not found! try to creat it")
	os.system("./getins.py" + " %s"%(sys.argv[1]))
if not os.path.exists(file2):
	print(file2 + " not found! try to creat it")
	os.system("./getins.py" + " %s"%(sys.argv[2]))
	
if not os.path.exists(file1) and os.path.exists(file1):
	print(file1 + " or "+ file2 + " not exist!")
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
			if "-new" in sys.argv:
				new_ins.append(ins)
# 计算指令出现次数差异
for ins in all_ins:
	times1 = file1_ins[ins] if ins in file1_ins else 0
	times2 = file2_ins[ins] if ins in file2_ins else 0
	ins_diff[ins] = times2 - times1

diff_sorted = sorted(ins_diff.items(), key=lambda x:abs(x[1]), reverse=True)

difffile = sys.argv[1] + "_" + sys.argv[2] + ".diff"
file=open(difffile,'w')

for ins_deta in diff_sorted:
	if ins_deta[1] != 0:
		if ins_deta[0] not in file1_ins:
			file.write("{: <15}".format(ins_deta[0])+"\t" + str(ins_deta[1]) +" (new)\n" )
		elif ins_deta[0] not in file2_ins:
			file.write("{: <15}".format(ins_deta[0])+"\t" + str(ins_deta[1]) +" (disapper)\n" )
		else:
			file.write("{: <15}".format(ins_deta[0]) + "\t" + str(ins_deta[1]) +"\n" )

# 出现了哪些新指令
if "-new" in sys.argv:
	file.write("\n\n" + str(len(new_ins)) + " kinds of new instruction:\n")
	for ins in new_ins:
		file.write("{: <15}".format(ins)+"\t" + str(ins_diff[ins]) +"\n" )
		
# 出现了哪些新指令
if "-dis" in sys.argv:
	for ins in file1_ins.keys():
		if ins not in file2_ins.keys():
			dis_ins.append(ins)
	file.write("\n\n" + str(len(dis_ins)) + " kinds of instruction disapper:\n")
	for ins in dis_ins:
		file.write("{: <15}".format(ins)+"\t" + str(ins_diff[ins]) +"\n" )
file.close()




