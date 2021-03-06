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

#  Uploading UCI's Iris dataset and adding column names to it 

csv = ('iris.data')
names = ["sepal length in cm", "sepal width in cm", "petal length in cm", "petal width in cm", "Species"]
irisData = pd.read_csv(csv, names=names)


# code for creating and writing a txt file of the summary information about this data set

with open("iris_summary.txt", "w") as f:
    f.write("This file contains basic data regarding the file type and contents of Fisher's Iris Data Set.\n\n\n")
    # Basic investigation into the dataset:
    f.write("Object Type for iris Data:\n\n" + str(type(irisData)) + "\n\n\n")
    f.write("This shows the basic info of the data set.\nIt includes a sampling of the head and tail of the data, the index and the number of rows and columns.\n\n" + str(irisData.info) + "\n\n\n")
    irisShape = irisData.shape # this gives me the shape of the matrix or data table - 150 rows, five columns
    f.write("Data Table Shape; The number of rows and number of columns:\n\n " + str(irisShape) + "\n\n\n")
    f.write("The Index of the columns are provided below along with the datatype:\n\n" + str(irisData.columns) + "\n\n\n") # this prints the Index showing titles of the columns)
    descriptives = irisData.describe()
    f.write("Table Summary of the Statistics of the Data Set Variables:\n\n" + descriptives.to_string() + "\n\n\n")
    f.write("The Iris data set is a balaced data set.\nBreakdown of the data by species:\n\n" + str(irisData["Species"].value_counts()) 
    + "\n\n\n")
    f.write("Digging Deeper into the Data - Examining by Species\n\n\n\n")
    # Mean, Median, Max & Min values of each attribute by class
    f.write("Pivot Table Showing Each Species Mean Measurements: \n\n" + str(irisData.pivot_table(index='Species', values=["sepal length in cm", "sepal width in cm", "petal length in cm", "petal width in cm"], aggfunc=np.mean)) + "\n\n")
    f.write("Pivot Table Showing Each Species Median Measurements: \n\n" + str(irisData.pivot_table(index='Species', values=["sepal length in cm", "sepal width in cm", "petal length in cm", "petal width in cm"], aggfunc=np.median)) + "\n\n")
    f.write("Pivot Table Showing Each Species Max Measurements: \n\n" + str(irisData.pivot_table(index='Species', values=["sepal length in cm", "sepal width in cm", "petal length in cm", "petal width in cm"], aggfunc=np.max)) + "\n\n")
    f.write("Pivot Table Showing Each Species Min Measurements: \n\n" + str(irisData.pivot_table(index='Species', values=["sepal length in cm", "sepal width in cm", "petal length in cm", "petal width in cm"], aggfunc=np.min)) + "\n\n")
    # https://www.w3resource.com/python-exercises/pandas/excel/pandas-pivot-exercise-13.php  max and min for pivot tables
    
# Plots

# Histograms of the variables

#sepal length
sns.set_style("darkgrid")
sns.displot(irisData, x = "sepal length in cm", hue="Species", kde=True, multiple="dodge") # hue color codes by that variable
# dodge makes the different species easier to see # kde adds a kernal density estimator line to the plot
plt.title("Sepal Lengths of Iris Species in CM")
plt.tight_layout()  # tightens layout to help prevent titles from being cut off
plt.subplots_adjust(top=0.88) # adjusts top to prevents title from being cut off
plt.savefig('Histogram_All_SepalLength.png') # Saves the plot as a png image
plt.show() # pops up the image of the plot when the program runs

sns.set_style("darkgrid")
sns.displot(data=irisData, x="sepal length in cm", hue="Species", col="Species", kde=True)  
plt.suptitle("Sepal Lengths in CM")
plt.tight_layout() 
plt.subplots_adjust(top=0.88) 
plt.savefig('Histogram_Individual_SepalLength.png')
plt.show() 

# sepal width
sns.set_style("darkgrid")
sns.displot(irisData, x = "sepal width in cm", hue="Species", kde=True, multiple="dodge") # hue color codes by that variable
# dodge makes the different species easier to see # kde adds a kernal density estimator line to the plot
plt.title("Sepal Widths of Iris Species in CM")
plt.tight_layout() 
plt.subplots_adjust(top=0.88) 
plt.savefig('Histogram_All_SepalWidth.png') # Saves the plot as a png image
plt.show() # pops open the plot when the program runs

sns.set_style("darkgrid")
sns.displot(data=irisData, x="sepal width in cm", hue="Species", col="Species", kde=True) 
plt.suptitle("Sepal Width in CM")
plt.tight_layout() 
plt.subplots_adjust(top=0.88)  
plt.savefig('Histogram_Individual_SepalWidth.png')
plt.show() 

# petal length
sns.set_style("darkgrid")
sns.displot(irisData, x = "petal length in cm", hue="Species", kde=True, multiple="dodge") # hue color codes by that variable
# dodge makes the different species easier to see # kde adds a kernal density estimator line to the plot
plt.title("Petal Length of Iris Species in CM")
plt.tight_layout() 
plt.subplots_adjust(top=0.88) 
plt.savefig('Histogram_All_PetalLength.png')
plt.show() 

sns.set_style("darkgrid")
sns.displot(data=irisData, x="petal length in cm", hue="Species", col="Species", kde=True)  
plt.suptitle("Petal Length in CM")
plt.tight_layout() 
plt.subplots_adjust(top=0.88) 
plt.savefig('Histogram_Individual_PetalLength.png')
plt.show() 

# petal width
sns.set_style("darkgrid")
sns.displot(irisData, x = "petal width in cm", hue="Species", kde=True, multiple="dodge") # hue color codes by that variable
# dodge makes the different species easier to see # kde adds a kernal density estimator line to the plot
plt.title("Petal Width of Iris Species in CM")
plt.tight_layout() 
plt.subplots_adjust(top=0.88) 
plt.savefig('Histogram_All_PetalWidth.png')
plt.show()

