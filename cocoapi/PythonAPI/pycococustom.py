
from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab
import os

pylab.rcParams['figure.figsize'] = (8.0, 10.0)


dataDir='../bipolar_data'
dataType='robot_bipolar'
annFile='{}/annotations/instances_{}.json'.format(dataDir,dataType)


# initialize COCO api for instance annotations
coco=COCO(annFile)

# display COCO categories and supercategories
cats = coco.loadCats(coco.getCatIds())
#[{'supercategory':'bipolar','id':1, 'name':'body'},{'supercategory':'bipolar','id':2, 'name':'upper'},{'supercategory':'bipolar','id':3, 'name':'lower'}]

nms=[cat['name'] for cat in cats]
print('COCO categories: \n{}\n'.format(' '.join(nms)))

nms = set([cat['supercategory'] for cat in cats])
print('COCO supercategories: \n{}'.format(' '.join(nms)))

# get all images containing given categories, select one at random

catIds = coco.getCatIds(catNms=['body','upper','lower']);
imgIds = coco.getImgIds(catIds=catIds );
imgIds = coco.getImgIds(imgIds = [10])
img = coco.loadImgs(imgIds[np.random.randint(0,len(imgIds))])[0]

# load and display image

I = io.imread(dataDir +'/'+ img['file_name'] ) 
plt.axis('off');plt.imshow(I); plt.show() 

# load and display instance annotations
plt.imshow(I) ; plt.axis('off')

annIds = coco.getAnnIds(imgIds=img['id'], catIds=catIds, iscrowd=None)
anns = coco.loadAnns(annIds)
draw_bbox = True
coco.showAnns(anns,draw_bbox)
plt.savefig('../segmented_images/'+str(imgIds[0])+'.png')
plt.show()