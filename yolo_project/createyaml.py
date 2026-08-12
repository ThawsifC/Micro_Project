import yaml

classes = ['Person', 'Chair', 'Toothbrush', 'Knife', 'Bottle', 'Cup', 'Spoon', 
    'Bench', 'Refrigerator', 'Fork', 'Bus', 'Toilet', 'Bicycle', 'Airplane', 
    'Truck', 'Motorcycles', 'Oven', 'Dog', 'Bed', 'Cat', 'Traffic Light', 
    'Currency', 'Face', 'Stop Sign', 'Car', 'Barriers', 'Path Holes', 
    'Stairs', 'Train', 'Bin', 'Blind Stick', 'Men Sign', 'Cell Phone', 
    'Women Sign', 'Tap']

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

with open('data.yaml', 'w') as f:
    yaml.dump(data_yaml_content, f, sort_keys=False)

print("Executed")