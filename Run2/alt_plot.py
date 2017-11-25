import numpy as np
import matplotlib.pyplot as plt
import os
import sys

#####
# Warning: 
# 1) This script eeds alt_script.py to be run first in order to have the moi folders
# 2) Ensure correct directory names below before run
#
# Usage: python alt_plot.py <arg1> <arg2>
# where <arg1> and <arg2> represent the environemntal parameters p1 and p2
# for example, python alt_script.py 0.1 1.0 will plot calculate and plot the graph for the worst phage environment (p1=0.1) and the best bacterial environment (p2=1.0)
#####

p1 = sys.argv[1] # phage environment
p2 = sys.argv[2] # bacterial environment

# print p1, p2
# Ensure correct directory name before run
base_folder = 'alt_run'

opt_plyso = [0.0 for x in xrange(100)]
for x in xrange(100):
	# print x
	fname = base_folder+'/p1_' + str(p1) + ',p2_' + str(p2) + '/moi_' + str(0.01*(x+1)) + '.csv'
	with open(fname) as f:
		diff = 1000000
		for lines in f:
			plyso = float(lines.rstrip().split(',')[0])
			final_moi = float(lines.rstrip().split(',')[1])
			# print plyso
			# print final_moi
			if np.abs(1- final_moi) < diff:
				opt_plyso[x] = plyso
				# print "new opt", plyso
				diff = np.abs(1 - final_moi)

# print opt_plyso
plt.ylim(0,1)
plt.plot(np.array([0.01*(x+1) for x in xrange(100)]),opt_plyso)
plt.suptitle(str(np.trapz(opt_plyso, np.array([0.01*(x+1) for x in xrange(100)]))))

# change directory name before run
directory = base_folder+'/Figures'
if not os.path.exists(directory):
	os.makedirs(directory)

imagefile = directory + '/p1_' + str(p1) + ',p2_' + str(p2) + '.png'
if os.path.exists(imagefile):
	os.remove(imagefile)

plt.savefig(imagefile)