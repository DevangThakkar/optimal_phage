import numpy as np
import matplotlib
matplotlib.rcParams.update({'font.size': 16})
from matplotlib import pyplot as pl

moi_range = 200

def plotting(p1):
	arr = [[0.0 for x in xrange(moi_range)] for x in xrange(25)]
	i=-1
	fname = 'points'+str(p1)+'.txt' # read file for required phage environment
	with open(fname, 'r') as f:
		for line in f:
			i+=1
			temp = line.split(',')
			for x in xrange(moi_range):
				arr[i][x] = float(temp[x+2])

	# generate maximum, minimum and trend data points for the entire moi_range
	mean = [0.0 for x in xrange(moi_range)]
	maxi = [0.0 for x in xrange(moi_range)]
	mini = [1.0 for x in xrange(moi_range)]

	for x in xrange(moi_range):
		for y in xrange(25):
			if maxi[x]<arr[y][x]:
				maxi[x] = arr[y][x]
			if mini[x]>arr[y][x]:
				mini[x] = arr[y][x]
			mean[x]+=arr[y][x]
		mean[x]/=25

	return mini, mean, maxi

x = np.linspace(0, 2, moi_range)

pl.clf()
pl.hold(1)
pl.xlabel('MoI')
pl.ylabel('P(lyso)')
lcolor = ['#0000FF', '#FF0000', '#FF0000', '#FF0000', '#FF00FF'] # central line color - choose dark colors
fcolor = ['#6666FF', '#FF7878', '#9494FF', '#FF7878', '#CCCCFF'] # variation area color - choose light colors
for i in [2,8]: # change range as per requirements
	mini, mean, maxi = plotting((i*1.0)/10)
	pl.plot(x, mean, 'k', color=lcolor[int((i*1.0)/2)-1])
	pl.fill_between(x, mini, maxi,
	    alpha=0.2, facecolor=fcolor[int((i*1.0)/2)-1],
	    antialiased=True)

pl.show()