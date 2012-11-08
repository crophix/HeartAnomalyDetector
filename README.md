Copyright (c) 2012 Daniel Leblanc

HeartAnomalyDetector
====================

Assignment 3 for CS 441 AI.  Machine learning algorithm to analyze some sample heart data and find abnormalities.

Approach:
This program will be using a Naive Bayesian approach to analyzing a binary set heart data.  Data is read from a comma delimited file with each line represented a separate case.  Training cases are seperate from test cases.  The training cases will be read in line by line and used to set probabilities for the program to use when analyzing the test cases.