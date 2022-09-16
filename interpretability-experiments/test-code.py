
# Running experiments from compactem: https://bitbucket.org/aghose/compactem/src/master/

import numpy as np

from sklearn.datasets import load_svmlight_file
from sklearn.model_selection import train_test_split
from joblib import Memory
mem = Memory("./mycache")

import os


def load_data(filename):

    data = load_svmlight_file(filename)
    X, y = data[0].toarray(), np.asarray(data[1], dtype=int)

    X, _, y, _ = train_test_split(X, y, train_size=12000, stratify=y)
    return X, y

    








if __name__ == "__main__":
    
    filename = 'data/circle_data.txt'
    X, y = load_data(filename)

    

    
    # pass
    # tpe_evals = 3000
    # base_dir = r'../data/oracle_based/scikit_dt'
    
    # dataset = 'circle'
    # X, y = comm_utils_data_load.load_data(dataset)
    # X, _, y, _ = train_test_split(X, y, train_size=10000, stratify=y)
    # X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, stratify=y)
