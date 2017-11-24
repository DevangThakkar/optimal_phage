#####
# Usage: python script_19-09.py <arg>
# where <arg> for values 0 to 10 refers to (y-intercept of line)*10
# and for values 11 and 12 refers to y = x^2 and y = sqrt(x) respectively
#####

#  Notations followed:
# 
#  Nb,h: Number of healthy bacteria
#  Nb,i: Number of infected bacteria
#  Np,free: Number of free phage
#  Np,lyso: Number of lysogenised phage
#  r: Normal growth rate of cell division
#  a: Burst rate for phage during lysis
#  MoI: Assume MoI to be less than 1 for now
#  p1: Probability of good environment for phage
#  p2: Probability of good environment for bacteria
#  lambda_b: Decay rate for bacteria in bad periods
#  lambda_p: Decay rate for phage in bad periods
#  lambda_p,static: Decay rate of phage in good periods

#  assume poisson process for decay of bacteria and phages

#  P(lyso): Probability of the phage choosing lysogeny
#  T: time of simulation

import numpy as np
import math
import sys

N_bh = 1000000L
N_bi = 0L
N_btot = N_bi + N_bh

N_bh_arr = np.array([])
N_bi_arr = np.array([])
N_btot_arr = np.array([])

N_pfree = 10L
N_plyso = 0L
N_ptot = N_pfree + N_plyso

N_pfree_arr = np.array([])
N_plyso_arr = np.array([])
N_ptot_arr = np.array([])

r = 1
a = 10
moi = (1.0*N_pfree)/N_bh

p1 = 0.3 # phage
p2 = 0.2 # bacteria

lambda_b = 0.01
lambda_p = 1
lambda_pstatic = lambda_p/100 

t = 10000
# print N_ptot
# print moi




step = 1
env_p = []
env_b = []
temp = []
# create phage environment step seconds at a time

for i in xrange(int(t/step)):
	r1 = np.random.rand()
	if r1 < p1:
		temp.append(1)
	else:
		temp.append(0)
temp = np.array(temp)

for item in xrange(int(t/step)):
	for item2 in xrange(step):
		env_p.append(temp[item])
env_p = np.array(env_p)

'''
print "phage"
for item in env_p:
	if item == 1:
		print "^",
	else:
		print "_",
print ""
'''

temp = []
# create bacteria environment step seconds at a time

for i in xrange(int(t/step)):
	r2 = np.random.rand()
	if r2 < p2:
		temp.append(1)
	else:
		temp.append(0)
temp = np.array(temp)

for item in xrange(int(t/step)):
	for item2 in xrange(step):
		env_b.append(temp[item])
env_b = np.array(env_b)

'''
print "bacteria"
for item in env_b:
	if item == 1:
		print "^",
	else:
		print "_",
print ""
'''



timetaken = 0
winner = 0

