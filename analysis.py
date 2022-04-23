# Programming and Scripting Module Final Project

# Author: Martin Cusack
                                                                    
from re import L
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd                                                  # use pandas to analyse data because Iris data set is in tabular format

iris = pd.read_csv(r"C:\Users\cusac\OneDrive\Desktop\iris.csv")      # open Fisher's iris data set CSV file using pandas
print(iris.head())                                                  # view first five rows of data frame using .head() method
print(iris.info())                                                  # display names of columns and the data types they contain using .info() method
print(iris.shape)                                                   # display number of rows and columns using .shape attribute
print(iris.describe())                                              # display some basic information on data set using .describe() method

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

PetalWidthCm_stats = (iris["PetalWidthCm"].mean(),                                # Generate some summary statistics on PetalWidth Cm column, as above
iris["PetalWidthCm"].median(),
iris["PetalWidthCm"].min(),
iris["PetalWidthCm"].max())

print(PetalWidthCm_stats)

with open('summary.txt', 'w') as f:                                               # generate text file and write summary statistics for Sepal Length 
    f.write('Sepal Length Cm: Mean, Median, Min and Max = ' + str(SepalLengthCm_stats))
    f.write('\n')                                                                 # use '\n' to create new line in text file

with open('summary.txt', 'a') as f:                                               # append summary stats for Sepal Width Cm using the argument 'a' 
    f.write('Sepal Width Cm: Mean, Median, Min and Max = ' + str(SepalWidthCm_stats))
    f.write('\n')

with open('summary.txt', 'a') as f:                                               # append stats for Petal Length Cm
    f.write('Petal Length Cm: Mean, Median, Min and Max = ' + str(PetalLengthCm_stats))   
    f.write('\n')

with open('summary.txt', 'a') as f:                                               # append stats for Petal Width Cm
    f.write('Petal Width Cm: Mean, Median, Min and Max = ' + str(PetalLengthCm_stats))  
    f.write('\n')
    
 
iris.hist(column = "SepalLengthCm")                                             # use matplotlib to output histograms for each column
plt.savefig('sepallength.png') 

iris.hist(column = "SepalWidthCm")
plt.savefig('sepalwidth.png') 

iris.hist(column = "PetalLengthCm")
plt.savefig('petallength.png') 

iris.hist(column = "PetalWidthCm")
plt.savefig('petalwidth.png') 

# use matplotlib to create scatter plots of each pair of variables