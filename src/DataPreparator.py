'''
Created on Mar 15, 2014

@author: The Queen
'''
def create_structure(csv_file, data_reader, headers):
    
    classes = []
    class_percentages = {}
    size = 0
    
    for row in data_reader:
        # determine classes
        cls = row[len(row) - 1]
        classes.append(cls)
        size += 1
        # end of finding classes
    
    class_percentages.update({'total': size})
    
    # now calculate the percentage of each class
    for cls in classes:
        class_percentages.update({cls : {'percentage' : (classes.count(cls)/len(classes)), 
                                         'total_count': classes.count(cls)} })
    
    
    # back to beginning of the file
    csv_file.seek(0)
    
    # find count of each attribute in each class
    for row in data_reader:
        for cls in class_percentages.keys():
            if row[len(row) - 1] == cls:
                
                for ind, header in enumerate(headers):
                    count_attr = 1
                    if class_percentages[cls].has_key(header):
                        if class_percentages[cls][header].has_key(row[ind//2]):
                            count_attr = int(class_percentages[cls][header][row[ind//2]]) + 1
    
                        h = {row[ind//2] : count_attr}
                        class_percentages[cls][header].update(h)
                    else:
                        class_percentages[cls].update({header: {}})
    
    return class_percentages