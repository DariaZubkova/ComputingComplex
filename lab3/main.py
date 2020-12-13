from numpy import loadtxt
from tolsolvty import tolsolvty
import numpy as np


def main():
    #path_folder = '../example'

    #infA = loadtxt(path_folder + '/infA.txt')
    #supA = loadtxt(path_folder + '/supA.txt')

    #infb = loadtxt(path_folder + '/infb.txt', ndmin=2)
    #supb = loadtxt(path_folder + '/supb.txt', ndmin=2)


    #infA = np.array([[1, 5], [6, 8], [1, 5]])
    #supA = np.array([[2, 6], [7, 9], [3, 7]])
    #infb = np.array([[0.1], [1.3], [0.3]])
    #supb = np.array([[2.1], [3.3], [2.3]])

    infA = np.array([[1, 6, 1], [5, 8, 5]])
    supA = np.array([[2, 7, 3], [6, 9, 7]])
    infb = np.array([[1.6], [2.5]])
    supb = np.array([[3.6], [4.5]])

    [tolmax, argmax, envs, ccode] = tolsolvty(infA, supA, infb, supb)
    print('tolmax = ', tolmax)
    print('argmax = ', argmax)
    print('envs = ', envs)
    print('ccode = ', ccode)


if __name__ == "__main__":
    main()
