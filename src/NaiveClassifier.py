'''
Created on Mar 16, 2014

@author: The Queen
'''
from __future__ import division
from Util import TOTAL_CLASS_LABEL, CLASS_PROBABILITY
from DataPreparator import create_structure
import sys

global fl_info
fl_info = sys.float_info


'''
 Naive Bayesian algorithm for training data
'''
def train(train_data, classes, headers):
    probabilities= {}
    
    class_percentages = create_structure(train_data, classes, headers)
    
    for cls in classes:
        probabilities.update({cls: {}})
        cls_dic = class_percentages[cls]
        
        # compute p(class)
        cls_prob = cls_dic[TOTAL_CLASS_LABEL] / len(train_data)
        probabilities[cls].update({CLASS_PROBABILITY: cls_prob, TOTAL_CLASS_LABEL: cls_dic[TOTAL_CLASS_LABEL]})
        print 'probability of ' + cls + ' is: ' + str(cls_prob)
        
        for header in headers:
            attrs = cls_dic[header]
            for attr in attrs:
                name = header + '_' + attr
                # compute p(X|class)
                # * 100 because of float multiplications can cause problem!
                probabilities[cls].update({name: (attrs[attr] / cls_dic[TOTAL_CLASS_LABEL]) * pow(10,2)})
                
            
    print probabilities
    return probabilities

'''
 Test new data
'''
def test_net(test_data, classes, headers, probabilities):
    test_probabilities = {}
    
    print fl_info
    for row in test_data:
        prob_value = 1
        for cls in probabilities.keys():
            print '----------------------------------------------------------'
            if cls != CLASS_PROBABILITY:
                for index, header in enumerate(headers):
                    name = header + '_' + row[index]
#                     print row[index] , name
                    if probabilities[cls].has_key(name):
                        prob_value *= probabilities[cls][name]
#                         print str(cls) + ' ' + name + ' ' + str(probabilities[cls][name])
                    else:
#                         if row[index] == :
                            print 'does not have ' + name
                            prob_value *= 0.1 * (pow(10, -15))
                # compute p(X|class)*p(class) = p(class|X)
                prob_value *= probabilities[cls][CLASS_PROBABILITY]
                test_probabilities.update({cls: prob_value})
                
        print '**********************************************************************'
        print test_probabilities
        print '**********************************************************************'
        # maximum value of classes is selected as train data class
        max_v = find_max(test_probabilities)
        row.append(max_v)
    
    return test_data


def calc_precision_recall(test_data, probabilities):
    test_precision = 0
    test_recall = {}
    true_positive = {}
    
    correct_values = 0
    incorrect_values = 0
    
    for row in test_data:
        real = row[len(row) - 2]
        estimated = row[len(row) - 1]
        if true_positive.has_key(real) == False:
            true_positive.update({real: 1})
        else:
            true_positive_count = true_positive[real] + 1
            true_positive[real] = true_positive_count
            
        if real == estimated:
            correct_values += 1
            
        else:
            incorrect_values += 1
             
    for cls in true_positive.keys():
        print '""""""""""""""""""""""""""""""""'
        print correct_values, true_positive[cls]
        print '""""""""""""""""""""""""""""""""'
        test_recall_count = correct_values / true_positive[cls]
        test_recall.update({cls: test_recall_count})
    
    test_precision = correct_values / len(test_data)
    
    print test_precision
    print test_recall
    return [test_precision, test_recall]


def find_max(probs):
    max_val = 0
    estimated_class = ''
    
    for cls in probs:
        if probs[cls] > max_val:
            max_val = probs[cls]
            estimated_class = cls
    
    return estimated_class
    
