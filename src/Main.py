'''
Created on Mar 13, 2014

@author: The Queen
'''
from __future__ import division
import csv
import re


csv_file = open('car.csv', 'r')
data_reader = csv.reader(csv_file)
headers = csv_file.next();

words = []
matched_word_count = 0
classes = []
class_percentages = {}
A_values = []
B_values = []
C_values = []
D_values = []
E_values = []
F_values = []

i=0
for row in data_reader:
    # determine classes
    cls = row[len(row) - 1]
    classes.append(cls)
    # end of finding classes
    
    if A_values.count(row[0]) == 0:
        A_values.append(row[0])
    
    for word in row:
        for item in words:
            
            if item.keys()[0] == word:
                words.remove(item)
                matched_word_count = int(item[word]) + 1
                item = {word: matched_word_count}
                words.append(item)
        if matched_word_count > 0 :
            matched_word_count = 0
        else:
            words.append({word: 1})
        i+=1

# now calculate the percentage of each class
for cls in classes:
#     if class_percentages.has_key(cls) == False:
    class_percentages.update({cls : {'percentage' : ((classes.count(cls)/len(classes))*100)} })

# remove last two: the class and '\n'
headers = headers[:len(headers) - 2]
print class_percentages
# back to beginning of the file
csv_file.seek(0)
for cls in class_percentages.keys():
    for row in data_reader:
        if row[len(row) - 1] == cls:
            
            for ind, header in enumerate(headers):
                count_attr = 1
                if class_percentages[cls].has_key(header):
#                     for index in range(len(row)-1):
#                     print str(ind) + ' ' + str(header)
                    if class_percentages[cls][header].has_key(row[ind//2]):
                        count_attr = int(class_percentages[cls][header][row[ind//2]]) + 1

#                             print class_percentages[cls][header]
                    h = {row[ind//2] : count_attr}
                    class_percentages[cls][header].update(h)
#                     count_attr = 0
#                         print class_percentages
                else:
                    class_percentages[cls].update({header: {}})
    #             print row
#                 for index in enumerate(row):
#                     print {index[1]: count_attr}
#                     class_percentages[cls].update({header: {index[1]: count_attr}})
                

# print re.findall(A_values[0], csv_file)

# print 'We have ' + str(len(classes)) + ' classes'
# print {'a':{'b':{'c':{'d':{'e':{}}}}}}
print class_percentages



