from PIL import Image
import numpy as np  
import random
import cv2
from colorama import Fore



class BlurImage:
    

    def __init__(self):
        self._probability = 0.5
        self.width = width
        self.height = height

    def probs(self):
        return self._probability

    def operate(self, augimage, idx):
        """
        Blurs a given image. Randomly decides how to blur. 
        Check cv2 docs for cv2.blur()
        """
        random_vars = {
            "0" : "Gaussian Blur",
            "1" : "Median Blur"
        }
        min_k = min(height,width)
        rand_blur = random.randint(0, 3)
        kernel_size = random.randint(1,min_k)

        if augimage.format == "array":
            if rand_blur==0:
                img = cv2.blur(augimage.img, (kernel_size,kernel_size))
            elif rand_blur==1:

                if kernel_size%2 == 0:
                    if (kernel_size - 1)<1:
                        kernel_size +=1
                    else:
                        kernel_size -= 1
                else:
                    pass

                img = cv2.GaussianBlur(augimage.img, (kernel_size,kernel_size),0)
            
            elif rand_blur==2:

                img = cv2.medianBlur(augimage.image, kernel_size)

            elif rand_blur==3:

                topLeft = (random.randint(0,height), random.randint(0,width))
                bottomRight = (random.randint(0,height), random.randint(0,width))

                x, y = topLeft[0], topLeft[1]
                w, h = bottomRight[0] - topLeft[0], bottomRight[1] - topLeft[1]
                
                # Grab ROI with Numpy slicing and blur
                ROI = augimage.image[y:y+h, x:x+w]
                blur = cv2.GaussianBlur(ROI, (5,5), 0) 

                # Insert ROI back into image
                augmimage.image[y:y+h, x:x+w] = blur
            if augimage.groundTruth is not None:
                pass


        else:
            try:
                #checking image type just incase
                if isinstance(augimage.img, Image.Image):
                    img = augimage.img.filter(ImageFilter.BLUR)
                    
                    if augimage.groundTruth is not None:
                        pass                        
                else:
                    raise TypeError
            except Exception as e:
                print(Fore.RED+"Error:"+Fore.RESET, end="")
                print(e)
                exit()

        name, ext = augimage.name.split(".")
        path = augimage.targPath+"/"+name+"_"+str(idx)+"."+ext
        cv2.imwrite(path, img)

        if augimage.groundTruth is not None:
            name, ext = augimage.truthName.split(".")
            truthpath = augimage.targTruthPath+"/"+name+"_"+str(idx)+"."+ext
            cv2.imwrite(truthpath, groundTruth)