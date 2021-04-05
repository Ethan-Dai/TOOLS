#!/usr/bin/python3
import sys
import os

if not len(sys.argv) == 3:	
	print("usage: sizecmp [before] [after]")
	sys.exit(-1)

if not os.path.exists(sys.argv[1]) and os.path.exists(sys.argv[2]):
	print(sys.argv[1] + " or "+ sys.argv[2] + " not exist!")
	sys.exit(-1)
else:
	before_file = sys.argv[1]
	after_file = sys.argv[2]

def get_size(file):
	sec_size = {}
	for line in open(file):
		temp = ' '.join(line.split()) #去除多余空格
		lineArr = temp.split(' ')  #以空格作为分隔符，对这行进行分解
		if (len(lineArr)) > 1 and "0x" in lineArr[1]:
			sec_size[lineArr[0]] = int(lineArr[1], 16)
	return sec_size

sec_size0 = get_size(before_file)
sec_size1 = get_size(after_file)

print("{: <20}".format("section")+"\t" + "size_delta(KB)")
for sec in sec_size1.keys():
	delta = sec_size1[sec] - sec_size0[sec]
	if delta != 0:
		delta_kb = round(delta/1024,2)
		per = round(100 * delta / sec_size0[sec], 2)
		print("{: <20}".format(sec)+ "\t" + str(delta_kb) + " (" + str(per) + "%)")

