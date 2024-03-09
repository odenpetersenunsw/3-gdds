#!/usr/bin/env python3
import glob
import numpy as np
import matplotlib.pyplot as plt

#Given a path to a .points file, parse it and display the corresponding nxn matrix, where n is the number of vertices in the design
def plot_type(filepath):
    with open(filepath,'r') as f:
        c = f.read()
    m = list(map(lambda s : s.split(', '),c.split('\n')))[:-2]
    m = [[int(x) for x in a] for a in m]
    m = [[1 if i in a else 0 for i in range(max(map(max,m))+1)] for a in m]
    m = np.array(m)

    plt.imshow(((m@m.T)>0) - np.eye(m.shape[0]))
    plt.title(filepath)
    plt.show()

if __name__ == '__main__':
    for filepath in glob.glob('types/**/*.points'):
        plot_type(filepath)
