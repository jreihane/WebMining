'''
Created on Mar 13, 2014

@author: The Queen
'''
from __future__ import division
import csv
from DataPreparator import retrieve_rows
from Validation import cross_validation
'''
1) get an array of rows
2) for 10 times (10-fold) break the row array into two parts: 172 items for testing and the rest for training
3) for the train data compute the probability of p(row|class)*p(class)
4) for every test data calculate p(X|class)
5) save the maximum value of that probability for each class
6) compare estimated class with the actual class mentioned at the end of row
7) calculate precision and recall
'''

# read file
csv_file = open('car.csv', 'r')
data_reader = csv.reader(csv_file)
headers = csv_file.next();

# remove last element: the class label
headers = headers.split(',')
headers = headers[:len(headers) - 1]

strctured_value = retrieve_rows(csv_file, data_reader, headers)

csv_file.seek(0)
cross_validation(strctured_value[1], strctured_value[0], strctured_value[2], 10, csv_file, headers)


