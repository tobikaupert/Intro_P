# Import all neccesary packages to solve assignment 
import numpy as np # for creating arrays and essenatial math tools
from scipy import optimize # for finding optimal consumption and labor 
%matplotlib inline
import matplotlib.pyplot as plt
%load_ext autoreload
%autoreload 2

# set all of the parameters of the labor supply problem 
m = 1
v = 10
e = 0.3
t0 = 0.4 
t1 = 0.1 
k = 0.4

# a. Create utility function that will be optimized to find L* and C*
def u(L, c, v, e):
    ''' calculates utility based upon combinations of labor supply and consumption.
    
    Arguments:
    L(float) = labor supply
    c(float) = consumption
    v(float) = disutility of work
    e(float)= labor supply elasticity
    
    Returns:
    utility 
    '''
    return np.log(c) - v*((L**(1+(1/e)))/(1 + (1/e)))

# b. Create best choice function used in minimization problem
def best_choices(L, w, m, v, e, t0, t1, k):
    ''' Function used to calculate negative utility
    
    Arguments:
    L(float) = labor supply
    w(float) = wage rate
    m(float) = initial cash
    v(float) = disutility of work
    e(float) = labor supply elasticity
    t0(float) = base tax level
    t1(float) = upper tax level 
    k(float) = cutoff
    
    Returns:
    Negative utility function
    '''
    c = m + w*L - (t0*w*L + t1*max(w*L - k, 0))
        
    return -u(L, c, v, e)

# c. minimize negative utility function

def optimization(w, m, v, e, t0, t1, k):
    ''' Function used to calculate optimal labor and consumption at a given wage
    
    Arguments:
    w(float) = wage rate
    m(float) = initial cash
    v(float) = disutility of work
    e(float) = labor supply elasticity
    t0(float) = base tax level
    t1(float) = upper tax level 
    k(float) = cutoff
    
    Returns:
    L = optimal labor supply at a given wage
    c = optimal consumption at a given wage 
    
    '''
    sol = optimize.minimize_scalar(best_choices, method='bounded', bounds=(0,1), args=(w, m, v, e, t0, t1, k))
    
    L = sol.x
    c = m + w*L - (t0*w*L + t1*max(w*L - k, 0))
    return [L, c]

# a. create empty lists for Labor and consumption 
L_best = [] # List of optimal values of labor for given wages
c_best = [] # list of optimal values of consumption given wages
N = 10000 # Number of wages to loop through 

# b. loop through wage levels of 0.5 and 1.5 to find optimal consumption and labor
w = np.linspace(0.5, 1.5, N) # range of wages between 0.5 and 1.5 for optimizer to use

for w_now in w: # wage loop
    optimal_par = optimization(w_now, m, v, e, t0, t1, k)
    L_best.append(optimal_par[0]) #append optimal labor values
    c_best.append(optimal_par[1]) # append optimal consumption values

# c. plotting optimal consumption and labor as functions of wage
plt.style.use('dark_background') # setting personal style 

fig = plt.figure(figsize=(10,4))

# Left plot - Optimal consumption to wage
ax_left = fig.add_subplot(1,2,1)
ax_left.plot(w, c_best)

ax_left.set_title('Optimal Consumption Relative to Wage Rate')
ax_left.set_xlabel('$Wage Rate$')
ax_left.set_ylabel('$Optimal Consumption$')
ax_left.grid(True)

# Right plot - Optimal Labor to wage 
ax_right = fig.add_subplot(1,2,2)
ax_right.plot(w, L_best)

ax_right.set_title('Optimal Labor Supply Relative to Wage Rate')
ax_right.set_xlabel('$Wage Rate$')
ax_right.set_ylabel('$Labor Supply$')
ax_right.grid(True)    

# a. Calculate total tax revenue based upon a given population
def totaltaxrevenue(w, v=10, e=0.3, t0=0.4, t1=0.1, k=0.4):
    ''' Calculates the total tax revenue recieved by a given population size and wage
    
    Arguments:
    w(float) = wage rate
    m(float) = initial cash
    v(float) = disutility of work
    e(float) = labor supply elasticity
    t0(float) = base tax level
    t1(float) = upper tax level 
    k(float) = cutoff
    
    Returns:
    total tax revenue that will be recieved from the population'''
    T= 0
    for w_now in w:
        optimal_val = optimization(w_now, m, v, e, t0, t1, k)
        L = optimal_val[0]
        T += (t0*w_now*L + t1*max(w_now*L - k, 0))
    return T

# b. print total tax revenue collected 
print("Total tax revenue collected" + " " + str(totaltaxrevenue(w))) 

print("Total tax revenue collected" + " " + str(totaltaxrevenue(w, e=0.1)))

# a. Create an objective function to maxamize taxes
def best_tax_levels(tax, w, v, e, m):
    ''' Create function that outputs negative total tax revenue that will be used to find optimal values of T0, T1, and K
    
    Arguments:
    tax(float) = list of various tax paramaters
    w(float) = wage rate 
    
    Results:
    Negative total tax revenue
    '''
    tax_low = tax[0]
    tax_high = tax[1]
    tax_cutoff = tax[2]
    
    return -totaltaxrevenue(w, v, e, tax_low, tax_high, tax_cutoff)

initial_guess = [.1, .1, .1] # Initial guess for optimizing tax revenue
sol = optimize.minimize(best_tax_levels, initial_guess, method='Nelder-Mead', args=(w, e, v, m))

tax1 = sol.x[0] # Optimal standard labor income tax
tax2 = sol.x[1] # Optimal top bracket labor income tax
tax3 = sol.x[2] # optimal cutoff
   
print("Standard labor income tax " + str(tax1))
print("Top bracket labor income tax " + str(tax2))
print("Cutoff " + str(tax3))
