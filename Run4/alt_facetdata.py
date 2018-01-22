#####
# This script creates the data for the facet grid to be created in R
#####

import numpy as np
import sys
import os

p1 = sys.argv[1] # phage environment
p2 = sys.argv[2] # bacterial environment

base_folder = 'alt_run/'
file_name = 'facet_plot/facet_data.txt'

if not os.path.exists(file_name):
	with open(file_name,'w') as f:
		f.write('p1\tp2\tMoI\tP(lyso)\n')
moi_range = 100

opt_plyso = [0.0 for x in xrange(moi_range)]
for x in xrange(moi_range):
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
	with open(file_name,'a') as f:
		f.write('p1='+str(p1)+'\tp2='+str(p2)+'\t'+str(0.01*(x+1))+'\t'+str(opt_plyso[x])+'\n')