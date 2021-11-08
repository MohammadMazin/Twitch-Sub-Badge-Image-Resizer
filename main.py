import cv2
import os

count = 1
path =os.getcwd()
length = len(path)

print("All the images present inside the current folder will be reisized")
print("The Sizes are 128x128\t72x72\t32x32\t18x18")
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
name = input("Enter title of Image: ")

for root, directories, file in os.walk(path):
    for file in file:
        if(file.endswith(".jpg") or file.endswith(".png")):
            paths = os.path.join(root,file)
            img = cv2.imread(paths[length+1:])
            
            im128 = cv2.resize(img, (128,128))
            im72 = cv2.resize(img, (72,72))
            im32 = cv2.resize(img, (32,32))
            im18 = cv2.resize(img, (18,18))
            
            fileName128 = name+"_128x128.png"
            fileName72 = name+"_72x72.png"
            fileName32 = name+"_32x32.png"
            fileName18 = name+"_18x18.png"
            cv2.imwrite(fileName128, im128)
            cv2.imwrite(fileName72, im72)
            cv2.imwrite(fileName32, im32)
            cv2.imwrite(fileName18, im18)