import numpy as np

def trapezoidal(function, num_points, array, equal):

    f = lambda x: eval(function, {"np": np, "x": x})
    
    if equal == True:
        
        h = (array[1] - array[0])/(num_points-1)
        
        equal_sum = 0
        
        for i in range(1, num_points-1):
            
            equal_sum += f(array[0] + i*h)
            
        return h*(f(array[0]) + 2*equal_sum + f(array[1]))/2
    
    elif equal == False:
        
        sum = 0
    
        for j in range(1, len(array)):
        
            sum += (array[j] - array[j-1]) * (f(array[j-1]) + f(array[j])) / 2
        
        return sum