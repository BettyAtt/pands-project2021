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
    irisData = pd.read_csv('iris.data', names =["sepal length in cm", "sepal width in cm", "petal length in cm", "petal width in cm", "Species"])  # reading in the data file 
    df = pd.DataFrame(irisData)  

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
-  `.shape`  [8] provides a tuple of the dimensions of the dataframe.  
  returns:  ``(150, 5)``

- `.columns`
-  `.describe`
-  `.value_counts()`.  

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




### References for Part 2.3  

[1] RealPython.com "Python With Open As Pattern" Available: https://realpython.com/working-with-files-in-python/#pythons-with-open-as-pattern  [Accessed 19 April 2021].      
[2] Mertz, J. RealPython.com "Reading and Writing Files in Python (Guide)" Available: https://realpython.com/read-write-files-python/  [Accessed 19 April 2021].  
[3] w3schools.com. "Python File Write" Available: https://www.w3schools.com/python/python_file_write.asp [Accessed 19 April 2021].  
[4] w3resource.com "Pandas DataFrame: to_string() function" Available: https://www.w3resource.com/pandas/dataframe/dataframe-to_string.php [Accessed 19 April 2021].  
[5] Datacamp. "Pandas Tutorial: DataFrames in Python" Available: https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python [Accessed 19 April 2021].  
[6] w3schools.com "Python Type() Function" Available: https://www.w3schools.com/python/ref_func_type.asp [Accessed 20 April 2021].
[7] w3resources.com "Pandas DataFrame .info Function" Available: https://www.w3resource.com/pandas/dataframe/dataframe-info.php [Accseed 20 April 2021].
[8] w3resource.com "Pandas Dataframe Property:Shape" Available: https://www.w3resource.com/pandas/dataframe/dataframe-shape.php [Accseed 20 April 2021].