# plot two graphs on same plot for comparison

#####
# Usage: python alt_combo_plot.py <folder1> <phage1> <bact1> <folder2> <phage2> <bact2>
# where folder1 and folder2 are run conditions to be compared (may be same), phage1 and phage2 are p1, bact1 and bact2 are p2 for respective run conditions
# for example, python alt_combo_plot.py alt_run2 0.1 1.0 alt_run3 0.1 1.0 plots comparison plots for same environments for run conditions 2 and 3 where the phage degradation rate is the same but the bacterial degradation rate differs (0.1 and 1.0).
#####

import numpy as np
import matplotlib.pyplot as plt
import os
import sys

folder = (sys.argv[1])
p1 = sys.argv[2] # phage environment
p2 = sys.argv[3] # bacterial environment

folder1 = str(sys.argv[4])
p1a = sys.argv[5] # 2nd phage environment
p2a = sys.argv[6] # 2nd bacterial environment

moi_range = 100

# print p1, p2, p1a, p2a
opt_plyso = [0.0 for x in xrange(moi_range)]
for x in xrange(moi_range):
	# print x
	fname = folder + '/p1_' + str(p1) + ',p2_' + str(p2) + '/moi_' + str(0.01*(x+1)) + '.csv'
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
plt.plot(np.array([0.01*(x+1) for x in xrange(moi_range)]),opt_plyso, 'r')

opt_plyso1 = [0.0 for x in xrange(moi_range)]
for x in xrange(moi_range):
	# print x
	fname1 = folder1 + '/p1_' + str(p1a) + ',p2_' + str(p2a) + '/moi_' + str(0.01*(x+1)) + '.csv'
	with open(fname1) as f1:
		diff1 = 1000000
		for lines1 in f1:
			plyso1 = float(lines1.rstrip().split(',')[0])
			final_moi1 = float(lines1.rstrip().split(',')[1])
			# print plyso
			# print final_moi
			if np.abs(1- final_moi1) < diff1:
				opt_plyso1[x] = plyso1
				# print "new opt", plyso1
				diff1 = np.abs(1 - final_moi1)

plt.ylim(0,1)
plt.plot(np.array([0.01*(x+1) for x in xrange(moi_range)]),opt_plyso1, 'b')
plt.suptitle('r - ' + folder +'/p1:'+str(p1)+',p2:'+str(p2)+'= '+str(np.trapz(opt_plyso, np.array([0.01*(x+1) for x in xrange(moi_range)])))+';    b - ' + folder1 + '/p1:'+str(p1a)+',p2:'+str(p2a)+'= '+str(np.trapz(opt_plyso1, np.array([0.01*(x+1) for x in xrange(moi_range)]))))
# plt.suptitle('p1=0.9, p2=0.1')

directory = 'graphs'
if not os.path.exists(directory):
	os.makedirs(directory)

imagefile = directory + '/' + folder + '-p1_' + str(p1) + ',p2_' + str(p2) + ';' + folder1 + '-p1_' + str(p1a) + ',p2_' + str(p2a) + '.png'
if os.path.exists(imagefile):
	os.remove(imagefile)

plt.savefig(imagefile)