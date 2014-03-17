'''
Created on Mar 16, 2014

@author: The Queen
'''
from __future__ import division
from Util import TOTAL_CLASS_LABEL, CLASS_PROBABILITY
from DataPreparator import create_structure

'''
 Naive Bayesian algorithm for training data
'''
def train(train_data, classes, headers):
    probabilities= {}
#     print len(train_data)
    class_percentages = create_structure(train_data, classes, headers)
    
    for cls in classes:
        probabilities.update({cls: {}})
        if class_percentages.has_key(cls):
            cls_dic = class_percentages[cls]
            
            # compute p(class)
            cls_prob = cls_dic[TOTAL_CLASS_LABEL] / len(train_data)
            probabilities[cls].update({CLASS_PROBABILITY: cls_prob, TOTAL_CLASS_LABEL: cls_dic[TOTAL_CLASS_LABEL]})
    #         print 'probability of ' + cls + ' is: ' + str(cls_prob)
            
            for header in headers:
#                 print cls_dic[TOTAL_CLASS_LABEL]
                attrs = cls_dic[header]
                for attr in attrs:
#                     print cls, header, attr, attrs[attr]
                    name = header + '_' + attr
                    # compute p(X|class)
                    # * 100 because of float multiplications can cause problem!
                    probabilities[cls].update({name: (attrs[attr] / cls_dic[TOTAL_CLASS_LABEL] * 100)})# * pow(10,0)
        
            
#     print probabilities
    return probabilities

'''
 Test new data
'''
def test_net(test_data, classes, headers, probabilities):
    test_probabilities = {}
    
#     print fl_info
    for row in test_data:
        prob_value = 1
        for cls in probabilities.keys():
#             print '----------------------------------------------------------'
            if cls != CLASS_PROBABILITY:
                for index, header in enumerate(headers):
                    name = header + '_' + row[index]
#                     print row[index] , name
                    if probabilities[cls].has_key(name):
#                         print cls + ' has ' + name
                        prob_value = probabilities[cls][name] * (prob_value)
                        
#                         prob_value /= 100
                    else:
#                         print cls + ' does not have ' + name
                        prob_value *= pow(10, -15)
#                 prob_value /= 100
                # compute p(X|class)*p(class) = p(class|X)
                if probabilities[cls].has_key(CLASS_PROBABILITY):
#                     print cls, prob_value, probabilities[cls][CLASS_PROBABILITY]
                    prob_value *= probabilities[cls][CLASS_PROBABILITY]
                    test_probabilities.update({cls: prob_value})
                
#         print '----------------------------------------------------------------------'
#         print test_probabilities
#         print '----------------------------------------------------------------------'
        # maximum value of classes is selected as train data class
        max_v = find_max(test_probabilities)
        row.append(max_v)
    
    return test_data


def calc_precision_recall(test_data, classes):
    test_precision = 1
    test_recall = {}
    true_positive = {}
    true_positive_class = {}
    false_positive_class = {}
    true_negative_class = {}
    false_negative_class = {}
    
    correct_values = 0
    incorrect_values = 0
    
    for cls in classes:
        true_negative_class.update({cls: 0})
        false_negative_class.update({cls: 0})
    
    for row in test_data:
        real = row[len(row) - 2]
        estimated = row[len(row) - 1]
        
        if true_positive.has_key(real) == False:
            true_positive.update({real: 1})
        else:
            true_positive_count = true_positive[real] + 1
            true_positive[real] = true_positive_count
        
#         print real, estimated
        if real == estimated:
            correct_values += 1
            if true_positive_class.has_key(real):
                true_positive_class[real] = true_positive_class[real] + 1
                for cls in classes:
                    if cls != real:
                        true_negative_class.update({cls: true_negative_class[cls] + 1})
            else:
                true_positive_class.update({real: 1})
                true_negative_class.update({cls: true_negative_class[cls] + 1})
        else:
            incorrect_values += 1
            if false_positive_class.has_key(estimated):
                false_positive_class[estimated] = false_positive_class[estimated] + 1
            else:
                false_positive_class.update({estimated: 1})
            
            if false_positive_class.has_key(real):
                false_negative_class[real] = false_negative_class[real] + 1
            else:
                 false_negative_class.update({cls: false_negative_class[cls] + 1})
    
    
    
    for cls in true_positive.keys():
#         print '""""""""""""""""""""""""""""""""'
#         print cls, true_positive[cls]#, true_positive_class[cls]
#         print '""""""""""""""""""""""""""""""""'
        if true_positive_class.has_key(cls):
            test_recall_count = true_positive_class[cls] / true_positive[cls]
#             print 'True positives are:',true_positive_class[cls], ' from total: ', true_positive[cls], ' of class: ', cls
        else:
            test_recall_count = 0
#             print 'True positives are: 0 from total: ', true_positive[cls], ' of class: ', cls
            
#         if false_positive_class.has_key(cls):
#             print 'False positives are: ', false_positive_class[cls], ' for class: ', cls
#         else:
#             print 'Class: ', cls, ' does not have any false positive value!'
    
        test_recall.update({cls: test_recall_count})
#     print 'True positive are', true_positive_class
#     print 'True negatives are', true_negative_class
    print 'False positives are: ', false_positive_class
    print 'False negatives are: ', false_negative_class
#     print '\n'
    if len(test_data) > 0:
        test_precision = correct_values / len(test_data)
    
    return [test_precision, test_recall]


def find_max(probs):
    max_val = 0
    estimated_class = ''
    
    for cls in probs:
        if probs[cls] > max_val:
            max_val = probs[cls]
            estimated_class = cls
    
    return estimated_class
    
