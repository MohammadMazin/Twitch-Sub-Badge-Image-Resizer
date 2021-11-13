print("Loading...")

import cv2
import os

count = 1
path =os.getcwd()
length = len(path)
os.system('cls')

print("All the images present inside the current folder will be reisized")
print("The Sizes are 128x128\t72x72\t36x36\t18x18")
print("----------------------------------------------------------")
print()
print("Images Found (.jpg and .png): ")

for root, directories, file in os.walk(path):
    for file in file:
        if(file.endswith(".jpg") or file.endswith(".png")):
            paths = os.path.join(root,file)
            print(count, ": " , paths[length+1:])
            count=count+1

print("----------------------------------------------------------")
print()
input("Press Enter to Continue...")

try:
    for root, directories, file in os.walk(path):
        for file in file:
            if(file.endswith(".jpg") or file.endswith(".png")):
                paths = os.path.join(root,file)
                img = cv2.imread(paths[length+1:],cv2.IMREAD_UNCHANGED)
                
                im128 = cv2.resize(img, (128,128))
                im72 = cv2.resize(img, (72,72))
                im36 = cv2.resize(img, (36,36))
                im18 = cv2.resize(img, (18,18))
                
            
                
                fileName128 = paths[length+1:(len(paths)-4)]+"_128x128.png"
                fileName72 = paths[length+1:(len(paths)-4)]+"_72x72.png"
                fileName36 = paths[length+1:(len(paths)-4)]+"_36x36.png"
                fileName18 = paths[length+1:(len(paths)-4)]+"_18x18.png"
                cv2.imwrite(fileName128, im128)
                cv2.imwrite(fileName72, im72)
                cv2.imwrite(fileName36, im36)
                cv2.imwrite(fileName18, im18)
                
    print(count-1, " Images have been resized'\n")
    input("Press Enter To Exit")
except Exception as e:
    print(e)
    


