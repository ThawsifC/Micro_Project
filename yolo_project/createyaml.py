'''
This script is used to create a yaml file which is used to train a model through YOLO
'''

import yaml

#various classes mentioned which was obtained from the kaggle dataset
classes = ['Person', 'Chair', 'Toothbrush', 'Knife', 'Bottle', 'Cup', 'Spoon', 
    'Bench', 'Refrigerator', 'Fork', 'Bus', 'Toilet', 'Bicycle', 'Airplane', 
    'Truck', 'Motorcycles', 'Oven', 'Dog', 'Bed', 'Cat', 'Traffic Light', 
    'Currency', 'Face', 'Stop Sign', 'Car', 'Barriers', 'Path Holes', 
    'Stairs', 'Train', 'Bin', 'Blind Stick', 'Men Sign', 'Cell Phone', 
    'Women Sign', 'Tap']

#yaml file setup involves path, train, val, nc(number of classes), and names of classes. Train and Val can be a single folder but we decided to use lists because the dataset was organized that way
#the path can be checked through this folder
data_yaml_content = {
    'path': './main images',
    'train': ["Batch 1/images/train",
              "Batch 2/images/train",
              "Batch 3/images/train",
              "Batch 4/images/train"],
    'val': ["Batch 1/images/val",
            "Batch 2/images/val",
            "Batch 3/images/val",
            "Batch 4/images/val"],
    'nc': len(classes),
    'names': classes }

#opens the data.yaml file or creates it if not present as write mode and stores it as variable f 
with open('data.yaml', 'w') as f:
    yaml.dump(data_yaml_content, f, sort_keys=False) #command to create yaml file and write on it; not sorted so that the content of the file is arranged in the exact setup as shown above
