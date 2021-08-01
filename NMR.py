#!/usr/bin/env python

#Importing python libraries

import numpy as np
import  matplotlib.pyplot as plt
import matplotlib.ticker as tick
import os

import func_NMR

#Defining constants
fnt = 16#Font size for matplotlib plots

hbar = 1.05e-34#Dirac's constant
ratio = 2.675e8#Gyromagnetic ratio
perm = 4*np.pi*1e-7#permativity of free space

B = (perm*ratio*hbar)/2#B_0

#Creating folders for output image files
if os.path.isdir('images_NMR_Q1') == True:
    pass#If folder already exists then do nothing to prevent os error
else:
    print('Creating folder named images_NMR_Q1 for data output')
    os.mkdir('images_NMR_Q1')#Create images folder for question 1

#Creating folders for output image files
if os.path.isdir('images_NMR_Q2') == True:
    pass#If folder already exists then do nothing to prevent os error
else:
    print('Creating folder named images_NMR_Q2 for data output')
    os.mkdir('images_NMR_Q2')#Create images folder for question 2

#Question 1(1) - Showing lines of constant magnetic field in space (Fixed Bmag -> vary r and theta)
#Demonstrates the 1/r^3 dependence as reductions in the magnetic field show large radial increases

theta = np.linspace(-2*np.pi,2*np.pi,100)#Creating values for angles between -2pi and 2pi
Bmag = [1e-2,1e-4,1e-5,1e-6]#Selecting 4 differing magnetic field magnitudes

labels_11 = ['B = 10 mT','B = 0.1 mT', r'B = 10 $\mu$T', r'B = 1 $\mu$ T']#Labels for matplotlib plot loop
colours_11 = ['black','blue','red','lime']#Colours for matplotlib plot loop

#Plotting radius against angle for different magentic fields
fig, ax = plt.subplots(figsize = (10,8))#Define figure size
for i in range(len(Bmag)):#Loop through the selected magnetic fields
    plt.plot(theta/(np.pi),func_NMR.radius(Bmag[i],theta), '-', label = labels_11[i], color = colours_11[i])
ax.xaxis.set_major_formatter(tick.FormatStrFormatter('%g $\pi$'))#x-axis as units of pi
ax.xaxis.set_major_locator(tick.MultipleLocator(base=1.0))
plt.xlabel(r' $\theta$ [rad]', fontsize = fnt)
plt.ylabel('r [nm]', fontsize = fnt)
plt.minorticks_on()
plt.tick_params(labelsize = fnt)
plt.legend(fontsize = fnt, loc = 'upper right', facecolor = 'white', framealpha=1)#Setting legend params
plt.savefig('images_NMR_Q1/1_1.png')#Saving as Question 1 part 1
plt.close()#Close this image

#Question 1(2) - Dependence of magnetic field components Bx and By on radius (constant theta)
#Show the direction of the dipole via maxima and minima in the magnetic field

r = np.linspace(1e-10,5e-10,1000)#Array of radius values in metres

a = [0,np.pi/2,np.pi,(3*np.pi)/2]#Angles list

labels_12 = [r'$\theta$ = 0',r'$\theta$ = $\pi$/2',r'$\theta$ = $\pi$',r'$\theta$ = 3$\pi$/2']#Labels for matplotlib plot loop
colours_12 = ['blue','green','red','black']#Colours for matplotlib plot loop

for i in range(1,3):# x and y components (1 and 2)
    fig = plt.figure(figsize = (10,8))

    for j in range(len(a)):#Length of angles list
        if i ==1:
            plt.plot(r*1e9,func_NMR.bx(a[j],r), '-', label = labels_12[j],color = colours_12[j])
        else:
            plt.plot(r*1e9,func_NMR.by(a[j],r), '-', label = labels_12[j],color = colours_12[j])

    plt.minorticks_on()
    plt.tick_params(labelsize = fnt)
    plt.legend(fontsize = fnt)
    plt.xlabel(' r [nm]', fontsize = fnt)
    if i == 1:
        plt.ylabel('$B_x$ [$\mu$T]', fontsize = fnt)
    else:
        plt.ylabel('$B_y$ [$\mu$T]', fontsize = fnt)

    plt.savefig(f'images_NMR_Q1/1_2{i}.png')#Saving image in question 1
    plt.close()#Close this image

#Question 2(1) - Solving the Bloch equations in the rotating frame of reference numerically (iterating with time step)

M_0 = 1.4e-6#Initial magnetisation defined by system characteristics

#Select 3 different magnetic fields perpendicular to z-axis with maximum time 1 second
array = [func_NMR.Mag(1e-7,0.001,10,0.001),func_NMR.Mag(1e-8,0.001,10,0.001),func_NMR.Mag(1e-9,0.001,10,0.001)]

labels_21 = ['100 nT','10 nT','1 nT']
colours_21 = ['red', 'blue', 'green']

#Plotting each magnetisation component
for i in range(0,len(array)):
    fig, ax = plt.subplots(figsize = (10,8))
    ax.set_xscale('log')#Log time axis
    for j in range(0,len(array[i])-1):
        plt.plot(array[j][-1], np.array(array[j][i])/M_0, label = labels_21[j], color = colours_21[j])
    plt.minorticks_on()
    ax.yaxis.set_major_formatter(tick.FormatStrFormatter('%g M$_0$'))
    plt.tick_params(labelsize = fnt)
    plt.legend(fontsize = fnt, loc = 'best', title = r'B$_1$ Values :', title_fontsize = fnt)
    plt.xlabel(r' Time [s]', fontsize = fnt)
    if i == 0:
        plt.ylabel("M$_{x'}$ [Am$^{-1}$]", fontsize = fnt)
    elif i == 1:
        plt.ylabel("M$_{y'}$ [Am$^{-1}$]", fontsize = fnt)
    else:
        plt.ylabel("M$_{z'}$ [Am$^{-1}$]", fontsize = fnt)
    plt.savefig(f'images_NMR_Q2/2_1{i+1}.png')
    plt.close()#Close this image

#Question 2(2) - Solving for long time scales and varying transverse magnetic field

B1 = np.linspace(1e-9,1e-6,1000)

Minf = [[],[],[]]

for i in B1:
    Mx, My, Mz, time = func_NMR.Mag(i,0.1,1,0.1)
    Minf[0].append(Mx[-1])
    Minf[1].append(My[-1])
    Minf[2].append(Mz[-1])

#Plotting each magnetisation component
for i in range(0,len(Minf)):
    fig, ax = plt.subplots(figsize = (10,8))
    ax.set_xscale('log')#Log time axis
    plt.plot(B1*1e6, np.array(Minf[i])/M_0, color = 'black')
    plt.minorticks_on()
    ax.yaxis.set_major_formatter(tick.FormatStrFormatter('%g M$_0$'))
    plt.tick_params(labelsize = fnt)
    plt.xlabel(r' B$_1$ [$\mu$T]', fontsize = fnt)
    if i == 0:
        plt.ylabel("M$_{x'}(\infty)$ [Am$^{-1}$]", fontsize = fnt)
    elif i == 1:
        plt.ylabel("M$_{y'}(\infty)$ [Am$^{-1}$]", fontsize = fnt)
    else:
        plt.ylabel("M$_{z'}(\infty)$ [Am$^{-1}$]", fontsize = fnt)
    plt.savefig(f'images_NMR_Q2/2_2{i+1}.png')
    plt.close()#Close this image
