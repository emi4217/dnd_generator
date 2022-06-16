import random
import os
import pyperclip

def random_lines():
    path = os.path.dirname(os.path.realpath(__file__));
    path = os.path.join(path, ("tables"))
    directories_list = os.listdir(path)
    for filename in directories_list:
        random_line = [ line for line in open(os.path.join(path, filename), encoding="utf8")]
        s1 = random.choice(random_line)
        pyperclip.copy(s1)
        s2 = pyperclip.paste()
        print(s2)



random_lines()