# Day Ahead Electricity Price Prediction
This project is the final project following the Data Science track at Flatiron School.

#### -- Project Status: [Completed]

## Project Intro/Objective
The purpose of this project was to predict the price of electricity in the day head markets, 24 hours in advance.

Effectively predicting the price of electricity has many useful applications: 
 * It can be used to optimize electricity storage.
 * It enables demand side flexibility of buildings, allowing them to reduce consumption in expensive times
   (and potentially increase during cheap/negative price periods) and earn additional revenue from otherwise sunk costs.
 * The correlation between electricity price and carbon intensity of generation means that acting on price changes also leads
   to carbon savings.
   

### Methods Used
* Inferential Statistics
* Machine Learning (Random Forests, XGBoost, ARIMA)
* Deep Learning (Neural Networks)
* Data Visualization
* Data Cleaning and Wrangling
* Predictive Modeling

### Technologies
* Python
* Pandas, Numpy, jupyter
* Google Collab, Google Cloud
* Keras, Tensorflow
* Scikit Learn
* Time-Series Analysis

## Project Description

The project began with the need to collect electricity price data. Hourly electricity prices were collected from Nordpool, 
who run several European electricity markets. The years collected were 2013- 2019, with 2018 used as a validation set, and 
2019 the test set.

A naive method was used as a baseline, in which the price in 24 hours was predicted to be the price now.

Hourly Temperature Data was collected using the DarkSky API in 61,000 requests. 

Daily commodity price data was collected for various inputs in the production of electricity, namely:

 * Coal
 * Natural Gas
 * Uranium
 * Oil

These extra variables all effect the price of electricity and so have predictive power.

Being time series analysis, time was spent reshaping the data depending on each different models requirement, namely the
regression trees and neural networks.

Neural networks were run on google collab due to increased spead thanks to the inbuild TPU. The results (predictions) were
downloaded as CSV for analysis within jupyter notebooks.

This led to models that from any hour, intook 168 hours of the past (1 week) as inputs of all the variables, and outputted
a 24 hour prediction.

The measure of accuracy used was MAPE. This was used because it is generally easy to interpret as the average error rate,
and is useful as a percentage for interperability. However some 0 values meant extra work had to go into calculating it,
and meant it was not always the best measure of model accuracy.



## Needs of this project

- data exploration/descriptive statistics
- data processing/cleaning
- statistical modeling
- predictive modelling
- non-technical presentation

## Getting Started

1. Clone this repo (for help see this [tutorial](https://help.github.com/articles/cloning-a-repository/)).
2. Raw Data is being kept [here](https://github.com/Carterbouley/ElectricityPricePrediction/tree/master/data) within this repo.
    
3. Data processing/transformation scripts are being kept [here](https://github.com/Carterbouley/ElectricityPricePrediction/blob/master/functions.py)


## Featured Notebooks/Analysis/Deliverables

| Name                   | Description |
| :---                    | --- |
| project_name            | A name for your project. Used mostly within documentation | 
| Initial_eda.ipynb       | Early data wrangling, exploration and simple analysis | 
| functions.py            | Refactored functions that are reused throughout the notebooks|
| data                    | Folder containing csvs of data collected |
| model_result            | Results of nerual network predictions | 
| weather_file.csv        | Result from DarkSky API call| 
| re_fixed...series.csv   | Single and multivariate cleaned time series .csv | 
| Battery                 | Simple model of tesla battery based on best predictive model | 
| ARIMA & XGBoost.ipynb   | ARIMA & XGBoost models | 
| naive_methods.ipynb     | Baseline model | 
| multivariate_LSTM_ele...| Google collab neural network upload| 
| Electricity Pr ... .pdf | Non-technical presentation | 
| ResultAnalysis.ipynb    | Neural network result analysis|



## Contact Me
* If you want to contact me, [you can do that here](https://www.linkedin.com/in/carter-b-159ab6a1/).  
* Or at carterbouley@gmail.com.
* Feel free to contact team leads with any questions or if you are interested in contributing!
