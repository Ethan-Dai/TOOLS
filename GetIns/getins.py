#!/bin/python3
import sys
import os
import re

dumptool = "llvm-objdump" #Disassembly tool 
inscol = "2" # instruction always appear in one Column

linenum = 0
unknown = 0
all_ins = {}

if len(sys.argv) < 2:
	print("usage: ./getins.py file")
	sys.exit(-1)

if os.path.exists(sys.argv[1]):
	inputfile = sys.argv[1]
else:
	print(sys.argv[1] + " not exist!")
	sys.exit(-1)

#Disassembly the elf file
dumpfile = inputfile+".dump"
ans="Y"
if os.path.exists(dumpfile):
	ans = input(dumpfile + " detected, need update? [Y/n]: ")
if ans != "n":
	os.system(dumptool + " -d %s > %s" %(inputfile, dumpfile))
else:
	print("warning: " + dumpfile + " not update!")

# pick the column that instructions appeared 
cutfile = inputfile+".cut"
ans="Y"
if os.path.exists(cutfile):
	ans = input(cutfile + " detected, need update? [Y/n]: ")
if ans != "n":
	os.system("cut -f " + inscol + " %s > %s" %(dumpfile, cutfile))
else:
	print("warning: " + cutfile + "not update!")

for line in open(cutfile):
	linenum = linenum + 1
	if line == "<unknown>\n":
		unknown = unknown + 1
		print("warning: unknown instruction found in line: " + str(linenum))
	a_z = re.findall(r"^[a-z]+$", line) # check whether it's an instruction
	if len(a_z) == 1:
		ins = a_z[0]
		if ins in all_ins:
			all_ins[ins] = all_ins[ins] +1
		else:
			all_ins[ins] = 1
ins_times=sorted(all_ins.items(), key=lambda x:x[0])
msg = str(len(ins_times)) + " kinds of instruction find in " + str(linenum) + " lines\n"
msg += str(unknown) + " unknown instctions\n"
print(msg)
insfile = inputfile+".ins"
file=open(insfile,'w')  
file.write(msg+"\n") 

for _ins_times in ins_times:
	if '-s' not in sys.argv:
		file.write("{: <15}".format(_ins_times[0])+"\t"+str(_ins_times[1])+"\n")
	else:
		file.write(str(_ins_times[0])+"\n")
file.close() 
