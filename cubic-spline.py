## In Octave - This would require an Octave kernel
## Read here on how to install a Octave kernel on your jupyter noteboook: https://pypi.org/project/octave-kernel/

function cubic_spline (X,Y)
    coefficients = splinefit(X,Y,numel (X)-1).coefs
endfunction


## In Python - This demonstrates more complex linear algebra compared to Octave that simply gives us the output coefficients.
## Octave is a more efficient but less comprehensive language for solving mathematical systems.

from numpy.linalg import inv
import numpy as np

def cubic_spline(x,y):
    n = len(x)
    h = x[1] - x[0]
    
    x = np.array(x).reshape(-1,1)
    y = np.array(y).reshape(-1,1)
    
    
    k_matrix = [[0 for __ in range(n)] for _ in range(n)]
    y_matrix = [[0 for __ in range(n)] for _ in range(n)]
    
    k_matrix[0][0] = 4
    k_matrix[0][1] = 1  
    k_matrix[n-1][n-2] = 1
    k_matrix[n-1][n-1] = 4
        
    y_matrix[0][0] = -2
    y_matrix[0][1] = 1
    y_matrix[n-1][n-1] = 1
    y_matrix[n-1][n-1] = -2
        
    
    for i in range(1,n-1):
        k_matrix[i][i-1] = 1
        k_matrix[i][i] = 4
        k_matrix[i][i+1] = 1
        
        y_matrix[i][i-1] = 1
        y_matrix[i][i] = -2
        y_matrix[i][i+1] = 1
    
    final_k = (6/h**2)*np.matmul(np.matmul(inv(k_matrix), y_matrix),y)
    
    return final_k
