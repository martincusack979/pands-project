# Programming and Scripting Module Final Project

# Author: Martin Cusack

# with open(r"C:\Users\cusac\OneDrive\Desktop\iris.csv" , 'r') as f:   # open Fisher's iris data set CSV file 
    # iris = f.read()                             
   #  f.close ()
                                                                    
import numpy as np
import matplotlib as pyplot
import pandas as pd                                                 # use pandas to analyse data because it's in tabular form

iris = pd.read_csv(r"C:\Users\cusac\OneDrive\Desktop\iris.csv") # open Fisher's iris data set CSV file using pandas
print(iris.head())                                              # view first five rows of data frame using .head() method
print(iris.info())                                              # display names of columns and the data types they contain using .info() method
print(iris.shape)                                               # display number of rows and columns using .shape
print(iris.describe())                                          # display soem basic information on data set
