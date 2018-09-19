import numpy as np
import matplotlib.pyplot as pyplot

data_file = np.loadtxt('data_file.txt', delimiter=',')

time = data_file[:,0]
