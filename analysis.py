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
irisData = pd.read_csv('iris.data', header=None)  # reading in the data file 

# code for creating and writing a txt file of the summary information about this data set

with open("iris_summary.txt", "w") as f:
# Basic investigation into the dataset:
# Next step: research how to add below data to the .txt file I opened rather than print to terminal and how to end block 
    print(irisData.info()) # this gives the basic information about the dataframe inclding the range index, 
#number of data columns, column numbers and how many non-null objects, as well as the dtype for each column content.
# finally it give the memory usage and null values.
irisData.columns = ['SepalLength_cm','SepalWidth_cm','PetalLength_cm','PetalWidth_cm','Species'] # adding column names to files

# ?? Should I look at error handling here for uploading datasets?? Review later

print(irisData.shape) # this gives me the shape of the matrix or data table - 150 rows, five columns
print(irisData.columns) # this prints the Index with the titles of the columns:
# Index(['SepalLength_cm', 'SepalWidth_cm', 'PetalLength_cm', 'PetalWidth_cm', 'Class'], dtype='object')
print(irisData["Species"].value_counts())
print(irisData.describe()) # is the describe function meaningful on the 
#whole set of would it be better isolated by class type?

