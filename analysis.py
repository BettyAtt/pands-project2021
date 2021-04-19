# pands-project2021 
# Author: Betty Attwood G00398300 
# Final Project for Programming & Scripting Module as a part of
# GMIT's Higher Diploma in Computer Science Data Analytics

# This program analyses and creates plots of Fisher's Iris Data Set 

# Uploading the libraries needed for this project:
import pandas as pd
import numpy 
import matplotlib
import seaborn
import sklearn

#  Uploading UCI's Iris dataset and adding some structure to it 
data = pd.read_csv('iris.data', header=None)  # reading in the data file 
data.columns = ['SepalLength_cm','SepalWidth_cm','PetalLength_cm','PetalWidth_cm','Class'] # adding column names to files
print(data.head(8)) # used to test that the dataset loaded correctly; once confirmed blocked out.
# ?? Should I look at error handling here for uploading datasets?? Review later

