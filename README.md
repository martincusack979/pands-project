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

Firstly, I used the head.() method to display the first five rows of the data frame in order to get a quick impression of the data set content. 
I then  displayed the names of columns and the data types they contain using the.info() method, and used the .shape attribute to display the numbers 
of rows and columns in the data frame in a tuple. This told me that there were 150 rows and 6 columns in the data set.

Pandas Data Frames consist of three elements: the index (in this case, the row numbers), the columns (in this case, ID, SepalLengthCm, SepalWidthCm, 
PetalLengthCm, PetalWidthCm and Species ) and a two-dimensional NumPy array of values (in this case, the different measurements which comprise the 
bulk of the information in the data set).

#### Outputting a summary of each variable 

The next task was to output a summary of each variable to a text file.  Pandas includes some very useful summary statistics tools which deliver an 
overview of the information contained in data frames.  I was required to summarise the following variables: SepalLengthCm, SepalWidthCm, PetalLengthCm
and PetalWidthCm. 

Firstly, I took the Sepal LengthCm column and performed some sample summary statistics on it.  These were:

•	.mean( ) - outputs the total of the numbers divided by how many numbers there are.
•	.median( ) - outputs the middle number of a list of numbers.
•	.min( ) - outputs the lowest number in a list of numbers
•	.max ( ) - outputs the highest number in a list of numbers

I then repeated these for the three other categories (SepalWidthCm, PetalLengthCm and PetalWidthCm.)
Next, I took the first set of summary statistics for SepalWidthCm and outputted it to a generated text file (named summary.txt) using the function 
***"with open('summary.txt', 'w') as f: ".*** To append the summary stats for the other variables to the text file I used 'a' for append, as in "with 
open('summary.txt', 'a') as f: ". To add a new line to the text file I used the '\n' character as in ***"f.write('\n')"***

#### Creating a histogram for each variable

I used Matplotlib to create histograms of each variable using ***iris.hist(column = "column_name")***, setting the column argument to the relevant column name. 
I saved each histogram as a png file using plt.savefig, as demonstrated in the module lectures.

#### Creating scatter plots for each pair of variables

Again, I used Matplotlib to create scatter plots of each pair of variables.  The first pair to work on was SepalLengthCm and SepalWidthCm, with the former on 
the x axis and the latter on the y axis.  Secondly, I created a scatter plot of PetalLengthCm and PetalWidthCm, again with the former on the x axis and the
latter on the y axis.

For information on how to perform this, I checked the information at: https://pandas.pydata.org/

#### Creating box plots and violin plots

Using a box plot, I could provide a better visual representation of the distribution of sepal and petal length across all three species of iris.  To do this, 
I firstly imported the seaborn package using "import seaborn as sns".  I then created the box plot using ***"box = sns.boxplot(x="Species", y="SepalLengthCm", 
data=iris)":***  specifying the iris data frame info was required with the "data" argument and placing "Species" on the x axis and "Sepal LengthCm" on the y axis. 
I then repeated these steps for the Petal LengthCm data.

The results are informative as they clearly demonstrate that Iris Setosa has both the shortest sepal length and petal length, while Iris Virginica has both the 
longest sepal length and petal length.  The box plot provides a greater depth of information than a scatter plot as the size of each box illustrates the 
distribution of lengths within each species.

Violin plots can also provide interesting insights, as the length and width of each "violin" allows the viewer to make a comparison of distributions between the 
different species categories in the Iris data set.  I created the violin plots using sns.violinplot(x="Species", y="PetalLengthCm", data=iris)

Again, the results are interesting, since for example in the Petal Length violin plot we see a greater density of data points for Iris Setosa compared to the 
other two species, indicating that the distribution of lengths in Iris Setosa is much shorter.

I checked the Kaggle website for information on how to create box and violin plots using the Seaborn package:
https://www.kaggle.com/code/benhamner/python-data-visualizations

#### References: 

1.	Fisher, R. A. (1936) "The use of multiple measurements in taxonomic problems. The Annals of Eugenics" (1935-1954). 

2.	For info on iris data set: https://www.kaggle.com/datasets/uciml/iris?resource=download

3.	For info on linear discriminant analysis: https://towardsdatascience.com/linear-discriminant-analysis-explained-f88be6c1e00b

4.	For info on Matplotlib:  https://www.w3schools.com/python/matplotlib_intro.asp

5.	For info on summary statistics: https://campus.datacamp.com/courses/data-manipulation-with-pandas/aggregating-dataframes?ex=1

6.	For info on data manipulation with Pandas: https://campus.datacamp.com/courses/data-manipulation-with-pandas/transforming-dataframes?ex=1

7.	For info on how to write to a text file in VS studio:  https://www.pythontutorial.net/python-basics/python-write-text-file/

8.	For info on how to write to a text file: https://stackoverflow.com/questions/43801152/read-output-of-a-csv-file-and-write-it-to-a-text-file-using-python

9.	For info on how to create box plots and violin plots: https://www.kaggle.com/code/benhamner/python-data-visualizations

10.	For info on how to create scatter plots:  https://pandas.pydata.org

11.	For general information:  McKinney, Wes. "Python for Data Analysis".  2nd Edition. O'Reilly. 2018
