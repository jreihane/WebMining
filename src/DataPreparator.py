'''
Created on Mar 15, 2014

@author: The Queen
'''
from __future__ import division
from Util import TOTAL_SIZE_LABEL, TOTAL_CLASS_LABEL, PERCENTAGE_LABEL

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
    
#     class_percentages.update({TOTAL_SIZE_LABEL: size})
     
    return [size, rows, classes]

def create_structure(rows, classes, headers):
    class_percentages = {}
    size = len(rows)
    # find classes
#     for cls in classes:
#         class_percentages.update({cls: {TOTAL_CLASS_LABEL : 0}})
# #         cls = row[len(row) - 1]
# #         print cls
#         class_count = rows.count(cls)
#         class_percentages.update({cls : {PERCENTAGE_LABEL : (class_count/size), 
#                                          TOTAL_CLASS_LABEL: class_count} })
    
    # now calculate the percentage of each class
#     for cls in classes:
#         class_percentages.update({cls : {PERCENTAGE_LABEL : (classes.count(cls)/len(classes)), 
#                                          TOTAL_CLASS_LABEL: classes.count(cls)} })
#     print class_percentages
    # find count of each attribute in each class
#     print size
    for row in rows:
        # count the number of uses of each classes
        cls = row[len(row) - 1]
        if class_percentages.has_key(cls) == False:
            class_percentages.update({cls: {TOTAL_CLASS_LABEL : 0}})
            
        class_count = class_percentages[cls][TOTAL_CLASS_LABEL] + 1
        class_percentages[cls].update({TOTAL_CLASS_LABEL: class_count})
        
        # count each attribute in each class
        for ind, header in enumerate(headers):
#             print row[ind]
            if class_percentages[cls].has_key(header) == False:
                class_percentages[cls].update({header:{}})
            if class_percentages[cls][header].has_key(row[ind]) == False:
                class_percentages[cls][header].update({row[ind]: 0})
            
            attr_count = class_percentages[cls][header][row[ind]] + 1
            class_percentages[cls][header].update({row[ind]: attr_count})
            
    
#     for row in rows:
#         for cls in classes:
# #             if class_percentages.has_key(cls) == False:
# #                 class_percentages.update({cls: {TOTAL_CLASS_LABEL : 0}})
#                 
#             if row[len(row) - 1] == cls:
# #                 classes_member_count = class_percentages[cls][TOTAL_CLASS_LABEL] + 1
# #                 class_percentages.update({cls: {TOTAL_CLASS_LABEL : classes_member_count}})
#                 
#                 for ind, header in enumerate(headers):
#                     count_attr = 1
#                     if class_percentages[cls].has_key(header):
# #                         print row[ind//2]
#                         if class_percentages[cls][header].has_key(row[ind]):
#                             count_attr = int(class_percentages[cls][header][row[ind]]) + 1
#      
#                         h = {row[ind//2] : count_attr}
#                         class_percentages[cls][header].update(h)
#                     else:
#                         class_percentages[cls].update({header: {}})
    
#     for cls in classes:
#         for 
    print class_percentages
    return class_percentages








