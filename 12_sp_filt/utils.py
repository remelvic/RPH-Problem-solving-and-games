import os
 
def read_classification_from_file(classification_path):
    dic = {}
    with open(classification_path,'r', encoding="utf-8") as f:
        for line in f:
            row = line.rstrip().split(' ')
            dic[row[0]] = row[1]
    return dic
 
 
def write_classification_to_file(classification_dir, dic, classification_file):
    with open(os.path.join(classification_dir,classification_file),'w',encoding="utf-8") as f:
        for key in dic:
            f.write(key + " " + dic[key] + "\n")
