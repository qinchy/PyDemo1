import os
import shutil
import glob
import random

list = random.sample(range(16), 10) 
print(list)

path = os.getcwd()
print(path)

# dir(os)
# help(os)

shutil.copyfile('./PyModule1/stdlib.py', './PyModule1/stdlib2.py')

glob.glob('*.py')