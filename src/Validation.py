'''
Created on Mar 15, 2014

@author: The Queen
'''
from __future__ import division
from Util import TOTAL_SIZE_LABEL
from NaiveClassifier import train, test_net, calc_precision_recall

def corss_validation(rows, size, classes, K, csv_file, headers):
    dividi = size // K #rows[TOTAL_SIZE_LABEL] // K
    print dividi
    
    
    # for each fold K
    for k in range(1,2):
#         csv_file.seek(0)
#         
#         print k
#         # for each new input
#         for ind, row in enumerate(data_reader):
#             # for each class
#             print ind , dividi, k, (k * dividi), (k * dividi + dividi)
#             if k == 1:
#                 if ind < dividi and ind >= 1:
#                     print 'TEST DATA'
#                 else:
#                     print 'TRAIN DATA'
#                     apply_alg(row, class_structure, headers)
#             else:
#                 if ind < (k * dividi ) or ind > ((k+1) * dividi): #ind >= dividi and 
#                     print 'TRAIN DATA'
#                         
#                 else:
#                     print 'TEST DATA '

        # divide data into two parts: one part is used for training the classifier and other part is used
        # for testing the classifier
        if k == 1:
            test_data = rows[1:dividi]
            train_data = rows[dividi:]
#             print 'len test:'
#             print len(test_data)
#             print 'len train:'
#             print len(train_data)
        else:
            test_data = rows[k * dividi: ((k+1) * dividi)]
            # data before test data and after it
            train_data = rows[1:(k * dividi)] + rows[((k+1) * dividi):]
        
        probs = train(train_data, classes, headers)
        test_data = test_net(test_data, classes, headers, probs)
        print test_data
        
        test_precision = calc_precision_recall(test_data, probs)
        print test_precision
#         print '-------------------------------------------'
#         print 'test data: '
#         print test_data
#         print 'train data: '
#         print train_data
    


            
            
            