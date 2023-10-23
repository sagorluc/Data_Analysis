import numpy as np
import pandas as pd

def calculate(numbers):
    
    if len(numbers) != 9:
      raise ValueError(f"{numbers} is not a valid number")

    matrix = np.array(numbers).reshape(3, 3)

    object = {

      'mean' : [list(np.mean(matrix, axis=0)), list(np.mean(matrix,     
                axis=1)), np.mean(matrix)],
      'variance' : [list(np.var(matrix, axis=0)), list(np.var(matrix,   
                axis=1)), np.var(matrix)],
      'standard deviation' : [list(np.std(matrix, axis=0)), 
                list(np.std(matrix, axis=1)), np.std(matrix)],
      'max' : [list(np.max(matrix, axis=0)), list(np.max(matrix,     
                axis=1)), np.max(matrix)],
      'min' : [list(np.min(matrix, axis=0)), list(np.min(matrix,     
                axis=1)), np.min(matrix)],
      'sum' : [list(np.sum(matrix, axis=0)), list(np.sum(matrix,     
                axis=1)), np.sum(matrix)],
    }
    
    return object