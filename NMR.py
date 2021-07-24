#!/usr/bin/env python

#--------------------------------------------------------------------------------------------#
#Importing python libraries

import numpy as np
import  matplotlib.pyplot as plt
import matplotlib.ticker as tick

#--------------------------------------------------------------------------------------------#
#Defining constants
fnt = 16#Font size for matplotlib plots

hbar = 1.05e-34#Dirac's constant
ratio = 2.675e8#Gyromagnetic ratio
perm = 4*np.pi*1e-7#permativity of free space

B = (perm*ratio*hbar)/2#B_0

#--------------------------------------------------------------------------------------------#
#Question 1(1) - Showing lines of constant magnetic field in space (Fixed Bmag -> vary r and theta)

theta = np.linspace(-2*np.pi,2*np.pi,100)#Creating 100 x-axis values
Bmag = [1e-2,1e-4,1e-5,1e-6]#Selecting 4 differing magnetic fields

#Defining function for the radius as a function of angle and magnetic field size
def radius(Bmag,theta):
    return ((perm*ratio*hbar)/(8*np.pi*Bmag)*(3*np.cos(theta)**2 + 1)**0.5)**(1/3)*1e9

#Generating radius data for each magnetic field
for i in range(len(Bmag)):
    exec(f'r{i} = radius(Bmag[i],theta)')

#Plotting radius against angle for 4 different magentic field
fig, ax = plt.subplots(figsize = (10,8))
plt.plot(theta/(np.pi),r0, '-', label = ' B = 10 mT',color = 'black')
plt.plot(theta/(np.pi),r1, '-', label = 'B = 0.1 mT',color = 'blue')
plt.plot(theta/(np.pi),r2, '-', label = r'B = 10 $\mu$T',color = 'red')
plt.plot(theta/(np.pi),r3, '-', label = r'B = 1 $\mu$ T',color = 'lime')
ax.xaxis.set_major_formatter(tick.FormatStrFormatter('%g $\pi$'))
ax.xaxis.set_major_locator(tick.MultipleLocator(base=1.0))
plt.xlabel(r' $\theta$ [rad]', fontsize = fnt)
plt.ylabel('r [nm]', fontsize = fnt)
plt.minorticks_on()
plt.tick_params(labelsize = fnt)
plt.legend(fontsize = fnt, loc = 'upper right', facecolor = 'white', framealpha=1)
plt.savefig('1_1.png')#Saving as Question 1 part 1
plt.show()

#--------------------------------------------------------------------------------------------#
#Question 1(2) - Dependence of magnetic field components Bx and By on radius (constant theta)

r = np.linspace(1e-10,5e-10,1000)#Array of radius values in metres

a = [0,np.pi/2,np.pi,(3*np.pi)/2]#Constant angle

def bx(a,r):
    return B*(np.cos(a))/(r**3)*(3*(np.cos(a))**2 + 1)**0.5*1e6

def by(a,r):
    return B*(np.sin(a))/(r**3)*(3*(np.cos(a))**2 + 1)**0.5*1e6

for i in range(len(a)):
    exec(f'Bx{i} = bx(a[i],r)')
    exec(f'By{i} = by(a[i],r)')

#Plotting x-axis magentic component with respect to radius
fig = plt.figure(figsize = (10,8))
plt.plot(r*1e9,Bx0, '-', label = r'$\theta$ = 0',color = 'blue')
plt.plot(r*1e9,Bx1, '-', label = r'$\theta$ = $\pi$/2',color = 'green')
plt.plot(r*1e9,Bx2, '-', label = r'$\theta$ = $\pi$',color = 'red')
plt.plot(r*1e9,Bx3, '-', label = r'$\theta$ = 3$\pi$/2',color = 'black')
plt.xlabel(' r [nm]', fontsize = fnt)
plt.ylabel('$B_x$ [$\mu$T]', fontsize = fnt)
plt.minorticks_on()
plt.tick_params(labelsize = fnt)
plt.legend(fontsize = fnt)
plt.savefig('1_21.png')#Saving as Question 1 part 2.1
plt.show()

