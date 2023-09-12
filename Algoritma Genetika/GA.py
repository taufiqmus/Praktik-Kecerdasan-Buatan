import numpy as np
from geneticalgorithm import geneticalgorithm as ga
import math

def f(X):
    global luas, keliling, penalti
    keliling = (X[0] + (2*X[1]) + (math.sqrt(X[0]**2 + X[1]**2)) + (2*X[2]))
    if  keliling > 100:
      penalti = 99999
    else:
      penalti = 0

    luas = ((0.5*X[1]*X[0])+(X[1]*X[2]))
    return -(luas - penalti)

varbound=np.array([[1,100],[1,100],[1,100]])

algorithm_param = {'max_num_iteration': 1000, 'population_size': 100, 'mutation_probability': 0.1, 'elit_ratio': 0.01,
                   'crossover_probability': 0.5, 'parents_portion': 0.3, 'crossover_type': 'uniform', 'max_iteration_without_improv': None}

model=ga(function=f,\
            dimension=3,\
            variable_type='real',\
            variable_boundaries=varbound,\
            algorithm_parameters=algorithm_param)

model.run()
