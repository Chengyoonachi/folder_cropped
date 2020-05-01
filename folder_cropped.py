import cv2
import os

def picture_cropped(pic_path):
    img = cv2.imread(pic_path)
    cropped = img[400:1200,480:1440]
    return cropped
    # cv2.imwrite("C:/Users/User/Cropped/black_000054.png",cropped)


path = "C:/Users/User/Picture/train/yelllow"
files = os.listdir(path)
print(files[0])
s = []

for file in files:
    s.append(file)
    f = (path+"/"+file)
    print(f)
    cropped = picture_cropped(f)
    new_path = ("C:/Users/User/Cropped/yellow"+"/"+file)
    cv2.imwrite(new_path,cropped)







    #cv2.imwrite("C:/Users/User/Cropped/black_000054.png",cropped)
