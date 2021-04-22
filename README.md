 # pands-project2021 
___
# Title: PANDS Project 2021 
# Author: Betty Attwood G00398300
![GMIT_LOGO](gmit_logo.png)
___
## About the Project:
This project analyses the well-known Fisher’s Iris data set [1] using Python [2]. This repository documents the researching of the data set, the documentation, and the code (in Python) used to investigate it.  
This project forms part of the coursework required for the module Programming & Scripting, a core module of GMIT's Higher Diploma of Computer Science in Data Analytics.

# README Table of Contents
1. Introduction - brief introduction to the history of Iris data set and its significance in data analytics.
2. Analysing the Data Set
3. 
4. 
5. 

# Breakdown of Tasks

Break down Tasked based on Project Objectives:  
• outputs a summary of each variable to a single text file,  
• saves a histogram of each variable to png files, and  
• outputs a scatter plot of each pair of variables.    

First Consideration: Framework  

1. Set up basic python project that imports Fisher's Iris Data Set and import libraries needed
2. Figure out how to parse specific data from the data set
3. Select from data set information I want to document and compare  

Second Consideration: Logic  

1. Output a summary of each variable
2. Write to a text file
3. Get variable data for a histogram
4. Save histogram as png
5. Use variable data to create scatter plot of paired variables  

Third Consideration: Presentation  

1. In program documentation so anyone can run it and understand what it is doing. i.e any prompts or data shown is clearly defined
2. In code documentation of what each block of text does along with what imports it is dependent on.
3. Formatting of summary text files and images for the best experience of the end user.
4. Ensure README file is thorough and includes sources referenced



# 1. Introduction - History & Significance of the Iris Data Set

Fisher's Iris data set is well known because it provides a manageably small but robust enough real world multivariagate data set [3]. This is ideal for use in a wide scope of problem solving scenarios including statistical analysis, statistical graphics, multivariate statistics and machine learning [4].  

Ronald Aylmer Fisher, later knighted for his work in statistics [3], wrote a paper in 1936 titled "The Use of Multiple Measurements in Taxonomic Problems" in which the Iris data set first appears [5]. The data set is a balanced data set consisting of 150 samples. It is considered a balanced dataset because it breaks down into 50 samples from each of three species of Iris (*Iris setosa, Iris versicolor, and Iris virginica*) [5].  Fisher's Iris data set is a multivariate data set containing four variable: sepal length and width, and petal length and width as well as the class (the three species of Iris). 

The data was used by Fisher with permission by Dr Edgar Anderson, who picked and measured two of the three species on the Gaspé Peninsula in Canada. The data Dr Anderson collected for each sample included sepal length in cm, sepal width in cm, petal length in cm, and petal width in cm [5]. In the article [5], Fisher developed and evaluated a linear function to differentiate between Iris species based on these four measurements [3]. 

![Image of Three Species with Petal and Sepals Labeled](Image3SpeciesTypesPetalSepal.png)   
Image Credit *Plural Sight* [6]

Fisher's Iris data set is an ideal starting point for learning data mining techniques. Data mining is digging through data to look for connections and predict trends. SAS notes data mining is a culmination of "three intertwined scientific disciplines: statistics (the numeric study of data relationships), artificial intelligence (human-like intelligence displayed by software and/or machines) and machine learning (algorithms that can learn from data to make predictions)" [7]. Machine Learning is a popular area of use as the data set is ideal for teaching beginners principles of machine learning as well as serving as an ideal test for new sorting and classifying methods. It is so commonly used that the machine learning library for Python Scikit-Learn (sk-learn) includes it as one of the loadable data sets. The data set is also freely available for download and use from UC Irvine's Machine Learning Repository [1]. UC Irvine's Machine Learning Repository enumerates the many published papers that reference this dataset showing the wide range of domains it is used in especially in the domains of computer science and statistics [1]. 

### References for Part 1:  

