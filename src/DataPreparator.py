'''
Created on Mar 15, 2014

@author: The Queen
'''
from __future__ import division
from Util import TOTAL_CLASS_LABEL

def retrieve_rows(csv_file, data_reader, headers):
    
    classes = []
    size = 0
    rows = []
    
    for row in data_reader:
        # determine classes
        cls = row[len(row) - 1]
        if classes.count(cls) == 0:
            classes.append(cls)
        size += 1
        rows.append(row)
         
    return [size, rows, classes]



def create_structure(rows, classes, headers):
    class_percentages = {}

    # find count of each attribute in each class
    for row in rows:
        # count the number of uses of each classes
        cls = row[len(row) - 1]
        if class_percentages.has_key(cls) == False:
            class_percentages.update({cls: {TOTAL_CLASS_LABEL : 0}})
            
        class_count = class_percentages[cls][TOTAL_CLASS_LABEL] + 1
        class_percentages[cls].update({TOTAL_CLASS_LABEL: class_count})
        
        # count each attribute in each class
        for ind, header in enumerate(headers):

            if class_percentages[cls].has_key(header) == False:
                class_percentages[cls].update({header:{}})
            if class_percentages[cls][header].has_key(row[ind]) == False:
                class_percentages[cls][header].update({row[ind]: 0})
            
            attr_count = class_percentages[cls][header][row[ind]] + 1
            class_percentages[cls][header].update({row[ind]: attr_count})
            
    return class_percentages








