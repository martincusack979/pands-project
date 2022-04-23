## Programming and Scripting : Final Project

#### Contents

1.	Introduction
2.	Importing the CSV file
3.	Outputting a summary of each variable
4.	Creating a histogram of each variable
5.	Creating scatter plots of each pair of variables
6.	Creating box plots and violin plots
7.	References

#### Introduction

The Iris flower data set first appeared in biologist Ronald Fisher's 1936 paper "The Use of Multiple Measurements in Taxonomic Problems".  
Fisher's work has been highly influential in the fields of data science and machine learning over the decades since its publication and
has been referenced on innumerable occasions by teachers and academics.

Fisher's data set comprises a study of three different species of the Iris flower (Iris setosa, Iris virginica and Iris versicolor) and  
contains six columns: ID, SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm and Species.  It is an example of linear discriminant 
analysis, which is a method of data analysis which is used "as a tool for classification, dimension reduction, and data visualization."

Reference: https://towardsdatascience.com/linear-discriminant-analysis-explained-f88be6c1e00b

Due to its tabular structure, the Iris data set lends itself easily to many different analytical approaches.  It also allows for exploration 
via a range of visualisations including histograms, scatter plots, box plots and many others.

#### Importing the CSV file

Firstly, I imported the various packages required for completion of the project : Numpy, Matplotlib and Pandas. The CSV table containing the data 
is in tabular format, so it made sense to convert the CSV file into a data frame in Pandas. Once the data frame was created, I could then perform 
interesting calculations and visualisations on the available information.

I downloaded the Iris data set from the Kaggle website at https://www.kaggle.com/datasets/uciml/iris?resource=download and imported the CSV file 
into the Virtual Studio Code environment using: ***"iris = pd.read_csv(r"C:\Users\cusac\OneDrive\Desktop\iris.csv)"***










