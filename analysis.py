# Programming and Scripting Module Final Project

# Author: Martin Cusack
                                                                    
import numpy as np
import matplotlib as pyplot
import pandas as pd                                                  # use pandas to analyse data because Iris data set is in tabular format

iris = pd.read_csv(r"C:\Users\cusac\OneDrive\Desktop\iris.csv")      # open Fisher's iris data set CSV file using pandas
#print(iris.head())                                                  # view first five rows of data frame using .head() method
#print(iris.info())                                                  # display names of columns and the data types they contain using .info() method
#print(iris.shape)                                                   # display number of rows and columns using .shape attribute
#print(iris.describe())                                              # display some basic information on data set using .describe() method

SepalLengthCm_stats = (iris["SepalLengthCm"].mean(),                             # Generate summary statistics on SepalLength Cm column. Firstly, output the mean length with .mean()
iris["SepalLengthCm"].median(),                                                  # Output the median length using .median()
iris["SepalLengthCm"].min(),                                                     # Output the lowest value using .min()
iris["SepalLengthCm"].max())                                                     # Output the highest value using .max()

print(SepalLengthCm_stats)

SepalWidthCm_stats = (iris["SepalWidthCm"].mean(),                              # Generate summary statistics on SepalWidth Cm column, as above
iris["SepalWidthCm"].median(),                                                  
iris["SepalWidthCm"].min(),                                                     
iris["SepalWidthCm"].max())                                                     

print(SepalWidthCm_stats)


PetalLengthCm_stats = (iris["PetalLengthCm"].mean(),                             # Generate summary statistics on PetalLength Cm column, as above
iris["PetalLengthCm"].median(),                                                   
iris["PetalLengthCm"].min(),                                                      
iris["PetalLengthCm"].max())                                                     

print(PetalLengthCm_stats)

PetalWidthCm_stats = (iris["PetalWidthCm"].mean(),                            # Generate some summary statistics on PetalWidth Cm column, as above
iris["PetalWidthCm"].median(),
iris["PetalWidthCm"].min(),
iris["PetalWidthCm"].max())

print(PetalWidthCm_stats)

with open('summary.txt', 'w') as f:                                              # generate text file and write all summary statistics to it
    f.write('Summary statistics: ' + str(SepalLengthCm_stats) + str (SepalWidthCm_stats) + str (PetalLengthCm_stats) +  str (PetalWidthCm_stats))



