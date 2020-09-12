#!/bin/python3
import sys
import os
import re

readlines = 0
all_ins = []

if len(sys.argv) != 2:
	print("useage: ./getins.py file")
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
if os.path.exists(dumpfile):
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
		if ins not in all_ins:
			all_ins.append(ins)
all_ins.sort()
msg = str(len(all_ins)) + " kinds of instctions find in " + str(readlines) + " lines:\n"
print(msg)
print(all_ins)
insfile = inputfile+".ins"
file=open(insfile,'w')  
file.write(msg+"\n") 
for _ins in all_ins:
	file.write(str(_ins)+"\n")
file.close() 
