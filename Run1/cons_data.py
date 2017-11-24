import numpy as np
import sys
import warnings

#####
# Usage: python cons_data.py <arg>
# where <arg> for values 0 to 10 refers to (y-intercept of line)*10
# and for values 11 and 12 refers to y = x^2 and y = sqrt(x) respectively
# e.g. python cons_data.py 4 provides the summary for the curve y=0.4+0.6x
#####

# p1: Probability of good environment for phage
#  p2: Probability of good environment for bacteria
p1 = 0.3
p2 = 0.2
phagecount = []
bactcount = []

fname = ""
# read file names

if int(str(sys.argv[1])) == 0:
	fname = 'p' + str(p1) + 'q' + str(p2) + "/result_0.0+1.0x.csv"
if int(str(sys.argv[1])) == 1:
	fname = 'p' + str(p1) + 'q' + str(p2) + "/result_0.1+0.9x.csv"
if int(str(sys.argv[1])) == 2:
	fname = 'p' + str(p1) + 'q' + str(p2) + "/result_0.2+0.8x.csv"
if int(str(sys.argv[1])) == 3:
	fname = 'p' + str(p1) + 'q' + str(p2) + "/result_0.3+0.7x.csv"
if int(str(sys.argv[1])) == 4:
	fname = 'p' + str(p1) + 'q' + str(p2) + "/result_0.4+0.6x.csv"
if int(str(sys.argv[1])) == 5:
	fname = 'p' + str(p1) + 'q' + str(p2) + "/result_0.5+0.5x.csv"
if int(str(sys.argv[1])) == 6:
	fname = 'p' + str(p1) + 'q' + str(p2) + "/result_0.6+0.4x.csv"
if int(str(sys.argv[1])) == 7:
	fname = 'p' + str(p1) + 'q' + str(p2) + "/result_0.7+0.3x.csv"
if int(str(sys.argv[1])) == 8:
	fname = 'p' + str(p1) + 'q' + str(p2) + "/result_0.8+0.2x.csv"
if int(str(sys.argv[1])) == 9:
	fname = 'p' + str(p1) + 'q' + str(p2) + "/result_0.9+0.1x.csv"
if int(str(sys.argv[1])) == 10:
	fname = 'p' + str(p1) + 'q' + str(p2) + "/result_1.0+0.0x.csv"
if int(str(sys.argv[1])) == 11:
	fname = 'p' + str(p1) + 'q' + str(p2) + "/result_x2.csv"
if int(str(sys.argv[1])) == 12:
	fname = 'p' + str(p1) + 'q' + str(p2) + "/result_xsqrt.csv"


with open(fname) as f:
	for line in f:
		winner = int(line.rstrip().split(',')[0])
		time = long(line.rstrip().split(',')[1])
		if winner == 0:
			phagecount.append(time)
		if winner == 1:
			bactcount.append(time)

with warnings.catch_warnings():
	warnings.simplefilter("ignore", category=RuntimeWarning)
	print "Mean of bact", "StdVar of bact", "Mean of phage", "StdVar of phage"
	print np.mean(bactcount), np.std(bactcount), np.mean(phagecount), np.std(phagecount)
