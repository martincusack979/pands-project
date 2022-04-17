# Programming and Scripting Module Final Project

# Author: Martin Cusack

# with open(r"C:\Users\cusac\OneDrive\Desktop\iris.csv" , 'r') as f:   # open Fisher's iris data set CSV file 
    # iris = f.read()                             
   #  f.close ()
                                                                    
import numpy as np
import matplotlib as pyplot
import pandas as pd

iris = pd.read_csv(r"C:\Users\cusac\OneDrive\Desktop\iris.csv") # open Fisher's iris data set CSV file using pandas
print(iris)