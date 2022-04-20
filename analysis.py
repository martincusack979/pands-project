# Programming and Scripting Module Final Project

# Author: Martin Cusack
                                                                    
import numpy as np
import matplotlib as pyplot
import pandas as pd                                                 # use pandas to analyse data because Iris data set is in tabular format

iris = pd.read_csv(r"C:\Users\cusac\OneDrive\Desktop\iris.csv") # open Fisher's iris data set CSV file using pandas
#print(iris.head())                                              # view first five rows of data frame using .head() method
#print(iris.info())                                              # display names of columns and the data types they contain using .info() method
#print(iris.shape)                                               # display number of rows and columns using .shape attribute
#print(iris.describe())                                          # display some basic information on data set using .describe() method

print(iris["SepalLengthCm"].mean())                             # Generate some summary statistics on SepalLength Cm column. Firstly, output the mean length with .mean()
print(iris["SepalLengthCm"].median())                           # Secondly, output the median length using .median()
print(iris["SepalLengthCm"].min())                              # Output the lowest value using .min()
print(iris["SepalLengthCm"].max())                              # Output the highest vaklue using .max()

print(iris["SepalWidthCm"].mean())                              # Generate some summary statistics on SepalWidth Cm column, as above
print(iris["SepalWidthCm"].median()) 
print(iris["SepalWidthCm"].min()) 
print(iris["SepalWidthCm"].max()) 

print(iris["PetalLengthCm"].mean())                              # Generate some summary statistics on PetalLength Cm column, as above
print(iris["PetalLengthCm"].median()) 
print(iris["PetalLengthCm"].min()) 
print(iris["PetalLengthCm"].max()) 

print(iris["PetalWidthCm"].mean())                              # Generate some summary statistics on PetalWidth Cm column, as above
print(iris["PetalWidthCm"].median()) 
print(iris["PetalWidthCm"].min()) 
print(iris["PetalWidthCm"].max()) 