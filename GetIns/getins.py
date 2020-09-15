#!/bin/python3
import sys
import os
import re

readlines = 0
all_ins = {}

if len(sys.argv) < 2:
	print("usage: ./getins.py file")
	sys.exit(-1)

if os.path.exists(sys.argv[1]):
	inputfile = sys.argv[1]
else:
	print("file not exist!")
	sys.exit(-1)

#反汇编
dumpfile = inputfile+".dump"
ans="Y"
if os.path.exists(dumpfile):
	ans = input(".dump file detected, need update? [Y/n]: ")
if ans != "n":
	os.system("llvm-objdump -d %s > %s" %(inputfile, dumpfile))
else:
	print("warning: .dump file not update!")

#截取汇编指令所在列
cutfile = inputfile+".cut"
ans="Y"
if os.path.exists(cutfile):
	ans = input(".cut file detected, need update? [Y/n]: ")
if ans != "n":
	os.system("cut -f 2 %s > %s" %(dumpfile, cutfile))
else:
	print("warning: .cut file not update!")

for line in open(cutfile):
	readlines = readlines + 1
	a_z = re.findall(r"^[a-z]+$", line) #检查是否为汇编指令
	if len(a_z) == 1:
		ins = a_z[0]
		if ins in all_ins:
			all_ins[ins] = all_ins[ins] +1
		else:
			all_ins[ins] = 1
ins_times=sorted(all_ins.items(), key=lambda x:x[0])
msg = str(len(ins_times)) + " kinds of instruction find in " + str(readlines) + " lines:\n"
print(msg)
insfile = inputfile+".ins"
file=open(insfile,'w')  
file.write(msg+"\n") 

for _ins_times in ins_times:
	if '-c' in sys.argv:
		file.write(_ins_times[0]+"\t\t\t"+str(_ins_times[1])+"\n")
	else:
		file.write(str(_ins_times[0])+"\n")
file.close() 
