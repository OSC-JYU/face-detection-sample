#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
from mtcnn import MTCNN
import os
import glob

img_dir = "hkm/"
results_dir = img_dir + "results/"

detector = MTCNN()

files = []
for file in glob.glob(img_dir + "*.jpg"):
    files.append(os.path.basename(file))

for file in files:
    print("detecting files: " + file)
    image = cv2.cvtColor(cv2.imread(img_dir + file), cv2.COLOR_BGR2RGB)
    result = detector.detect_faces(image)

    for i in result:
    # Result is an array with all the bounding boxes detected. We know that for 'ivan.jpg' there is only one.
        bounding_box = i['box']
        keypoints = i['keypoints']

        cv2.rectangle(image,
                      (bounding_box[0], bounding_box[1]),
                      (bounding_box[0]+bounding_box[2], bounding_box[1] + bounding_box[3]),
                      (0,155,255),
                      2)

        cv2.circle(image,(keypoints['left_eye']), 2, (0,155,255), 2)
        cv2.circle(image,(keypoints['right_eye']), 2, (0,155,255), 2)
        cv2.circle(image,(keypoints['nose']), 2, (0,155,255), 2)
        cv2.circle(image,(keypoints['mouth_left']), 2, (0,155,255), 2)
        cv2.circle(image,(keypoints['mouth_right']), 2, (0,155,255), 2)

    cv2.imwrite(results_dir + file + "_drawn.jpg", cv2.cvtColor(image, cv2.COLOR_RGB2BGR))

    print("faces found: " + str(len(result)))
