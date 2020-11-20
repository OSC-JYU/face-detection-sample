import cv2
from mtcnn import MTCNN
import os
import glob

img_dir = "hkm/"
face_dir = img_dir + "faces/"

detector = MTCNN()
files = []
for file in glob.glob(img_dir + "*.jpg"):
    files.append(os.path.basename(file))

for file in files:

    print("detecting file: " + file)
    image = cv2.cvtColor(cv2.imread(img_dir + file), cv2.COLOR_BGR2RGB)
    result = detector.detect_faces(image)

    count = 0

    for i in result:
        count = count + 1
        bounding_box = i['box']
        keypoints = i['keypoints']

        x=bounding_box[0]
        y=bounding_box[1]

        h=bounding_box[3]
        w=bounding_box[2]
        crop = image[y:y+h, x:x+w]
        cv2.imwrite(face_dir + str(count) + "_" + file + ".jpg", cv2.cvtColor(crop, cv2.COLOR_RGB2BGR))
