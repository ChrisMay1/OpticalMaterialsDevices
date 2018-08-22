from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

SoS = False
DefEff = False
p3 = False

L,m = np.zeros(6), np.zeros(4)
y1,y2,y3,y4,y5,y6 = np.zeros(4),np.zeros(4),np.zeros(4),np.zeros(4),np.zeros(4),np.zeros(4)

L[:] = [100,90,80,70,60,50]
m[:] = [2,1,1,2]
y1[:] = [17.25,9,8.75,17.25]
y2[:] = [16,8,8,15.75]
y3[:] = [14.5,8,6,13]
y4[:] = [12.25,6,6,11]
y5[:] = [10.5,4.5,5.5,10.25]
y6[:] = [9.5,4.5,4.5,9.5]
lam = 632e-9
f = 80e6

v1 = np.mean(m*lam*f/y1/1e-3)
v2 = np.mean(m*lam*f/y2/1e-3)
v3 = np.mean(m*lam*f/y3/1e-3)
v4 = np.mean(m*lam*f/y4/1e-3)
v5 = np.mean(m*lam*f/y5/1e-3)
v6 = np.mean(m*lam*f/y6/1e-3)


print 185 * 0.27
if SoS:
	m,dy = np.zeros(3),np.zeros(3)
	m[0],m[1],m[2] = [2,1,-1]
	dy = [-28.5e-3,-14.5e-3,15.5e-3]
	lam = 632e-9
	f = 80e6

	v_s = m*lam*f/dy

	print 'Speed of Sound in the Crystal: ', np.mean(v_s),'pm', np.std(v_s)

if DefEff:
	sig0_45 = np.zeros(3)
	sig0_40= np.zeros(3)
	sig0_35= np.zeros(3)
	sig0_30= np.zeros(3)
	sig0_25= np.zeros(3)

	sig1_45= np.zeros(3)
	sig1_40= np.zeros(3)
	sig1_35= np.zeros(3)
	sig1_30= np.zeros(3)
	sig1_25= np.zeros(3)

	sig1_45e= np.zeros(3)
	sig1_40e= np.zeros(3)
	sig1_35e= np.zeros(3)
	sig1_30e= np.zeros(3)
	sig1_25e= np.zeros(3)


	sig0_45[0],sig0_45[1],sig0_45[2] = [1.02,930e-3,645e-3]
	sig0_40[0],sig0_40[1],sig0_40[2] = [1.02,967e-3,718e-3]
	sig0_35[0],sig0_35[1],sig0_35[2] = [1.05,920e-3,611e-3]
	sig0_30[0],sig0_30[1],sig0_30[2] = [850,755e-3,455e-3]
	sig0_25[0],sig0_25[1],sig0_25[2] = [865,820e-3,772e-3]


	sig1_45[0],sig1_45[1],sig1_45[2] = [0,72.2e-3,344e-3]
	sig1_40[0],sig1_40[1],sig1_40[2] = [0,57e-3,274e-3]
	sig1_35[0],sig1_35[1],sig1_35[2] = [0,51.6e-3,188e-3]
	sig1_30[0],sig1_30[1],sig1_30[2] = [0,83.4e-3,180e-3]
	sig1_25[0],sig1_25[1],sig1_25[2] = [0,32.5e-3,125e-3]

	sig1_45e[0],sig1_45e[1],sig1_45e[2] = [0,0.5e-3,2e-3]
	sig1_40e[0],sig1_40e[1],sig1_40e[2] = [0,0.5e-3,1e-3]
	sig1_35e[0],sig1_35e[1],sig1_35e[2] = [0,0.4e-3,1e-3]
	sig1_30e[0],sig1_30e[1],sig1_30e[2] = [0,1.5e-3,2e-3]
	sig1_25e[0],sig1_25e[1],sig1_25e[2] = [0,1.5e-3,2e-3]

	level = np.zeros(3)
	level[0],level[1],level[2] = [0,5,10]

	plt.figure()
	plt.errorbar(level,sig1_45/sig0_45, yerr = sig1_45e, fmt = '.-', label = '45 MHz')
	plt.errorbar(level,sig1_40/sig0_40, yerr = sig1_40e, fmt = '.-', label = '40 MHz')
	plt.errorbar(level,sig1_35/sig0_35, yerr = sig1_35e, fmt = '.-', label = '35 MHz')
	plt.errorbar(level,sig1_30/sig0_30, yerr = sig1_30e, fmt = '.-', label = '30 MHz')
	plt.errorbar(level,sig1_25/sig0_25, yerr = sig1_25e, fmt = '.-', label = '25 MHz')
	plt.xlabel('Driver Level')
	plt.ylabel('Ratio of First Order to Zeroth Order Maximum')
	plt.title('AOM1 Deflection Efficiency')
	plt.legend(title = 'Frequency')
	plt.show()


if p3:
	b1 = np.zeros(3)
	b2 = np.zeros(3)
	b3 = np.zeros(3)
	b4 = np.zeros(3)

	c1 = np.zeros(3)
	c2 = np.zeros(3)
	c3 = np.zeros(3)
	c4 = np.zeros(3)

	f1 = np.zeros(3)
	f2 = np.zeros(3)
	f3 = np.zeros(3)
	f4 = np.zeros(3)

	A = np.zeros(3)
	A[0],A[1],A[2] = [0,-3,-6]

	b1[0],b1[1],b1[2] = [10, 1.2e6, 1.8e6]
	b2[0],b2[1],b2[2] = [10, 1.15e6, 1.7e6]
	b3[0],b3[1],b3[2] = [10, 1.2e6, 1.7e6]
	b4[0],b4[1],b4[2] = [10, 1.2e6, 1.9e6]

	f1[0],f1[1],f1[2] = [10, 1.35e6, 1.9e6]
	f2[0],f2[1],f2[2] = [10, 1.25e6, 1.75e6]
	f3[0],f3[1],f3[2] = [10, 1.25e6, 1.85e6]
	f4[0],f4[1],f4[2] = [10, 1.3e6, 2.1e6]

	c1[0],c1[1],c1[2] = [10, 1.4e6, 2.2e6]
	c2[0],c2[1],c2[2] = [10, 1.2e6, 1.8e6]
	c3[0],c3[1],c3[2] = [10, 1.3e6, 1.9e6]
	c4[0],c4[1],c4[2] = [10, 1.375e6, 2.1e6]

	b = (b1 + b2 + b3 + b4)/4
	f = (f1 + f2 + f3 + f4)/4
	c = (c1 + c2 + c3 + c4)/4
	plt.figure()
	plt.semilogx(b[1:3],A[1:3], '.-', label = 'm = 0, Large Spot')

	plt.semilogx(f[1:3],A[1:3], '.-', label = 'm = 1, Large Spot')

	plt.semilogx(c[1:3],A[1:3], '.-', label = 'm = 0, Small Spot')

	plt.legend()
	plt.xlabel('Modulation Frequency (Hz)')
	plt.ylabel('Intensity (dB)')
	plt.title('-3dB and -6dB Frequencies for different incident beam widths')
	plt.show()
