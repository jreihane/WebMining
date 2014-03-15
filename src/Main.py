'''
Created on Mar 13, 2014

@author: The Queen
'''
from __future__ import division
import csv
from DataPreparator import create_structure
from Validation import corss_validation

# read file
csv_file = open('car.csv', 'r')
data_reader = csv.reader(csv_file)
headers = csv_file.next();
# remove last two: the class and '\n'
headers = headers.split(',')
headers = headers[:len(headers) - 1]

class_percentages = create_structure(csv_file, data_reader, headers)
print class_percentages

csv_file.seek(0)
corss_validation(data_reader, 10, class_percentages, csv_file, headers)
# print 'We have ' + str(len(classes)) + ' classes'


'''
last test result
{'acc': {'A': {'high': 108, 'med': 115, 'vhigh': 71, 'low': 89}, 'C': {'5more': 102, '3': 99, '2': 80, '4': 102}, 'B': {'high': 105, 'med': 114, 'vhigh': 72, 'low': 92}, 'E': {'small': 104, 'med': 135, 'big': 144}, 'D': {'4': 197, 'more': 186}, 'F': {'high': 203, 'med': 180}, 'percentage': 22.22222222222222, ',': {'low': 181, 'med': 545, 'vhigh': 143, 'big': 144, '5more': 102, 'high': 417, '3': 99, '2': 81, '4': 300, 'small': 105, 'more': 186}},
'unacc': {'A': {'high': 324, 'med': 268, 'vhigh': 359, 'low': 258}, 'C': {'5more': 292, '3': 300, '2': 325, '4': 292}, 'B': {'high': 314, 'med': 268, 'vhigh': 359, 'low': 268}, 'E': {'small': 449, 'med': 392, 'big': 368}, 'D': {'2': 575, '4': 312, 'more': 322}, 'F': {'high': 277, 'med': 357, 'low': 575}, 'percentage': 70.02314814814815, ',': {'med': 1285, '5more': 292, 'big': 368, 'vhigh': 719, '4': 604, 'high': 915, '3': 300, '2': 902, 'low': 1102, 'small': 450, 'more': 322}},
'good': {'A': {'med': 22, 'low': 46}, 'C': {'5more': 18, '3': 18, '2': 14, '4': 18}, 'B': {'med': 23, 'low': 45}, 'E': {'small': 20, 'med': 24, 'big': 24}, 'D': {'4': 35, 'more': 33}, 'F': {'high': 29, 'med': 39}, 'percentage': 3.9930555555555554, ',': {'med': 108, 'big': 24, '5more': 18, '4': 54, 'high': 30, '3': 18, '2': 15, 'low': 92, 'small': 21, 'more': 33}},
'vgood': {'A': {'med': 25, 'low': 39}, 'C': {'5more': 20, '3': 15, '2': 9, '4': 20}, 'B': {'high': 13, 'med': 25, 'low': 26}, 'E': {'big': 39, 'med': 25}, 'D': {'4': 29, 'more': 35}, 'F': {'high': 64}, 'percentage': 3.761574074074074, ',': {'high': 78, 'med': 76, '3': 15, '2': 10, '4': 50, 'low': 65, 'big': 40, '5more': 20, 'more': 35}}}

'''

