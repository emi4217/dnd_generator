import random
import os
import pyperclip
from pandas import *

def random_lines():
    path = os.path.dirname(os.path.realpath(__file__));
    path = os.path.join(path, ("tables"))
    directories_list = os.listdir(path)
    result = []
    
    




    #iterate through files to generate random lines --->> ToChange: iterate through a list of generated possibility lists 
    for filename in directories_list:
        with open(os.path.join(path, filename), 'r', encoding='utf8') as f:
            
            lines = f.readlines()[1:]
            random_line = [ line for line in lines ]
            s1 = filename + " " + random.choice(random_line)
            result.append(s1)
            
    
    #convert result[] to str
    result_string = ' '.join(result)

    #copy result to the clipboard   
    pyperclip.copy(result_string)
    copied_result = pyperclip.paste()
    return copied_result


while True:
    input("Press Enter to continue")
    print(random_lines())