[1] UC Irvine Machine Learning Repository. Iris data set.
http://archive.ics.uci.edu/ml/datasets/Iris.  [Accessed 9 April 2021]  
[2] Python Software Foundation. Welcome to python.org. https://www.python.org/.  
[3] Cui, Y. (2020, April 25). "The Iris Dataset-A Little Bit of History and Biology." Towards Data Science. Available: https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5 [Accessed 17 April 2021]  
[4] Cox, N. (2013) "Aspects of the Iris data set". Stack Exchange. Available: https://stats.stackexchange.com/questions/74776/what-aspects-of-the-iris-data-set-make-it-so-successful-as-an-example-teaching [Accessed 17 April 2021]   
[5] Fisher, R.A. (1936), The Use of Multiple Measurements in Taxonomic Problems. *Annals of Eugenics*, 7: 179-188. Available: https://doi.org/10.1111/j.1469-1809.1936.tb02137.x [Accessed 17 April 2021]
[6] Singhal, G. (2020) *Plural Sight* "Designing a Machine Learning Model" Available: https://www.pluralsight.com/guides/designing-a-machine-learning-model [Accessed 17 April 2021]
[7] SAS. (2021). 'What is Data Mining?' Available: https://www.sas.com/en_ie/insights/analytics/data-mining.html [Accessed 17 April 2021]

# 2 Analysing the Iris Data Set
## 2.1 Setting Up the Environment, & Libraries & Modules  

### 2.1.1 Downloading the Dataset

Before beginning the analysis, the data set had to be downloaded. It is available from UCI Machine Learning Repository or can be loaded in Pythopn using sk-learn. As the dataset is requested to be uploaded to the repository I downloaded the file from UCI Machine Learning Database as a .data file. These .data files hold data in either comma seperated value (.csv) format or in tab seperated value format and the data may be in text or binary format [1]. The iris.data file opened in VS Code in csv format and was in text.  

### 2.1.2 The Programming Environment

I completed the project using Python 3.8.5 via Conda 4.9.2.  
Tasks were run through the code editor VS Code Version 1.55.0.  
All the code and documentation is stored publically on my GitHub repository.  
Various libraries were imported for this project:

1. pandas
2. numpy
3. matplotlib
4. seaborn
5. sklearn

These libraries were imported using the follow code:  

    import pandas as pd
    import numpy 
    import matplotlib
    import seaborn
    import sklearn

Informatiom about the libraries imported and their relevance to the project:  


- pandas: Pandas is a library specifically for working with data sets. It helps with analyzing, cleaning, exploring, and manipulating data [3].   

- numpy: NumPy stands for numberical Python and is particularly useful as its `nparray` feature allows for speed in dealing with arrays. [2]  

- matplotlib: MatPlotLib is a low level graph plotting function that allows for visualisation of data in plot format. Many of the most useful functions are under the submodule `pyplot` often downloaded as `plt`  [4]
    import matplotlib.pyplot as plt  
This library is useful for making some of the simpler plots to illustrate the dataset.   

- seaborn: Seaborn library works with matplotlib and its strengths lay in visualising random distributions [5].  

- sklearn: Scikit Learn (sklearn) is a machine learning library. It is a predicitive data analysis tool built on NumPy, SciPy, and Matplotlib [6]. It also has the iris data set as one of its built-in data set options.   




### References for Part 2.1:

[1] AskPython.com "How to Read a .data file?"  Available: https://www.askpython.com/python/examples/read-data-files-in-python [Accessed 18 April 2021]   
[2] w3schools.com "NumPy Introduction" Available: https://www.w3schools.com/python/numpy/numpy_intro.asp [Accessed 18 April 2021].     
[3] w3schools.com "Pandas Introduction" Available: https://www.w3schools.com/python/pandas/pandas_intro.asp  [Accessed 18 April 2021].    
[4] w3schools.com "Matplotlib Introduction" Available: https://www.w3schools.com/python/matplotlib_intro.asp [Accessed 18 April 2021].    
[5] w3schools.com "Seaborn Module" Available: https://www.w3schools.com/python/numpy/numpy_random_seaborn.asp [Accessed 18 April 2021].   
[6] Scikit-learn.org "Scikit=Learn Tutorial" Available: https://scikit-learn.org/stable/tutorial/basic/tutorial.html [Accessed 18 April 2021].  

### 2.2 Importing the Data Set  

