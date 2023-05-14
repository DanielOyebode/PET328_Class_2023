# input statements

co2_comp = float(input('What is the CO2 composition?'))

n2_comp = float(input('What is the N2 composition?'))

h2s_comp = float(input('What is the H2S composition?'))

h2o_comp = float(input('What is the H2O composition?'))

gas_gravity = float(input('What is the measured gas gravity?'))

# the if statement

if co2_comp <= 0.12 and n2_comp <= 0.03 and h2s_comp <= 0:

    print('No correction needed.')

else:
     gas_gravity = (gas_gravity - (1.1767*h2s_comp) - \

                      (1.5196*co2_comp) - (0.9672*n2_comp) - \

                       (0.622*h2o_comp))/(1- h2s_comp - co2_comp - n2_comp - h2o_comp)
    
    print('The corrected gas gravity is', gas_gravity)

# computing pseudo-critical pressure and temperature of the hydrocarbon mixture

p_pch = 756.8 - (131*gas_gravity) - (3.6*gas_gravity**2)

t_pch = 169.2 + (349.5*gas_gravity) - (74.0*gas_gravity**2)

# displaying the results.

print('The hydrocarbon pseudo-critical pressure is {0:.2f} psia'.format(p_pch))

print('The hydrocarbon pseudo-critical temperature is {0:.2f} deg Rankine'.format(t_pch))

