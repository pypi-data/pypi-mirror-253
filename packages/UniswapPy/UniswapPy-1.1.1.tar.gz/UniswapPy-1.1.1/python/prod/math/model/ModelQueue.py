# ModelQueue.py
# Author: Ian Moore ( utiliwire@gmail.com )
# Date: Sept 2022

import numpy as np
import queue

class ModelQueue():

    def __init__(self):
        self.__model_queue = queue.Queue()
      
    def size(self):
        return self.__model_queue.qsize()
    
    def apply(self, arr, n_points = None):     
        n_points = len(arr) if n_points == None else n_points  
        for k in range(n_points):
            self.__model_queue.put(arr[k])
            
        return self.__model_queue   