sns.set_style("darkgrid")
sns.displot(data=irisData, x="petal width in cm", hue="Species", col="Species", kde=True)
plt.suptitle("Petal Width in CM")
plt.tight_layout() 
plt.subplots_adjust(top=0.88)   
plt.savefig('Histogram_Individual_PetalWidth.png')
plt.show()

# Making Boxplots:
# set of boxplots with swarm overlay to located outliers
figboxplot, (ax1, ax2, ax3, ax4) = plt.subplots(1,4, figsize=(14,12)) 
plt.suptitle("Boxplots with Swarmplots Comparing the Four Variables", y= 1.0001)
# setout the number of subplots in the figure, the number of rows and columns,
# and the size of the total figure.
sns.boxplot(x='Species',y='sepal length in cm',data=irisData, ax=ax1) # x axis on all plots is Species, 
# y is the individual variables, and the ax tells which subplot to plot the data to.
sns.swarmplot(x="Species", y="sepal length in cm", data=irisData, color="brown", ax=ax1) 
# overlay of swarmplot to better determine outliers
# code adapted from https://www.kaggle.com/biphili/seaborn-matplotlib-iris-data-visualization-code-1
ax1.set_ylabel("Lenght/Width in cm") #labeling the axis
ax1.set_xlabel("Sepal Lenght in cm")

sns.boxplot(x='Species',y='sepal width in cm',data=irisData, ax=ax2)
sns.swarmplot(x="Species", y="sepal width in cm", data=irisData, color="brown", ax=ax2)
ax1.set_ylabel("") # no label as this lays in the middle of the figure
ax1.set_xlabel("Sepal Width in cm")

sns.boxplot(x='Species',y='petal length in cm',data=irisData, ax=ax3)
sns.swarmplot(x="Species", y="petal length in cm", data=irisData, color="brown", ax=ax3)
ax1.set_ylabel("")
ax1.set_xlabel("Petal Length in cm")

sns.boxplot(x='Species',y='petal width in cm',data=irisData, ax=ax4)
sns.swarmplot(x="Species", y="petal width in cm", data=irisData, color="brown", ax=ax4)
ax1.set_ylabel("")
ax1.set_xlabel("Petal Width in cm")
plt.savefig("IrisBoxplots.png")
plt.show()


# Making Scatterplots:
# Pairplot: Seaborn has functionality that allows for visualisation of multidimensional relationships in the data.
sns.set_style("whitegrid")
sns.pairplot(irisData, hue = "Species", diag_kind = "hist", palette = "colorblind", height = 2)
plt.suptitle("Pairplot Comparing the Four Variables", y= 1.0001) #y = > 1 so the title appears slightly above the plot
plt.savefig("pairplot.png")
plt.show()
# reference: https://jakevdp.github.io/PythonDataScienceHandbook/04.14-visualization-with-seaborn.html


# Individual Scatterplots:

#sepal length sepal width scatterplot
sns.set_style("whitegrid") # add background grid and set style
sns.FacetGrid(irisData, hue="Species", height=4).map(plt.scatter,"sepal length in cm","sepal width in cm").add_legend()
# Facet grid shows conditional relationships. Hue specifies what variable sets the color coding of the plot. 
#.map sets the type of plot and then columns for the x and y axis. Legend had to be added to explain what the colors represent.
plt.title("Examining Sepal Length and Sepal Width Correlation")
plt.subplots_adjust(top=0.88) # adjusts height so title isnt cut off
plt.savefig("scatter_sl_sw.png")
plt.show()

#sepal length petal width scatterplot
sns.set_style("whitegrid")
sns.FacetGrid(irisData, hue="Species", height=4).map(plt.scatter,"sepal length in cm","petal length in cm").add_legend()
plt.title("Examining Sepal Length and Petal Length Correlation")
plt.subplots_adjust(top=0.88)
plt.savefig("scatter_sl_pl.png")
plt.show()

#sepal length petal width scatterplot
sns.set_style("whitegrid")
sns.FacetGrid(irisData, hue="Species", height=4).map(plt.scatter,"sepal length in cm","petal width in cm").add_legend()
plt.title("Examining Sepal Length and Petal Width Correlation")
plt.subplots_adjust(top=0.88)
plt.savefig("scatter_sl_pw.png")
plt.show()

#sepal width petal length scatterplot
sns.set_style("whitegrid")
sns.FacetGrid(irisData, hue="Species", height=4).map(plt.scatter,"sepal width in cm","petal length in cm").add_legend()
plt.title("Examining Sepal Width and Petal Length Correlation")
plt.subplots_adjust(top=0.88)
plt.savefig("scatter_sw_pl.png")
plt.show()

#sepal width petal width scatterplot
sns.set_style("whitegrid")
sns.FacetGrid(irisData, hue="Species", height=4).map(plt.scatter,"sepal width in cm","petal width in cm").add_legend()
plt.title("Examining Sepal Width and Petal Width Correlation")
plt.subplots_adjust(top=0.88)
plt.savefig("scatter_sw_pw.png")
plt.show()

#petal length petal width
sns.set_style("whitegrid")
sns.FacetGrid(irisData, hue="Species", height=4).map(plt.scatter,"petal length in cm","petal width in cm").add_legend()
plt.title("Examining Petal Length and Petal Width Correlation")
plt.subplots_adjust(top=0.88)
plt.savefig("scatter_pl_pw.png")
plt.show()

print("The program has completed the analysis of the Iris data set and printed detailed analysis to the file:iris_summary.txt.\nThe program has also saved images (.png files) of plots to the current working directory. ")