#Plotting y-axis magentic component with respect to radius
fig = plt.figure(figsize = (10,8))
plt.plot(r*1e9,By0, '-', label = r'$\theta$ = 0',color = 'blue')
plt.plot(r*1e9,By1, '-', label = r'$\theta$ = $\pi$/2',color = 'lime')
plt.plot(r*1e9,By2, '-', label = r'$\theta$ = $\pi$',color = 'red')
plt.plot(r*1e9,By3, '-', label = r'$\theta$ = 3$\pi$/2',color = 'black')
plt.xlabel(' r [nm]', fontsize = fnt)
plt.ylabel('$B_y$ [$\mu$T]', fontsize = fnt)
plt.minorticks_on()
plt.tick_params(labelsize = fnt)
plt.legend(fontsize = fnt)
plt.savefig('1_22.png')#Saving as Question 1 part 2.2
plt.show()

#--------------------------------------------------------------------------------------------#
#Question 2(1) - Solving the Bloch equations in the rotating frame of reference numerically (iterating with time step)

M_0 = 1.4e-6#Initial magnetisation defined outside function for use later

def Mag(B1):
    
    T1 = 100e-3 #Longitudinal relaxation time
    T2 = 10e-3 #Transverse relaxation time
    B0 = 10 #Z-axis static field
    gamma = 6.72e7 #Gyromagnetic ratio of C-13
    
    #initial parameters
    Mzi = 0
    Mxi = 0
    Myi= M_0
    time = []
    timei = 0
    step = 0.0001 #Time step iteration is 0.1 milliseconds
    
    Bx = B1 #Rotating frame of refernece 
    By = 0
    Bz = 0
    
    Mx = []
    My = []
    Mz = []
    
    #While loop to solve first order differential equation with time
    while timei <= 1 :#iterate through to 0.4 seconds
        
        time_new = timei + step
        
        gradMzi = (M_0-Mzi)/T1 + gamma*(Mxi*By - Myi*Bx)
        gradMxi = - (Mxi)/T2 + gamma*(Myi*Bz - Mzi*By)
        gradMyi = - (Myi)/T2 + gamma*(Mzi*Bx - Mxi*Bz)

        Mxi_new = Mxi + gradMxi*step
        Mzi_new = Mzi + gradMzi*step
        Myi_new = Myi + gradMyi*step
        
        Mxi = Mxi_new
        Myi = Myi_new
        Mzi = Mzi_new
    
        Mx.append(Mxi_new)
        My.append(Myi_new)
        Mz.append(Mzi_new)
        
        timei = time_new
        
        time.append(timei)
        
    return Mx, My, Mz, time

#Select 3 different magnetic fields perpendicular to z-axis
Mx, My, Mz, time = Mag(1e-7)
Mx1, My1, Mz1, time1 = Mag(1e-8)
Mx2, My2, Mz2, time2 = Mag(1e-9)

#Plotting each magnetisation component
fig, ax = plt.subplots(figsize = (10,8))
ax.set_xscale('log')
plt.plot(time, np.array(Mx)/M_0, label = '100 nT', color = 'red')
plt.plot(time1, np.array(Mx1)/M_0, label = '10 nT', color = 'blue')
plt.plot(time2, np.array(Mx2)/M_0, label = '1 nT', color = 'green')
plt.xlabel(r' Time [s]', fontsize = fnt)
plt.ylabel("M$_{x'}$ [Am$^{-1}$]", fontsize = fnt)
plt.minorticks_on()
ax.yaxis.set_major_formatter(tick.FormatStrFormatter('%g M$_0$'))
plt.tick_params(labelsize = fnt)
plt.legend(fontsize = fnt, loc = 'best', title = r'B$_1$ Values :', title_fontsize = fnt)
plt.savefig('2_11.png')
plt.show()

