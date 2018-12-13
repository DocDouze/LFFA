################################################################################
#
# 
#
# Description - implements the Kalman filter
#
# Example uses a 400Hz sampling rate with noise applied to both measurement
# and acceleration.
#
################################################################################
from pylab import *
import random

# Sampling rate: 400Hz
sampling_rate = 1.0/400.0

# Simulation duration (seconds)
simulation_duration = 120
number_of_samples = int(simulation_duration / sampling_rate)

# Noise parameters

sigma_a_k = 2.0
sigma_z = 0.2

# Noise Estimation

sigma_z_e = 0.2




F = array([[1.0, sampling_rate],[0.0, 1.0] ])           #l33
G = array([[sampling_rate**2.0/2.0],[sampling_rate]])   #l34
Q_k = dot(G,G.T)*sigma_a_k**2.0                         #l35
H_k = array([1.0, 0.0])                                 #l36


# Observation noise covariance
R_k = sigma_z_e**2					#l37

# Initial Conditions
x_k = array([[0.0],[0.0]])
x_km1 = array([[0.0],[0.0]])
xh_k_km1 = array([[0.0],[0.0]])
xh_km1_km1 = array([[0.0],[0.0]])
P_km1_km1 = array([[0.0, 0.0],[0.0, 0.0]])
# End of Initial Conditions

# Reserve log vectors for plotting later
x_log = zeros((2,number_of_samples))
z_log = zeros((2,number_of_samples))
yh_log = zeros((2,number_of_samples))
xh_log = zeros((2,number_of_samples))
k_log = zeros((2,number_of_samples))
P_log = zeros((2,number_of_samples))
# End of Initial Conditions

# Sampling Loop
for t in range(1,number_of_samples):

	# Simulation of the process
	a_k = random.normalvariate(0.1*sin(2*pi*t*sampling_rate), sigma_a_k) # Random acceleration  		#l63
	x_k = dot(F,x_km1) + dot(G,a_k) # The real state 							#l64
	# End of Simulation of the process
		
	xh_k_km1 = dot(F,xh_km1_km1)										#l65
	P_k_km1 = dot(dot(F,P_km1_km1), F.T) + Q_k 								#l66
	#z_k = dot(H_k, x_k) + random.normalvariate(0.0, sigma_z)						#l66

	z_k = dot(H_k, x_k) + random.normalvariate(0.0, sigma_z+t/(10000.0))
	
	if t>5000 and t<10000 :   # What happends if ...
		z_k=0


	yh_k= z_k - dot(H_k,xh_k_km1)										#l77
	S_k = dot(dot(H_k,P_k_km1),H_k.reshape(2,1)) + R_k							#l78
	K_k = dot(P_k_km1, H_k.reshape(2,1))*S_k								#l79
	xh_k_k = xh_k_km1 + K_k*yh_k										#l80
	P_k_k = (1 - dot(H_k, K_k))*P_k_km1 									#l81

	x_km1 = x_k		
	xh_km1_km1 = xh_k_k
	P_km1_km1 = P_k_k

	# Data logging
	x_log[0,t] = x_k[0,0]
	x_log[1,t] = x_k[1,0]
	z_log[0,t] = z_k
	xh_log[0,t] = xh_k_k[0,0]
	k_log[0,t] = K_k[1]
	yh_log[0,t] = yh_k
	P_log[0,t] = P_k_k[0,0]
	P_log[1,t] = P_k_k[1,1]
	# End of Data logging

	# Some print during Simulation
	if t%1000 == 0:
		print("t:"+str(t))
		print("z_k:"+str(z_k))
		print("K_k:"+str(K_k))
		print("R_k:"+str(K_k))
	# End of Some print during Simulation

# End of Sampling Loop

# Some plot at the end of the simulation
# Figure 1
plot(x_log[0,:])
plot(z_log[0,:])
plot(xh_log[0,:])
xlabel('Sample')
ylabel('Position (meters)')
title('Position : Actual State')
grid(True)

# Figure 2
figure()
xlabel('Sample')
ylabel('Velocity (meters/second)')
title('Velocity : Actual State')
grid(True)
plot(x_log[1,:])

# Figure 2
figure()
xlabel('Sample')
title('Kalman Position Gain over Time')
grid(True)
plot(k_log[0,:])

# Figure 3
figure()
xlabel('Sample')
title('Residual over Time')
grid(True)
plot(yh_log[0,:])

# Figure 4
figure()
xlabel('Sample')
title('Covariances')
grid(True)
plot(P_log[0,:])
plot(P_log[1,:])

show()
# End of Some plot at the end of the simulation
