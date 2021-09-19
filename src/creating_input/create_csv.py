import csv
from glob import glob
import os

bg_paths = glob('/Users/sunita/Documents/Nvidia-Hackathon-Dataset/training/background/*')
hi_paths = glob('/Users/sunita/Documents/Nvidia-Hackathon-Dataset/training/hi/*')
test_paths = glob('/Users/sunita/Documents/Nvidia-Hackathon-Dataset/test/*')

print(len(bg_paths))
print(len(hi_paths))

with open('/Users/sunita/Documents/Nvidia-Hackathon-Dataset/input/train.csv', 'w') as f:
    headrow = ('Image_path', 'label')
    csvwriter = csv.writer(f)

    csvwriter.writerow(headrow)

    for bg_path in bg_paths:
        csvwriter.writerow((bg_path,'0'))

    for hi_path in hi_paths:
        csvwriter.writerow((hi_path,'1'))

    # for test_path in test_paths:
    #     csvwriter.writerow((test_path,'-1'))


