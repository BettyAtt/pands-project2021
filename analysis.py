# pands-project2021 
# Author: Betty Attwood G00398300 
# Final Project for Programming & Scripting Module as a part of
# GMIT's Higher Diploma in Computer Science Data Analytics

# This program analyses and creates plots of Fisher's Iris Data Set 

# Uploading the libraries needed for this project:
import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sbn
import sklearn as sk 

#  Uploading UCI's Iris dataset and adding column names to it 
#irisData = pd.read_csv('iris.data', names =["sepal length in cm", "sepal width in cm", "petal length in cm", "petal width in cm", "Species"])  # reading in the data file 
#df = pd.DataFrame(irisData)

csv = ('iris.data')
names = ["sepal length in cm", "sepal width in cm", "petal length in cm", "petal width in cm", "Species"]
irisData = pd.read_csv(csv, names=names)


# code for creating and writing a txt file of the summary information about this data set

with open("iris_summary.txt", "w") as f:
    # Basic investigation into the dataset:


    #f.write(df.columns = ['SepalLength_cm','SepalWidth_cm','PetalLength_cm','PetalWidth_cm','Species']) # adding column names to files
    irisShape = irisData.shape # this gives me the shape of the matrix or data table - 150 rows, five columns
    f.write("The shape of the data table is provided in the format (number of rows, number of columns): \n\n " + str(irisShape) + "\n\n")
    f.write("The Index of the columns are provided below along with the datatype: \n\n" + str(irisData.columns) + "\n\n") # this prints the Index with the titles of the columns:
# Index(['SepalLength_cm', 'SepalWidth_cm', 'PetalLength_cm', 'PetalWidth_cm', 'Class'], dtype='object')
    descriptives = irisData.describe()
    f.write("Summary Statistics of each variables in a table: \n\n" + descriptives.to_string() + "\n\n") 
    f.write("Breakdown of the data by species: \n\n" + str(irisData["Species"].value_counts()) + "\n\n")
    #f.write(df.describe()) # is the describe function meaningful on whole set or by loc only? # this gives the basic information about the dataframe inclding the range index, 
# number of data columns, column numbers and how many non-null objects, as well as the dtype for each column content.
# finally it give the memory usage and null values.
    #irisInfo = df.info()
    f.write("Pivot Table Showing Each Species Mean Measurements: \n\n" + str(irisData.pivot_table(index='Species', values=["sepal length in cm", "sepal width in cm", "petal length in cm", "petal width in cm"], aggfunc=np.mean)) + "\n\n")
    f.write("Pivot Table Showing Each Species Median Measurements: \n\n" + str(irisData.pivot_table(index='Species', values=["sepal length in cm", "sepal width in cm", "petal length in cm", "petal width in cm"], aggfunc=np.median)) + "\n\n")
    #f.write("Description of table data for species Iris setosa" + str(irisData.loc[irisData["Species"] == "Iris-setosa"])  + "\n\n")
    
    
    maxsepallength = irisData["sepal length in cm"].max()
    #maxsepalwidth = irisData['sepal_width'].max()
    #maxpetallength = irisData['petal_length'].max()
    #maxpetalwidth = irisData['petal_width'].max()
    #minsepallength = irisData['sepal_length'].min()
    #minsepalwidth = irisData['sepal_width'].min()
    #minpetallength = irisData['petal_length'].min()
    #minpetalwidth = irisData['petal_width'].min()
    f.write("The maximum sepal length in cm for this data set is: " + str(maxsepallength) + "\n\n")

    # More specific analysis
    # Min, Max & Median values of each attribute by class
    f.write("Maximum values for each attribute by Class: \n\n" + str(irisData.groupby('Species').max()) +"\n\n")
    f.write("Minimum values for each attribute by Class: \n\n" + str(irisData.groupby('Species').min()) +"\n\n")
    f.write("Median values for each attribute by Class: \n\n" + str(irisData.groupby('Species').median()) +"\n\n")
   
    modevalues = irisData.mode(axis=0,numeric_only=True,dropna=True)
    f.write("Mode of each attribute: \n\n" + str(modevalues) + "\n\n")  # how can I do this by species? maybe use series instead of group by
    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mode.html
    