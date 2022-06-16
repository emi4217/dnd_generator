import random
import os
import pyperclip
import csv

def random_lines():
    path = os.path.dirname(os.path.realpath(__file__));
    path = os.path.join(path, ("tables"))
    directories_list = os.listdir(path)
    result = []
    
    #iterate through files to generate random lines 
    for filename in directories_list:
        f = open(filename)
        csv_f = csv.reader(f)
        next(csv_f)
        for row in csv_f:
            random_line = [ line for line in open(os.path.join(path, filename), encoding="utf8")]
            s1 = filename + " " + random.choice(random_line)
        result.append(s1)
    
    #convert result[] to str
    result_string = ' '.join(result)

    #copy result to the clipboard   
    pyperclip.copy(result_string)
    copied_result = pyperclip.paste()
    print(copied_result)



random_lines()