fig, ax = plt.subplots(figsize = (10,8))
ax.set_xscale('log')
plt.plot(time, np.array(My)/M_0, label = '100 nT', color = 'red')
plt.plot(time1, np.array(My1)/M_0, label = '10 nT', color = 'blue')
plt.plot(time2, np.array(My2)/M_0, label = '1 nT', color = 'green')
plt.xlabel(r' Time [s]', fontsize = fnt)
plt.ylabel("M$_{y'}$ [Am$^{-1}$]", fontsize = fnt)
plt.minorticks_on()
ax.yaxis.set_major_formatter(tick.FormatStrFormatter('%g M$_0$'))
ax.yaxis.set_major_locator(tick.MultipleLocator(base = 0.2))
plt.ylim(0,1)
plt.tick_params(labelsize = fnt)
plt.legend(fontsize = fnt, loc = 'best', title = r'B$_1$ Values :', title_fontsize = fnt)
plt.savefig('2_12.png')
plt.show()

fig, ax = plt.subplots(figsize = (10,8))
ax.set_xscale('log')
plt.plot(time, np.array(Mz)/M_0, label = '100 nT', color = 'red')
plt.plot(time1, np.array(Mz1)/M_0, label = '10 nT', color = 'blue')
plt.plot(time2, np.array(Mz2)/M_0, label = '1 nT', color = 'green')
plt.xlabel(r' Time [s]', fontsize = fnt)
plt.ylabel("M$_{z'}$ [Am$^{-1}$]", fontsize = fnt)
plt.minorticks_on()
ax.yaxis.set_major_formatter(tick.FormatStrFormatter('%g M$_0$'))
plt.tick_params(labelsize = fnt)
plt.legend(fontsize = fnt, loc = 'best', title = r'B$_1$ Values :', title_fontsize = fnt)
plt.savefig('2_13.png')
plt.show()

#--------------------------------------------------------------------------------------------#
#Question 2(2) - Solving for long time scales and varying transverse magnetic field

B1 = np.linspace(1e-9,1e-6,1000)

Mxinf = []
Myinf = []
Mzinf = []

for i in B1:
    Mx, My, Mz, time = Mag(i)
    Mxinf.append(Mx[-1])
    Myinf.append(My[-1])
    Mzinf.append(Mz[-1])

#Plotting each magnetisation component at t=infinity
fig, ax = plt.subplots(figsize = (10,8))
ax.set_xscale('log')
plt.plot(B1*1e6, Mxinf, color = 'black')
plt.xlabel(r' B$_1$ [$\mu$T]', fontsize = fnt)
plt.ylabel("M$_{x'}(\infty)$ [Am$^{-1}$]", fontsize = fnt)
plt.minorticks_on()
plt.tick_params(labelsize = fnt)
ax.yaxis.set_major_formatter(tick.FormatStrFormatter('%g M$_0$'))
plt.savefig('2_21.png')
plt.show()

fig, ax = plt.subplots(figsize = (10,8))
ax.set_xscale('log')
plt.plot(B1*1e6, np.array(Mzinf)/M_0, color = 'black')
plt.xlabel(r' B$_1$ [$\mu$T]', fontsize = fnt)
plt.ylabel("M$_{z'}(\infty)$ [Am$^{-1}$]", fontsize = fnt)
plt.minorticks_on()
ax.yaxis.set_major_formatter(tick.FormatStrFormatter('%g M$_0$'))
#ax.yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(base = ''))
plt.tick_params(labelsize = fnt)
plt.savefig('2_22.png')
plt.show()

fig, ax = plt.subplots(figsize = (10,8))
ax.set_xscale('log')
plt.plot(B1*1e6, np.array(Myinf)/M_0, color = 'black')
plt.xlabel(r' B$_1$ [$\mu$T]', fontsize = fnt)
plt.ylabel("M$_{y'}(\infty)$ [Am$^{-1}$]", fontsize = fnt)
plt.minorticks_on()
plt.tick_params(labelsize = fnt)
ax.yaxis.set_major_formatter(tick.FormatStrFormatter('%g M$_0$'))
ax.yaxis.set_major_locator(tick.MultipleLocator(base = 0.05))
plt.savefig('2_23.png')
plt.show()
