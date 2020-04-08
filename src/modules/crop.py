from PIL import Image
import numpy as np  
import random
import cv2
from colorama import Fore



class CropImage:
    

    def __init__(self, width, height):
        self.probability = 0.2
        self.width = width
        self.height = height

    def crop_array(self,arr_input):

        h,w,c = arr_input.shape
        if(self.width > w or self.height>h):
            return arr_input

        crop = arr_input[:self.height, :self.width]
        return crop
        

    def operate(self, augimage, idx):

        
        if augimage.format == "array":

            img = self.crop_array(augimage.img)
                                
            if augimage.groundTruth is not None:
                groundTruth = crop_array(augimage.groundTruth)

        else:

            try:

                if isinstance(augimage.img, Image.Image):

                    w,h = augimage.img.size
                    l_coord = random.randint(0, int((w - self.width)))
                    d_coord = random.randint(0, int((h - self.height)))
                    if self.height > h or self.width > w :
                        img=  augimage.img

                    else:
                        img =  augimage.img.crop((l_coord,d_coord,self.width+l_coord,self.height+d_coord))

                    
                    if augimage.groundTruth is not None:

                        groundTruth = augimage.groundTruth.crop((l_coord,d_coord,self.width+l_coord,self.height+d_coord))



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





