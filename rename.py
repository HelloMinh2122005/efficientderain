import os

path = '/data/uittogether2/GEN-dataset/tmp/efficientderain/ground_truth'
index = 0
name = 'gt_img_'

for filename in os.listdir(path):
    index += 1
    os.rename(os.path.join(path, filename), os.path.join(path, name + str(index) + '.jpg'))