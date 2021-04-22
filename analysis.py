# pands-project2021 
# Author: Betty Attwood G00398300 
# Final Project for Programming & Scripting Module as a part of
# GMIT's Higher Diploma in Computer Science Data Analytics

# This program analyses and creates plots of Fisher's Iris Data Set 

# Uploading the libraries needed for this project:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as sk 

#  Uploading UCI's Iris dataset and adding column names to it 
#irisData = pd.read_csv('iris.data', names =["sepal length in cm", "sepal width in cm", "petal length in cm", "petal width in cm", "Species"])  # reading in the data file 
#df = pd.DataFrame(irisData)

csv = ('iris.data')
names = ["sepal length in cm", "sepal width in cm", "petal length in cm", "petal width in cm", "Species"]
irisData = pd.read_csv(csv, names=names)


# code for creating and writing a txt file of the summary information about this data set

with open("iris_summary.txt", "w") as f:
    f.write("This file contains basic data regarding the file type and contents of Fisher's Iris Data Set.\n\n\n")
    # Basic investigation into the dataset:
    f.write("Object Type for iris Data:\n\n" + str(type(irisData)) + "\n\n\n")
    f.write("This shows the basic info of the data set.\nIt includes a sampling of the head and tail of the data, the index and the number of rows and columns.\n\n" + str(irisData.info) + "\n\n\n")
    # look at the <bound dataframe.info issue later -- https://stackoverflow.com/questions/46239946/attempt-to-access-dataframe-column-displays-bound-method-ndframe-xxx
    # https://www.reddit.com/r/learnprogramming/comments/3yx9er/python_what_does_it_mean_to_call_something/
    irisShape = irisData.shape # this gives me the shape of the matrix or data table - 150 rows, five columns
    f.write("Data Table Shape; The number of rows and number of columns:\n\n " + str(irisShape) + "\n\n\n")
    f.write("The Index of the columns are provided below along with the datatype:\n\n" + str(irisData.columns) + "\n\n\n") # this prints the Index showing titles of the columns)
    descriptives = irisData.describe()
    f.write("Table Summary of the Statistics of the Data Set Variables:\n\n" + descriptives.to_string() + "\n\n\n")
    f.write("The Iris data set is a balaced data set.\nBreakdown of the data by species:\n\n" + str(irisData["Species"].value_counts()) 
    + "\n\n\n")

    f.write("Digging Deeper into the Data - Examining by Species\n\n\n\n")
    # Max, Min & Median values of each attribute by class
    f.write("Maximum values for each attribute by Species: \n\n" + str(irisData.groupby('Species').max()) +"\n\n")
    f.write("Minimum values for each attribute by Species: \n\n" + str(irisData.groupby('Species').min()) +"\n\n")
    f.write("Median values for each attribute by Species: \n\n" + str(irisData.groupby('Species').median()) +"\n\n")
    f.write("Pivot Table Showing Each Species Mean Measurements: \n\n" + str(irisData.pivot_table(index='Species', values=["sepal length in cm", "sepal width in cm", "petal length in cm", "petal width in cm"], aggfunc=np.mean)) + "\n\n")
    f.write("Pivot Table Showing Each Species Median Measurements: \n\n" + str(irisData.pivot_table(index='Species', values=["sepal length in cm", "sepal width in cm", "petal length in cm", "petal width in cm"], aggfunc=np.median)) + "\n\n")
    f.write("Pivot Table Showing Each Species Max Measurements: \n\n" + str(irisData.pivot_table(index='Species', values=["sepal length in cm", "sepal width in cm", "petal length in cm", "petal width in cm"], aggfunc=np.max)) + "\n\n")
    f.write("Pivot Table Showing Each Species Min Measurements: \n\n" + str(irisData.pivot_table(index='Species', values=["sepal length in cm", "sepal width in cm", "petal length in cm", "petal width in cm"], aggfunc=np.min)) + "\n\n")
    # https://www.w3resource.com/python-exercises/pandas/excel/pandas-pivot-exercise-13.php  max and min for pivot tables
    
# Plots

# Histograms of the variables

#sepal length

sns.displot(irisData, x = "sepal length in cm", hue="Species", kde=True, multiple="dodge") # hue color codes by that variable
# dodge makes the different species easier to see # kde adds a kernal density estimator line to the plot
plt.grid()
# Saves the plot as a png image
plt.savefig('Histogram_All_SepalLength.png')
plt.clf() # Clears the plot so a new plot can be created. Without this, the subsequent plots are combined into the previous plot

sns.displot(data=irisData, x="sepal length in cm", hue="Species", col="Species", kde=True)  
plt.grid()
plt.savefig('Histogram_Individual_SepalLength.png')
plt.clf() 

# sepal width
sns.displot(irisData, x = "sepal width in cm", hue="Species", kde=True, multiple="dodge") # hue color codes by that variable
# dodge makes the different species easier to see # kde adds a kernal density estimator line to the plot
plt.grid()
# Saves the plot as a png image
plt.savefig('Histogram_All_SepalWidth.png')
plt.clf() # Clears the plot so further plots can be created.

sns.displot(data=irisData, x="sepal width in cm", hue="Species", col="Species", kde=True)  
plt.grid()
plt.savefig('Histogram_Individual_SepalWidth.png')
plt.clf() 

# petal length
sns.displot(irisData, x = "petal length in cm", hue="Species", kde=True, multiple="dodge") # hue color codes by that variable
# dodge makes the different species easier to see # kde adds a kernal density estimator line to the plot
plt.grid()
# Saves the plot as a png image
plt.savefig('Histogram_All_PetalLength.png')
plt.clf() # Clears the plot so further plots can be created.

sns.displot(data=irisData, x="petal length in cm", hue="Species", col="Species", kde=True)  
plt.grid()
plt.savefig('Histogram_Individual_PetalLength.png')
plt.clf() 

# petal width
sns.displot(irisData, x = "petal width in cm", hue="Species", kde=True, multiple="dodge") # hue color codes by that variable
# dodge makes the different species easier to see # kde adds a kernal density estimator line to the plot
plt.grid()
# Saves the plot as a png image
plt.savefig('Histogram_All_PetalWidth.png')
plt.clf() # Clears the plot so further plots can be created. 

sns.displot(data=irisData, x="petal width in cm", hue="Species", col="Species", kde=True)  
plt.grid()
plt.savefig('Histogram_Individual_PetalWidth.png')
plt.clf() 

