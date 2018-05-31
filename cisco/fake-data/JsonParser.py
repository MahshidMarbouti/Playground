
import operator
import json
import os
import pygtrie as trie


class file_reader(): 
    def __init__(self, filename):
        self.filename = filename

    def parse_file(self):
        os.chdir("/Users/Mahshid/Playground/cisco/fake-data")
        result = []
        for line in open(self.filename, 'r'):
            result.append(json.loads(line))
        return result


class path_extractor(): 
    def __init__(self, json_elements):
        self.json_elements = json_elements    
        self.dictionary = {}  

    def find_path_field(self):
        for line in self.json_elements:
            path=line["ph"]
            if path[1]  not in  self.dictionary.keys():
                    self.dictionary[path]= 1
            else:
                self.dictionary[path]+=1
        return self.dictionary

    def find_most_k_frequent_path(self, k):
        sorted_dictionary = sorted(self.dictionary.items(), key=operator.itemgetter(1))
        for i in range(k):
            print(sorted_dictionary[i])  
