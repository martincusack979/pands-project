# Programming and Scripting Module Final Project

# Author: Martin Cusack

# with open(r"C:\Users\cusac\OneDrive\Desktop\iris.csv" , 'r') as f:   # open Fisher's iris data set CSV file 
    # iris = f.read()                             
   #  f.close ()
                                                                    
import numpy as np
import matplotlib as pyplot
import pandas as pd                                                 # use pandas to analyse data because it's in tabular form

iris = pd.read_csv(r"C:\Users\cusac\OneDrive\Desktop\iris.csv") # open Fisher's iris data set CSV file using pandas
# print(iris.head())                                              # view first five rows of data frame using .head() method

SepalLengthCm_stats = (iris["SepalLengthCm"].mean(),                             # Generate summary statistics on SepalLength Cm column. Firstly, output the mean length with .mean()
iris["SepalLengthCm"].median(),                                                  # Output the median length using .median()
iris["SepalLengthCm"].min(),                                                     # Output the lowest value using .min()
iris["SepalLengthCm"].max())                                                     # Output the highest value using .max()

print(SepalLengthCm_stats)