for i in xrange(t):
	timetaken = i
	if int(str(sys.argv[1])) == 0:
		p_lyso = 0.0 + min(moi,1)*1.0
	if int(str(sys.argv[1])) == 1:
		p_lyso = 0.1 + min(moi,1)*0.9
	if int(str(sys.argv[1])) == 2:
		p_lyso = 0.2 + min(moi,1)*0.8
	if int(str(sys.argv[1])) == 3:
		p_lyso = 0.3 + min(moi,1)*0.7
	if int(str(sys.argv[1])) == 4:
		p_lyso = 0.4 + min(moi,1)*0.6
	if int(str(sys.argv[1])) == 5:
		p_lyso = 0.5 + min(moi,1)*0.5
	if int(str(sys.argv[1])) == 6:
		p_lyso = 0.6 + min(moi,1)*0.4
	if int(str(sys.argv[1])) == 7:
		p_lyso = 0.7 + min(moi,1)*0.3
	if int(str(sys.argv[1])) == 8:
		p_lyso = 0.8 + min(moi,1)*0.2
	if int(str(sys.argv[1])) == 9:
		p_lyso = 0.9 + min(moi,1)*0.1
	if int(str(sys.argv[1])) == 10:
		p_lyso = 1.0 + min(moi,1)*0.0
	if int(str(sys.argv[1])) == 11:
		p_lyso = min(moi,1)*min(moi,1)
	if int(str(sys.argv[1])) == 12:
		p_lyso = math.sqrt(min(moi,1))

	print moi
	print N_bh, N_bi
	print N_pfree, N_plyso
	
	if env_p[i] == 1 and env_b[i] == 1:
		# print "1"
		
		N_bh = long(max(N_bh + r*N_bh - N_pfree, 0))
		N_bh_arr = np.append(N_bh_arr, N_bh)
		
		if N_bh == 0:
			break
		
		N_bi = long(N_bi + r*N_bi + p_lyso*N_pfree)
		N_bi_arr = np.append(N_bi_arr, N_bi)
		
		N_plyso = long(N_plyso + r*N_plyso + p_lyso*N_pfree)
		N_plyso_arr = np.append(N_plyso_arr, N_plyso)
		
		N_pfree = long(max(N_pfree + a*(1-p_lyso)*N_pfree - (p_lyso)*N_pfree, 0))
		N_pfree_arr = np.append(N_pfree_arr, N_pfree)
		
		N_btot_arr = np.append(N_btot_arr, N_bi + N_bh)
		N_ptot_arr = np.append(N_ptot_arr, N_pfree + N_plyso)
		
		if N_pfree + N_plyso == 0:
			break
		
	
	if env_p[i] == 1 and env_b[i] == 0:
		# print "2"

		
		N_bh = long(max(N_bh + r*N_bh - N_pfree, 0))
		N_bh_arr = np.append(N_bh_arr, N_bh)
		
		if N_bh == 0:
			break
		
		N_bi = long((N_bi + p_lyso*N_pfree)*np.exp(-lambda_b)) # n new = (n old + x)* exp(-t)
		N_bi_arr = np.append(N_bi_arr, N_bi)
		
		N_plyso = long(N_plyso*np.exp(-lambda_b) + p_lyso*N_pfree)
		N_plyso_arr = np.append(N_plyso_arr, N_plyso)
		
		N_pfree = long(max(N_pfree + a*(1-p_lyso)*N_pfree + 1 * (N_bi + p_lyso*N_pfree)*np.exp(-lambda_b) - (p_lyso)*N_pfree,0))
		N_pfree_arr = np.append(N_pfree_arr, N_pfree)
		
		N_btot_arr = np.append(N_btot_arr, N_bi + N_bh)
		N_ptot_arr = np.append(N_ptot_arr, N_pfree + N_plyso)
		
		if N_pfree + N_plyso == 0:
			break
		
	if env_p[i] == 0 and env_b[i] == 1:
		# print "3"
		
		N_bh = long(max(N_bh + r*N_bh - N_pfree, 0))
		N_bh_arr = np.append(N_bh_arr, N_bh)
		
		if N_bh == 0:
			break
		
		N_bi = long(N_bi + r*N_bi + p_lyso*N_pfree)
		N_bi_arr = np.append(N_bi_arr, N_bi)
		
		N_plyso = long(N_plyso + r*N_plyso + p_lyso*N_pfree)
		N_plyso_arr = np.append(N_plyso_arr, N_plyso)
		
		N_pfree = long(max(N_pfree + a*(1-p_lyso)*N_pfree - (p_lyso)*N_pfree,0)*np.exp(-lambda_p))
		N_pfree_arr = np.append(N_pfree_arr, N_pfree)
		
		N_btot_arr = np.append(N_btot_arr, N_bi + N_bh)
		N_ptot_arr = np.append(N_ptot_arr, N_pfree + N_plyso)
		
		if N_pfree + N_plyso == 0:
			break
		
	if env_p[i] == 0 and env_b[i] == 0:
		# print "4"
		
		N_bh = long(max(N_bh + r*N_bh - N_pfree, 0))
		N_bh_arr = np.append(N_bh_arr, N_bh)
		
		if N_bh == 0:
			break
		
		N_bi = long((N_bi + p_lyso*N_pfree)*np.exp(-lambda_b))
		N_bi_arr = np.append(N_bi_arr, N_bi)
		
		N_plyso = long((N_plyso + p_lyso*N_pfree)*np.exp(-lambda_b))
		N_plyso_arr = np.append(N_plyso_arr, N_plyso)
		
		N_pfree = long(max(N_pfree + a*(1-p_lyso)*N_pfree + (N_bi + p_lyso*N_pfree)*np.exp(-lambda_b) - (p_lyso)*N_pfree,0)*np.exp(-lambda_p))
		N_pfree_arr = np.append(N_pfree_arr, N_pfree)
		
		N_btot_arr = np.append(N_btot_arr, N_bi + N_bh)
		N_ptot_arr = np.append(N_ptot_arr, N_pfree + N_plyso)
		
		if N_pfree + N_plyso == 0:
			break
	
	#update moi
	moi = (1.0*N_pfree)/N_bh

if N_bh == 0:
	winner = 0
elif N_bi == 1:
	winner = 1
else:
	winner = -1
	
# print N_bh, N_bi
# print N_pfree, N_plyso

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


f = open(fname, 'a')
# data = str(winner) + "," + str(timetaken) + "," + str(N_bh) + "," + str(N_bi) + "," + str(N_pfree) + "," + str(N_plyso) + "\n"
data = str(winner) + "," + str(timetaken) + "\n"
f.write(data)