Once the libraries have been added and the data set downnloaded from UCI's Machine Learning Repository,
the next step is to save the UCI `.data` file into my repository folder and to read it into my ``analysis.py`` file.  

There are several methods for opening the Iris data set in a Python program that I encountered while researching. I chose to import pandas as `pd` and use the read in function [1] as the  iris.data file is structured in a csv format [4]: `pd.read_csv()`.  
I chose this method because it is straightforward and the pandas module is a foundational library for data analysis. Other options for importing including using JSON or pickle [4], but the pandas method seemed sufficient for this task. Also, pandas did not involve the more complicated capabilities of scikit-learn which might not be necessary at the beginner level[2] or the extra conversion steps of shutil and loss of metadata [3] which were other options for completing this task. 

### Referenences for Part 2.2  

[1] w3schools.com "Pandas Tutorial" Available: https://www.w3schools.com/python/pandas/pandas_csv.asp [Accessed 19 April 2021]  
[2] Scikit-Learn.org "Loading Iris Data Set" Available: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html [Accessed 19 April 2021].    
[3] Python Docs. "Shutil- High Level File Operations"Available: https://docs.python.org/3/library/shutil.html [Accessed 19 April 2021].    
[4]  AskPython.com "How to Read a .data file?"  Available: https://www.askpython.com/python/examples/read-data-files-in-python [Accessed 18 April 2021].  


# 2.3 Analysing: Parsing the dataset  

## 2.3.1 Reading in the Data  

The csv dataset read in from the `.data` file is named as a variable, irisData, and then I created a dataframe, df, for it [4] The dataframe allows for two dimensional labeled data structures with columns of potentially different types [5].:  
``irisData = pd.read_csv('iris.data', names =["sepal length in cm", "sepal width in cm", "petal length in cm", "petal width in cm", "Species"])`` 
  

## 2.3.2 Writing to a .txt File  

One of the primary objectives of the project is to analyse the data using python and to generate a summary of the data in `.txt` file format. I used the `with open()` method of populating my data to a .txt file [1]. This method was chosen because it will automatically close the file once I leave the block [2].   

