#!/usr/bin/env python

import numpy as np

hbar = 1.05e-34#Dirac's constant
ratio = 2.675e8#Gyromagnetic ratio
perm = 4*np.pi*1e-7#permativity of free space
B = (perm*ratio*hbar)/2#B_0

M_0 = 1.4e-6#Initial magnetisation

#Defining function for the radius as a function of angle and magnetic field size
def radius(Bmag,theta):
    '''
    Equation for the radial dependence of angle with a constant magnetic field from a 
    dipole. The magnitude 'Bmag' is derieved from the magnetic dipole vector. The 1e9
    factor is to obtain the radial distance in nm.
    '''
    if Bmag ==0:#Prevent unphysical magnetic field
        raise ValueError('The magnitude of the mangetic field can only be zero at infinite range')
    return ((perm*ratio*hbar)/(8*np.pi*Bmag)*(3*np.cos(theta)**2 + 1)**0.5)**(1/3)*1e9

#Function for the x component of the magnetic field
def bx(a,r):
    '''
    Equation for the x component of the dipole magnetic field derived from the cosine of the 
    magnetic field magnitude. The 1e6 gives the magnetic field in units of micro-Tesla.
    '''
    if np.any(r == 0):
        raise ValueError('The magnetic field at a radius of zero is infinity, which is unphysical')
    return B*(np.cos(a))/(r**3)*(3*(np.cos(a))**2 + 1)**0.5*1e6

#Function for the y component of the magnetic field
def by(a,r):
    '''
    Equation for the y component of the dipole magnetic field derived from the cosine of the 
    magnetic field magnitude. The 1e6 gives the magnetic field in units of micro-Tesla.
    '''
    if np.any(r == 0):
        raise ValueError('The magnetic field at a radius of zero is infinity, which is unphysical')
    return B*(np.sin(a))/(r**3)*(3*(np.cos(a))**2 + 1)**0.5*1e6

#Bloch equation function
def Mag(B1,T_0,T,step):#Transverse magnetic field, initial time, final time, iteration
    '''
    Function to numerically solve the Bloch equations in the rotating frame of reference for carbon-13 atoms in a static magnetic field of
    10 Tesla aligned along the z-axis. The equilibrium magnetisation is given by the temperature of the system and is defined outside the
    function. Initial parameters are defined inside the function and are given by the context of the problem. Bloch's equations are first
    order differential equations with time; hence, they are solved by iterating with a time step using a while loop. The function returns the
    time list and magnetisation components list.
    '''
    if B1 == 0 or T == 0 or step == 0:
        raise ValueError('Function arguments are unphysical')
    else:
        pass#If B1 is not zero then allow function to proceed
    
    #Initial params
    T1 = 100e-3 #Longitudinal relaxation time
    T2 = 10e-3 #Transverse relaxation time
    B0 = 10 #Z-axis static field
    gamma = 6.72e7 #Gyromagnetic ratio of C-13
    
    #initial parameters
    Mzi = 0
    Mxi = 0
    Myi= M_0
    time = [] #Time list to append too
    timei = T_0 #Initialise time param for while loop
    
    Bx = B1 #Rotating frame of refernece 
    By = 0
    Bz = 0
    
    #Magnetisation lists to append too
    Mx = []
    My = []
    Mz = []
    
    #While loop to solve first order differential equation with time
    while timei <= T :#iterate through to specific time
        
        timei += step#Increase time by st
        
        #Bloch equations
        gradMzi = (M_0-Mzi)/T1 + gamma*(Mxi*By - Myi*Bx)
        gradMxi = - (Mxi)/T2 + gamma*(Myi*Bz - Mzi*By)
        gradMyi = - (Myi)/T2 + gamma*(Mzi*Bx - Mxi*Bz)

        Mxi += gradMxi*step
        Mzi += gradMzi*step
        Myi += gradMyi*step
        
        #Append magnetisation components
        Mx.append(Mxi)
        My.append(Myi)
        Mz.append(Mzi)

        time.append(timei)#Apend the time iteration
        
    return Mx, My, Mz, time #Return magnetisation and time lists