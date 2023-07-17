import os
import csv 
import re


class read_templates():
    '''
    (test)->(python dictionary)
    Class to import the template.text file, read contents and output to a single python dictionary
    disctionary key = Name of template
    dictionary values = python list of associated tops - split on ',' delimiter to putput as python list
    key and values are distinguished using a regex pattern matech
    PRECONDITIONS: template.txt is int he correct format 'KEY', ['form top1',...'form top n']
    KJAGGS NOV 2022
    '''
    def __init__(self):

        #regex to find two text sections
        #First: Name of Template-Example 'Breagh Template' REQUIRED FORMAT String with single quotes
        #Second: list of required formation tops-Example '['Bunter Sand','Bunter Shale'] REQUIRED FORMAT list of strings
        self.regexID = "^('.*'),\[(.*)]"  

        #initialise output dictionary   
        self.template_dict = {}


    def generate_templates(self, template_source):
        #reference text file - found in root directory
        #file contains pre defined list for required template
        #selected formation tops will be added to comboboxes to aid data entry speed

        #template_source = "H:\Python\iepg\Formation Top Loader\templates.txt"
        #template_root = os.path.join(os.path.dirname(__file__),  template_source)
        #rel_path = "Config"
        #full_path = os.path.join(os.path.dirname(__file__), rel_path)
        #print(template_infile)

        #read each text file line
        #print(os.path.join(os.path.dirname(__file__), 'Config', template_source))
        #with open('.\\Config\\templates.txt', "r") as ti:

        #print(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
        with open(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)), 'Config', template_source), "r") as ti:
        
            reader = ti.readlines()

            #read each text file line    
            for line in reader:

                #if regex pattern match, append data to dictionary
                if re.search(self.regexID,line):
                        match = re.search(self.regexID,line)
                        
                        self.template_dict[match[1]] = match[2].split(',')

        #return template disctionary
        #print(self.template_string)
        return self.template_dict
        

