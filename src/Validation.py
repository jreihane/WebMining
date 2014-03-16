'''
Created on Mar 15, 2014

@author: The Queen
'''
from __future__ import division
from NaiveClassifier import train, test_net, calc_precision_recall

def corss_validation(rows, size, classes, K, csv_file, headers):
    # find the size that test data should have
    dividi = size // K

    # for each fold K
    for k in range(1,K+1):
        # divide data into two parts: one part is used for training the classifier and other part is used
        # for testing the classifier
        if k == 1:
            test_data = rows[0:dividi]
            train_data = rows[dividi + 1:]

        else:
            test_data = rows[k * dividi: ((k+1) * dividi)]
            
            # data before test data and after it
            train_data = rows[0:(k * dividi)] + rows[((k+1) * dividi) + 1:]
        
        probs = train(train_data, classes, headers)
        test_data = test_net(test_data, classes, headers, probs)
        
        test_precision = calc_precision_recall(test_data, probs)
        
        print '***************************** FINAL RESULTS in k = ' + str(k) + ' *****************************************************************'
        print 'Precision: ' + str(test_precision[0]) + '\t Recall: ' + str(test_precision[1])
        print '**********************************************************************************************************************\n\n'

            
            
            