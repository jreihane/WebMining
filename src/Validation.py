'''
Created on Mar 15, 2014

@author: The Queen
'''
from __future__ import division

def corss_validation(data_reader, K, class_structure, csv_file, headers):
    dividi = class_structure['total'] // K
    print dividi
    # for each fold K
    for k in range(1,K+2):
#         csv_file.seek(0)
        
        print k
        # for each new input
        for ind, row in enumerate(data_reader):
            # for each class
            print ind , dividi, k, (k * dividi), (k * dividi + dividi)
            if k == 1:
                if ind < dividi and ind >= 1:
                    print 'TEST DATA'
                else:
                    print 'TRAIN DATA'
                    apply_alg(row, class_structure, headers)
            else:
                if ind < (k * dividi ) or ind > ((k+1) * dividi): #ind >= dividi and 
                    print 'TRAIN DATA'
                        
                else:
                    print 'TEST DATA '
#             for cls in class_structure.keys():
                
#                 if k > 1:
#                     while remain > 0:
#                         print cls

def apply_alg(row, class_structure, headers):
#     print 'aaaa'
    print headers
    for cls in class_structure:
        for header in headers:
#             print header
            if cls != 'total' and cls != 'percentage':
                print class_structure[cls][header]
            
            
            
            
            
            