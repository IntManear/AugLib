from PIL import Image
import numpy as np  
import random
import cv2
from colorama import Fore



class ScaleImage:
    

    def __init__(self, factor):
        self.probability = 0.4
        self.factor = factor

    def scale_array(self, arr_input):

        width = int(arr_input.shape[1] * self.factor)
        height = int(arr_input.shape[0] * self.factor)

        dim = (width, height)

        changed_array = cv2.resize(arr_input, dim, interpolation = cv2.INTER_AREA)

        return changed_array


    def operate(self, augimage, idx):

        
        if augimage.format == "array":

            img = scale_array(augimage.img)
                                
            if augimage.groundTruth is not None:
                groundTruth = scale_array(augimage.groundTruth)

        else:

            try:

                if isinstance(augimage.img, Image.Image):

                    w,h = augimage.img.size
                    new_h = int(h*self.factor)
                    new_w = int(w*self.factor)

                    img = augimage.img.resize((new_w,new_h), resample = Image.BICUBIC)
                    if augimage.groundTruth is not None:
                        groundTruth = scale_array(augimage.groundTruth)



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





