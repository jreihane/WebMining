'''
Created on Mar 13, 2014

@author: The Queen
'''
import csv
import re


csv_file = open('car.csv', 'r')
data_reader = csv.reader(csv_file)
words = []
matched_word_count = 0

i=0
for row in data_reader:
    for word in row:
        for item in words:
            
            if item.keys()[0] == word:
#                 print item.keys()[0] + '  ' + word
                words.remove(item)
                matched_word_count = int(item[word]) + 1
                item = {word: matched_word_count}
                words.append(item)
#                 print 'OK'
#             else:
#                 words.append({word: 1})
#         print matched_word_count
        if matched_word_count > 0 :
            matched_word_count = 0
#             continue
#             matched_word_count += 1
#             print '666' + str(word)
#             count = word[word]
#             count+=1
#             words[word] = {word: matched_word_count}
        else:
#             words.append(word)
            words.append({word: 1})
#         print 'ddfg' + str(words[i])
        i+=1
# for word in words:
#     matched_words = re.findall(word, data_reader., re.IGNORECASE)

print words