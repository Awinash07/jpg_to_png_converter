import sys
import os
from PIL import Image
#grab first and second arguments

images_folder = sys.argv[1]
output_folder = sys.argv[2]

#check is new/exists,if not create
if not os.path.exists(output_folder):
    
    #os.makedirs(output_folder)
    os.makedirs(output_folder)



#loop through images
for filename in os.listdir(images_folder):
    img = Image.open(f"{images_folder}{filename}")
    clean_name = os.path.splitext(filename)[0]
   # print(clean_name)
    img.save(f"{output_folder}{clean_name}.png","png")
    print("all done!")
#convert images to png
#save to the new folder