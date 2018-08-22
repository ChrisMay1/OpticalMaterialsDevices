from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

SMFBeam = True
LensBeam = True
p3 = False
if SMFBeam:
	fname = 'BeamData.txt'

	f = np.loadtxt(fname, 'float')
	z = f[:,1] # mm
	x_width = f[:,2] # micron
	y_width = f[:,3] # micron
	
	xfit = np.polyfit(z,x_width,2)
	yfit = np.polyfit(z,y_width,2)
	
	px = np.poly1d(xfit)
	py = np.poly1d(yfit)
	
	zfit = np.linspace(min(z),max(z),100)
	
	plt.figure()
	plt.plot(z,x_width, '.', label = r'$w_x(z)$')
	plt.plot(z,y_width,'.', label = r'$w_y(z)$')
	plt.plot(zfit,px(zfit),'--',label = r'$w_x(z)$= %.2e $z^2$ + %.2e z + %.2e'%(px[2],px[1],px[0]))
	plt.plot(zfit,py(zfit),'--',label = r'$w_y(z)$=%.2e $z^2$ +%.2e z + %.2e'%(py[2],py[1],py[0]))
	plt.legend(title = 'Beam Width')
	plt.xlabel('Stage Position (mm)')
	plt.ylabel(r'Beam waist w(z) ($\mu m$)')
	plt.title('Beam waist through SMF')
	plt.show()
	w0 = 10*px[1]/px[2]
	print np.pi*w0**2/632e-3
if LensBeam:
	fname = 'LensBeam.txt'

	f = np.loadtxt(fname, 'float')
	z = 155 + f[:,1]
	x_width = f[:,2]
	y_width = f[:,3]

	xfit = np.polyfit(z[3:],x_width[3:],1)
	yfit = np.polyfit(z[3:],y_width[3:],1)

	px = np.poly1d(xfit)
	py = np.poly1d(yfit)
	z0 = 130640
	w0 = 160
	zfit = np.linspace(z[3],max(z),100)
	zt = np.arange(-220,220,1e-2)
	w = w0*np.sqrt(1 + (zt-155/z0)**2)
	plt.figure()
	plt.plot(185+zt,w,label = r'$w(z) = w_0 \sqrt{1 + \frac{z}{z_0}}$')
	plt.plot(z,x_width, '.', label = r'$w_x(z)$')
	plt.plot(z,y_width, '.', label = r'$w_y(z)$')
	# ~ plt.plot(zfit, px(zfit), '--',label = r'$w_x(z)$=%dz + %d'%(px[1],px[0]))
	# ~ plt.plot(zfit, py(zfit), '--',label = r'$w_y(z)$=%dz + %d'%(py[1],py[0]))
	plt.xlabel('Stage Distance from Lens (mm)')
	plt.ylim([0,2000])
	plt.xlim([155,225])
	plt.ylabel(r'Beam Waist $w(z)$ $(\mu m)$')
	plt.title('Beam Waist through 200mm lens)')
	plt.legend()
	plt.show()

if p3:
	fname = 'Divergence_easy.txt'
	f = np.loadtxt(fname)
	z = f[:,0]
	x_width = f[:,1]
	y_width = f[:,2]

	plt.figure()
	plt.plot(z,x_width,'.-', label = 'x')
	plt.plot(z,y_width,'.-', label = 'y')
	plt.xlabel('Stage Position (mm)')
	plt.ylabel(r'Beam Divergence $(\mu m)$')
	plt.title('Beam Divergence as a function of stage position')
	plt.legend(title = 'coordinate')
	plt.show()
