from PIL import Image
import numpy as np  
import random
import cv2
from colorama import Fore

class FlipImage:
    
    """
    Module is used to flip image. Modules are not accessed directly
    by default. Although, the user can do so if its requried.

    Parameters: 
        -> probability: probability that this file gets called during the
                        automated process.

    Functions: 
        -> operate(self, obj): The AugImage type object that needs to be 
                                operated on. Saves it also.
                                                 
    """

    def __init__(self):
        self._probability = 0.8

    def probs(self):
        return self._probability

    def operate(self, augimage, idx):
        """
        Flips a given image. Randomly decides how to flip. 
        Check cv2 docs for cv2.flip()
        """
        random_vars = {
            "0" : "Image.FLIP_TOP_BOTTOM",
            "1" : "Image.FLIP_LEFT_RIGHT"
        }

        rand_axis = random.randint(0, 1)

        if augimage.format == "array":
            img = cv2.flip(augimage.img, rand_axis)         
            if augimage.groundTruth is not None:
                groundTruth = cv2.flip(augimage.groundTruth, rand_axis)


        else:
            try:
                #checking image type just incase
                if isinstance(augimage.img, Image.Image):
                    img = augimage.img.transpose(random_vars[str(rand_axis)])
                    img = np.asarray(img)
                    img = img[:,:,::-1]
                    if augimage.groundTruth is not None:
                        groundTruth = augimage.groundTruth.transpose(random_vars[str(rand_axis)])
                        groundTruth = np.asarray(groundTruth)
                        groundTruth = groundTruth[:,:,::-1]                        
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



                
