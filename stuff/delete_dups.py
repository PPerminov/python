import hashlib
import os
from glob import glob


fArray = [y for x in os.walk('/home/user100/learning_to_fly/') for y in glob(os.path.join(x[0], '*'))]

# print(fArray)


for filepath in fArray:
    if os.path.isfile(filepath):
        with open(filepath, 'r') as file:
            try:
                fs = file.read().encode('UTF')
            except UnicodeDecodeError:
                print(filepath)
            # hashlib.sha256(file.read()).hexdigest()
            # hash.update(file.read())
            # print(hash.digest)/