The code used is: 
`with open("iris_summary.txt", "w") as f:`  
The write ("w) option was chosen as I want the program to create the file if it does not already exist and write over it each time the program is ran [3]. This is important because if changes are made to the dataset, the information in the `.txt` file will be automatically updated when the program runs with the new data.  

## 2.3.3 Parsing the Dataset as a whole

The various elements of analysis were wrapped in `f.write()` to have the resulting analysis automatically written to the .txt file.  

`f.write("This file contains basic data regarding the file type and contents of Fisher's Iris Data Set.\n\n\n")`  

Then the basic analysis comprised of running several in-built pandas functions including:
- ``type()`` returning the type of the specified object [6]  
  returns: `<class 'pandas.core.frame.DataFrame'>`
-  ``.info`` [7] provides a concise summary of the dataframe.  
 returns: 
 ``` 
    <bound method DataFrame.info of      sepal length in cm  sepal width in cm  petal length in cm  petal width in cm         Species
0                   5.1                3.5                 1.4                0.2     Iris-setosa
1                   4.9                3.0                 1.4                0.2     Iris-setosa
2                   4.7                3.2                 1.3                0.2     Iris-setosa
3                   4.6                3.1                 1.5                0.2     Iris-setosa
4                   5.0                3.6                 1.4                0.2     Iris-setosa
..                  ...                ...                 ...                ...             ...
145                 6.7                3.0                 5.2                2.3  Iris-virginica
146                 6.3                2.5                 5.0                1.9  Iris-virginica
147                 6.5                3.0                 5.2                2.0  Iris-virginica
148                 6.2                3.4                 5.4                2.3  Iris-virginica
149                 5.9                3.0                 5.1                1.8  Iris-virginica

[150 rows x 5 columns]>
```
-  `.shape`   provides a tuple of the dimensions of the dataframe.[8]  
  returns:  ``(150, 5)``

- `.columns` returns the index of the columns along with the data type.
  returns: ``Index(['sepal length in cm', 'sepal width in cm', 'petal length in cm', 'petal width in cm', 'Species'],dtype='object')``  

-  `.describe`provides a summary of statistics about the data frame columns including mean, sample standard deviation, and interquartile range [9].  
 returns:`sepal length in cm  sepal width in cm  petal length in cm  petal width in cm
count          150.000000         150.000000          150.000000         150.000000
mean             5.843333           3.054000            3.758667           1.198667
std              0.828066           0.433594            1.764420           0.763161
min              4.300000           2.000000            1.000000           0.100000
25%              5.100000           2.800000            1.600000           0.300000
50%              5.800000           3.000000            4.350000           1.300000
75%              6.400000           3.300000            5.100000           1.800000
max              7.900000           4.400000            6.900000           2.500000 `
-  `.value_counts()`.  returns a series the counts of unique rows in the dataframe [10].  
 returns:  
 `Iris-setosa        50
Iris-virginica     50
Iris-versicolor    50
Name: Species, dtype: int64`

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

Issues: for .info getting:         # look at the <bound dataframe.info issue later -- https://stackoverflow.com/questions/46239946/attempt-to-access-dataframe-column-displays-bound-method-ndframe-xxx
        # https://www.reddit.com/r/learnprogramming/comments/3yx9er/python_what_does_it_mean_to_call_something/
        Also key: https://pandas.pydata.org/pandas-docs/version/0.25.3/reference/api/pandas.DataFrame.info.html
In Progress: Issues with reading in -- tried .df and didnt work -- tried without and got errors but solved with using str to convert tuples into writeable format. Add step by step instructions here. shape - w3schools.com "Numpy Array Shape" Available: https://www.w3schools.com/python/numpy/numpy_array_shape.asp [Accessed 19 April 2021]. Pandas Dataframe.info would not print to the doc pandas.pydata.org "Pandas DataFrame.Info" Available: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html [Accessed 19 April 2021].  learndatasci.org Pandas Python Tutorial Available: https://www.learndatasci.com/tutorials/python-pandas-tutorial-complete-introduction-for-beginners/  [Accessed 19 April 2021]. 

## 2.3.3 Drilling into the Data - Parsing by Species of Iris
More meaningful data could be obtained by using either the groupby() functions of pandas or converting the dataframe into a pivot table to isolate the three species types and look at the statistical information for each of them.  
Code Block:  
`f.write("Digging Deeper into the Data - Examining by Species\n\n\n\n")
    # Max, Min & Median values of each attribute by class
    f.write("Maximum values for each attribute by Species: \n\n" + str(irisData.groupby('Species').max()) +"\n\n")
    f.write("Minimum values for each attribute by Species: \n\n" + str(irisData.groupby('Species').min()) +"\n\n")
    f.write("Median values for each attribute by Species: \n\n" + str(irisData.groupby('Species').median()) +"\n\n")
    f.write("Pivot Table Showing Each Species Mean Measurements: \n\n" + str(irisData.pivot_table(index='Species', values=["sepal length in cm", "sepal width in cm", "petal length in cm", "petal width in cm"], aggfunc=np.mean)) + "\n\n")
    f.write("Pivot Table Showing Each Species Median Measurements: \n\n" + str(irisData.pivot_table(index='Species', values=["sepal length in cm", "sepal width in cm", "petal length in cm", "petal width in cm"], aggfunc=np.median)) + "\n\n")
    f.write("Pivot Table Showing Each Species Max Measurements: \n\n" + str(irisData.pivot_table(index='Species', values=["sepal length in cm", "sepal width in cm", "petal length in cm", "petal width in cm"], aggfunc=np.max)) + "\n\n")
    f.write("Pivot Table Showing Each Species Min Measurements: \n\n" + str(irisData.pivot_table(index='Species', values=["sepal length in cm", "sepal width in cm", "petal length in cm", "petal width in cm"], aggfunc=np.min)) + "\n\n")`

    Breakdown of the code:  
    The groupby() Method:
    `'str(irisData.groupby('Species').max())` and `.min()``, `.median()` The groupby() function with dataframes allows grouping by an obect, in this case the variable 'Species' and the ``.agg`` function is used to return a single aggregated value for each group (such as max, min, median) [11]. 
    returns: 
    `                 sepal length in cm  sepal width in cm  petal length in cm  petal width in cm
Species                                                                                      
Iris-setosa                     5.8                4.4                 1.9                0.6
Iris-versicolor                 7.0                3.4                 5.1                1.8
Iris-virginica                  7.9                3.8                 6.9                2.5

Minimum values for each attribute by Species: 

                 sepal length in cm  sepal width in cm  petal length in cm  petal width in cm
Species                                                                                      
Iris-setosa                     4.3                2.3                 1.0                0.1
Iris-versicolor                 4.9                2.0                 3.0                1.0
Iris-virginica                  4.9                2.2                 4.5                1.4

Median values for each attribute by Species: 

                 sepal length in cm  sepal width in cm  petal length in cm  petal width in cm
Species                                                                                      
Iris-setosa                     5.0                3.4                1.50                0.2
Iris-versicolor                 5.9                2.8                4.35                1.3
Iris-virginica                  6.5                3.0                5.55                2.0`

The pivot table method:  
The pandas .pivot_table method allows for data digging by creating multiindex objects and allowing selective summaries of the table [11]. Here I chose 'Series' as the index and investigated this for the values of sepal lenth, sepal width, petal length, and petal width.  
`(irisData.pivot_table(index='Species', values=["sepal length in cm", "sepal width in cm", "petal length in cm", "petal width in cm"], aggfunc=np.mean))`
results: `
                 petal length in cm  petal width in cm  sepal length in cm  sepal width in cm
Species                                                                                      
Iris-setosa                   1.464              0.244               5.006              3.418
Iris-versicolor               4.260              1.326               5.936              2.770
Iris-virginica                5.552              2.026               6.588              2.974

Pivot Table Showing Each Species Median Measurements: 

                 petal length in cm  petal width in cm  sepal length in cm  sepal width in cm
Species                                                                                      
Iris-setosa                    1.50                0.2                 5.0                3.4
Iris-versicolor                4.35                1.3                 5.9                2.8
Iris-virginica                 5.55                2.0                 6.5                3.0

Pivot Table Showing Each Species Max Measurements: 

                 petal length in cm  petal width in cm  sepal length in cm  sepal width in cm
Species                                                                                      
Iris-setosa                     1.9                0.6                 5.8                4.4
Iris-versicolor                 5.1                1.8                 7.0                3.4
Iris-virginica                  6.9                2.5                 7.9                3.8

Pivot Table Showing Each Species Min Measurements: 

                 petal length in cm  petal width in cm  sepal length in cm  sepal width in cm
Species                                                                                      
Iris-setosa                     1.0                0.1                 4.3                2.3
Iris-versicolor                 3.0                1.0                 4.9                2.0
Iris-virginica                  4.5                1.4                 4.9                2.2
`



### References for Part 2.3  

[1] RealPython.com "Python With Open As Pattern" Available: https://realpython.com/working-with-files-in-python/#pythons-with-open-as-pattern  [Accessed 19 April 2021].      
[2] Mertz, J. RealPython.com "Reading and Writing Files in Python (Guide)" Available: https://realpython.com/read-write-files-python/  [Accessed 19 April 2021].  
[3] w3schools.com. "Python File Write" Available: https://www.w3schools.com/python/python_file_write.asp [Accessed 19 April 2021].  
[4] w3resource.com "Pandas DataFrame: to_string() function" Available: https://www.w3resource.com/pandas/dataframe/dataframe-to_string.php [Accessed 19 April 2021].  
[5] Datacamp. "Pandas Tutorial: DataFrames in Python" Available: https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python [Accessed 19 April 2021].  
[6] w3schools.com "Python Type() Function" Available: https://www.w3schools.com/python/ref_func_type.asp [Accessed 20 April 2021].
[7] w3resources.com "Pandas DataFrame .info Function" Available: https://www.w3resource.com/pandas/dataframe/dataframe-info.php [Accessed 20 April 2021].
[8] w3resource.com "Pandas Dataframe Property:Shape" Available: https://www.w3resource.com/pandas/dataframe/dataframe-shape.php [Accessed 20 April 2021].
[9] tutorialspoint.com "Python Pandas Descriptive Statistics" Available: tutorialspoint.com/python_pandas/python_pandas_descriptive_statistics.htm [Accessed 20 April 2021].
[10] pandas.pydata.org "Pandas .DataFrame.value_counts" Available: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.value_counts.html [Accessed 20 April 2021].
[11] pydata.org "Pandas pivot_table" Available: https://pandas.pydata.org/docs/reference/api/pandas.pivot_table.html [Accessed 21 April 2021].

# Section 3 Visualising the Data
I chose to use the Python library Seaborn which builds upon Matplotlib to create high quality statistical graphics [1]. 
Seaborn.pydata.org has extensive information on how to create plots to show relational, distributional, categorical, and regression with customisation of plot types, layout and colour and grid options.

# 3.1.1 Histograms of the Variables

The first step is to create histograms of the variables (sepal length, sepal width, petal length, petal width).
``sns.displot`` the first step is to call seaborn and specify plot chosen as histogram ``.displot()``. 
Then we define the parameters of the histplot ``(irisData, x = "sepal length in cm", hue="Species", kde=True, binwidth=0.2)`` Firstly it specifies the data it is to use is my dataset irisData, the x axis indicates we are looking at the sepal length in cm, the y is by default set to count, the hue specifies which columns in the data seaborn uses to set its color encoding, I have set it to colour code by Species [1]. The kde option stands for kernel density estimate. "Rather than using discrete bins, a KDE plot smooths the observations with a Gaussian kernel, producing a continuous density estimate" [2] By plotting this you can visualize the distribution of observartions in a dataset analagous to a histogram [3]. The bin is when the entire range of values is divided into a series of intervals so that it can be counted how many values fall into each interval[4]. The bars on the histogram are called bins. By default the number of bins assigned based on the amount of variables but can be adjusted. The height of each bin shows how many values from the data fall into that range [5]. The width of each bin is equal to the (max value of data – min value of data) / total number of bins. Since there are multiple variables we are looking at, ``multiple="dodge"`` is used to display them more clearly in the histographs that contain data regarding all three species of Iris [6]. Other options were using a "layer" or "step" approach but in this case the dodge made it easiest to see the counts of measurements the distinctive Iris types.

``plt.grid()`` A grid is used to make understanding the data easier. 

``plt.savefig('Histogram_All_SepalLength.png')`` Matplotlib Pyplot has an option to save plots into a image file such as a png. [7] This saves to the current working directory.
``plt.clf()`` This clears the current figure from the code so that it does not add all the plots to one file [8]

This process is repeated for sepal width, petal length, petal width in lines ENTER LINES HERE of the code.

-- Graphs of the general data -- min, max, deviation, etc?

--Scatterplots view seaborn tutorial.

### References 3.1.1  

[1] seaborn.pydata.org "Seaborn Introduction" Available: https://seaborn.pydata.org/#:~:text=Seaborn%20is%20a%20Python%20data,attractive%20and%20informative%20statistical%20graphics. [Accessed 22 April 2021].  
[2] seaborn.pydata.org "Seaborn Tutorial: KDE plots" Available: https://seaborn.pydata.org/tutorial/distributions.html#tutorial-kde [Accessed 22 April 2021].  
[3] seaborn.pydata.org "KDE Plots" Available: https://seaborn.pydata.org/generated/seaborn.kdeplot.html [Accessed 22 April 2021].  
[4]. Datacamp. "Histograms in Matplotlib" Available: https://www.datacamp.com/community/tutorials/histograms-matplotlib [Accessed 22 April 2021].  
[5] geeksforgeeks.org "Bin Size in MatPlotLib Histogram" Available: https://www.geeksforgeeks.org/bin-size-in-matplotlib-histogram/#:~:text=Width%20of%20each%20bin%20is,pyplot. [Accseed 22 April 2021].
[6] seaborn.pydata.org "Seaborn Distrubution Tutorial" Available: https://seaborn.pydata.org/tutorial/distributions.html [Accessed 22 April 2021].
[7] Matplotlib.org "Pyplot Savefig" Available: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html [Accessed 22 April 2021]
[8] Matplotlib.org "Pyplot.clf" Available: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.clf.html [Accessed 22 April 2021].