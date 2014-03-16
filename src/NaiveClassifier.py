'''
Created on Mar 16, 2014

@author: The Queen
'''
from Util import TOTAL_SIZE_LABEL, PERCENTAGE_LABEL
from DataPreparator import create_structure

def train(train_data, classes, headers):
#     for cls in class_structure:
#         for header in headers:
# #             print header
#             if cls != TOTAL_SIZE_LABEL and cls != PERCENTAGE_LABEL:
#                 print class_structure[cls][header]
            
    create_structure(train_data, classes, headers) 