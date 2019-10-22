from submask import *
from submaskann import *
import json
import os 


data_path = './images/'
file_list = os.listdir(data_path)
n_data = len(file_list)
mask_images = []
for image in range(n_data): 
    mask_images.append(Image.open(data_path+file_list[image]))



# Define which colors match which categories in the images
body_id, upper_id, lower_id = [1, 2, 3]
category_ids = {}
for image in range(n_data):
    category_ids[image+1] = {
        '(255, 255, 0)': body_id,
        '(255, 0, 0)': upper_id,
        '(0, 0, 255)': lower_id
    }

is_crowd = 0

# These ids will be automatically increased as we go
annotation_id = 1
image_id = 1

# Create the annotations
cocoanns = {}
annotations = []
images = []

for img in range(n_data):
    images.append({'file_name': file_list[img],'width':1920,'height':1080,'id':img})
for mask_image in mask_images:
    sub_masks = create_sub_masks(mask_image)
    for color, sub_mask in sub_masks.items():
        category_id = category_ids[image_id][color]
        annotation = create_sub_mask_annotation(sub_mask, image_id, category_id, annotation_id, is_crowd)
        annotations.append(annotation)
        annotation_id += 1
    image_id += 1


cocoanns['annotations'] = annotations
cocoanns['categories']=[{'supercategory':'bipolar','id':1,'name':'body'}
                        ,{'supercategory':'bipolar','id':2,'name':'upper'}
                        ,{'supercategory':'bipolar','id':3,'name':'lower'}]
cocoanns['images'] = images


with open('ann_1021.json', 'w') as json_file:
    json.dump(cocoanns, json_file) 




 