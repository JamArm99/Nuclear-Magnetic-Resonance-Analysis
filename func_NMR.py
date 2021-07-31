#!/usr/bin/env python

import numpy as np

hbar = 1.05e-34#Dirac's constant
ratio = 2.675e8#Gyromagnetic ratio
perm = 4*np.pi*1e-7#permativity of free space
B = (perm*ratio*hbar)/2#B_0

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
    if r==0:
        raise ValueError('The magnetic field at a radius of zero is infinity, which is unphysical')
    return B*(np.cos(a))/(r**3)*(3*(np.cos(a))**2 + 1)**0.5*1e6

#Function for the y component of the magnetic field
def by(a,r):
    '''
    Equation for the y component of the dipole magnetic field derived from the cosine of the 
    magnetic field magnitude. The 1e6 gives the magnetic field in units of micro-Tesla.
    '''
    if r==0:
        raise ValueError('The magnetic field at a radius of zero is infinity, which is unphysical')
    return B*(np.sin(a))/(r**3)*(3*(np.cos(a))**2 + 1)**0.5*1e6