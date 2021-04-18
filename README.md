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
3. Packages Used


# 1. Introduction - History & Significance of the Iris Data Set

Fisher's Iris data set is well known because it provides a manageably small but robust enough real world multivariagate data set [3]. This is ideal for use in a wide scope of problem solving scenarios including statistical analysis, statistical graphics, multivariate statistics and machine learning [4].  

Ronald Aylmer Fisher, later knighted for his work in statistics [3], wrote a paper in 1936 titled "The Use of Multiple Measurements in Taxonomic Problems" in which the Iris data set first appears [5]. The data set is a balanced data set consisting of 150 samples. It is considered a balanced dataset because it breaks down into 50 samples from each of three species of Iris (*Iris setosa, Iris versicolor, and Iris virginica*) [5].  

The data was used by Fisher with permission by Dr Edgar Anderson, who picked and measured two of the three species on the Gaspé Peninsula in Canada. The data Dr Anderson collected for each sample included sepal length in cm, sepal width in cm, petal length in cm, and petal width in cm [5]. In the article [5], Fisher developed and evaluated a linear function to differentiate between Iris species based on these four measurements [3]. 

![Image of Three Species with Petal and Sepals Labeled](Image3SpeciesTypesPetalSepal.png)   
Image Credit *Plural Sight* [6]

Fisher's Iris data set is an ideal starting point for learning data mining techniques. Data mining is digging through data to look for connections and predict trends. SAS notes data mining is a culmination of "three intertwined scientific disciplines: statistics (the numeric study of data relationships), artificial intelligence (human-like intelligence displayed by software and/or machines) and machine learning (algorithms that can learn from data to make predictions)" [7]. Machine Learning is a popular area of use as the data set is ideal for teaching beginners principles of machine learning as well as serving as an ideal test for new sorting and classifying methods. It is so commonly used that the machine learning library for Python Scikit-Learn (sk-learn) includes it as one of the loadable data sets. The data set is also freely available for download and use from UC Irvine's Machine Learning Repository [1]. UC Irvine's Machine Learning Repository enumerates the many published papers that reference this dataset showing the wide range of domains it is used in especially in the domains of computer science and statistics [1]. 

# References for Part 1: 
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

___Downloading the Dataset___
Before beginning the analysis, the data set had to be downloaded. It is available from UCI Machine Learning Repository or can be loaded in Pythopn using sk-learn. As the dataset is requested to be uploaded to the repository I downloaded the file from UCI Machine Learning Database as a .data file. These .data files hold data in either comma seperated value (.csv) format or in tab seperated value format and the data may be in text or binary format [1]. The iris.data file opened in VS Code in csv format and was in text.  

___The Programming Environment___

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

    import pandas
    import numpy 
    import matplotlib
    import seaborn
    import sklearn

Informatiom about the libraries imported and their relevance to the project:  


-pandas: Pandas is a library specifically for working with data sets. It helps with analyzing, cleaning, exploring, and manipulating data [3].   

-numpy: NumPy stands for numberical Python and is particularly useful as its `nparray` feature allows for speed in dealing with arrays. [2]  

-matplotlib: MatPlotLib is a low level graph plotting function that allows for visualisation of data in plot format. Many of the most useful functions are under the submodule `pyplot` often downloaded as `plt`  [4]
    import matplotlib.pyplot as plt  
This library is useful for making some of the simpler plots to illustrate the dataset.   

-seaborn: Seaborn library works with matplotlib and its strengths lay in visualising random distributions [5].  

-sklearn: Scikit Learn (sklearn) is a machine learning library. It is a predicitive data analysis tool built on NumPy, SciPy, and Matplotlib [6]. It also has the iris data set as one of its built-in data set options.   




## References for Part 2  

[1] AskPython.com "How to Read a .data file?"  Available: https://www.askpython.com/python/examples/read-data-files-in-python [Accessed 18 April 2021]  
[2] w3schools.com "NumPy Introduction" Available: https://www.w3schools.com/python/numpy/numpy_intro.asp [Accessed 18 April 2021].   
[3] w3schools.com "Pandas Introduction" Available: https://www.w3schools.com/python/pandas/pandas_intro.asp  [Accessed 18 April 2021].   
[4] w3schools.com "Matplotlib Introduction" Available: https://www.w3schools.com/python/matplotlib_intro.asp [Accessed 18 April 2021].   
[5] w3schools.com "Seaborn Module" Available: https://www.w3schools.com/python/numpy/numpy_random_seaborn.asp [Accessed 18 April 2021].   
[6] Scikit-learn.org "Scikit=Learn Tutorial" Available: https://scikit-learn.org/stable/tutorial/basic/tutorial.html [Accessed 18 April 2021].  