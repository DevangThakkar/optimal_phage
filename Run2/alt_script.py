# The aim of this approach is to find for a given value of p1, p2 and moi, a value of P(lyso) that brings the MoI as close to 1 as possible. The logic is this: One way to achieve coexistence is to ensure that the MoI remains equal to 1 so that neither of the two species dominates the other.

# For each value of MoI at an interval of 0.01, calculate the range of average MoI (for 100 runs) of 1 period each for each of P(lyso) at intervals of 0.05; the optimal curve would pass through points that equal MoI = 1 or closest to it.


#####
# Warning: Ensure correct directory name below before run
#
# Usage: python alt_script.py <arg1> <arg2>
# where <arg1> and <arg2> represent the environemntal parameters p1 and p2
# for example, python alt_script.py 0.1 1.0 will run the code for the worst phage environment (p1=0.1) and the best bacterial environment (p2=1.0)
#####

import numpy as np
import os
import time
import sys
start_time = time.time()

iterations = 1000 # number of times the code runs for each value of MoI

moi_range = [x*0.01 for x in xrange(1,101)] # MoI between 0.01 and 1 
plyso_range = [x*0.005 for x in xrange(1,201)] # plyso between 0.005 and 1 

p1 = float(sys.argv[1]) # phage environment
p2 = float(sys.argv[2]) # bacterial environment

r = 1 # bacterial steady growth
a = 10 # amplification factor(burst size)

lambda_p = 2 # degradation factor for phage - phage die
lambda_b = 0.1 # degradation factor for bacteria - bacteria die and lysed bacteria are released as free phages

moi_arr = [0.0 for x in xrange(iterations)]
mean_moi = 0.0

# Ensure correct directory name before run
base_folder = 'alt_run'

for moi in moi_range:
	for plyso in plyso_range:
		for x in xrange(iterations):
			
			# create the environment
			r1 = np.random.rand()
			if r1 < p1:
				envp = 1
			else:
				envp = 0

			r2 = np.random.rand()
			if r2 < p2:
				envb = 1
			else:
				envb = 0

			# initialise populations
			N_bh = 10000
			N_pfree = N_bh*moi
			N_bi = 0

			if envp == 1 and envb == 1:
				
				N_bh = long(max(N_bh + r*N_bh - N_pfree, 0))
				N_bi = long(N_bi + r*N_bi + plyso*N_pfree)
				N_pfree = long(max(N_pfree + a*(1-plyso)*N_pfree - (plyso)*N_pfree, 0))

			if envp == 1 and envb == 0:
				
				N_bh = long(max(N_bh + r*N_bh - N_pfree, 0))
				N_bi = long((N_bi + plyso*N_pfree)*np.exp(-lambda_b))
				N_pfree = long(max(N_pfree + a*(1-plyso)*N_pfree + 1 * (N_bi + plyso*N_pfree)*np.exp(-lambda_b) - (plyso)*N_pfree,0))

			if envp == 0 and envb == 1:
				
				N_bh = long(max(N_bh + r*N_bh - N_pfree, 0))
				N_bi = long(N_bi + r*N_bi + plyso*N_pfree)
				N_pfree = long(max(N_pfree + a*(1-plyso)*N_pfree - (plyso)*N_pfree,0)*np.exp(-lambda_p))

			if envp == 0 and envb == 0:
				
				N_bh = long(max(N_bh + r*N_bh - N_pfree, 0))
				N_bi = long((N_bi + plyso*N_pfree)*np.exp(-lambda_b))
				N_pfree = long(max(N_pfree + a*(1-plyso)*N_pfree + (N_bi + plyso*N_pfree)*np.exp(-lambda_b) - (plyso)*N_pfree,0)*np.exp(-lambda_p))

			# update moi
			moi_arr[x] = (1.0*N_pfree/(N_bh+1))

		# calculate mean moi over all iterations
		mean_moi = np.mean(moi_arr)

		folder1 = 'p1_' + str(p1) + ',p2_' + str(p2)
		directory = base_folder + '/' + folder1

		# create directory if not exists
		if not os.path.exists(directory):
			os.makedirs(directory)
		
		fname = directory + '/moi_' + str(moi) + '.csv'
		f = open(fname, 'a')
		# data = str(winner) + "," + str(timetaken) + "\n"
		f.write(str(plyso) + ',' + str(mean_moi) + '\n')
		f.close()
		
		# reinitialise moi array and moi
		moi_arr = [0.0 for x in xrange(iterations)]
		mean_moi = 0.0

print("--- %s seconds ---" % (time.time() - start_time))
