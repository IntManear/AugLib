from PIL import Image
import cv2
import imutils
import math
import random
from colorama import Fore



class RotateImage:
    def __init__(self):
        self.probability = 0.8
       
    def probs(self):
        return self._probability


    def operate(self,augimage, idx):
        angle = random.randint(0, 20)
      
        if augimage.format == "array":
            return None #currently only supports PIl format
            x = augimage.img.shape[1]
            y = augimage.img.shape[0]
            rotation = 45
            image = imutils.rotate_bound(augimage.img,angle)
            X = image.shape[1]
            Y = image.shape[0]
            angle_a = abs(rotation)
            angle_b = 90 - angle_a
            angle_a_rad = math.radians(angle_a)
            angle_b_rad = math.radians(angle_b)
            angle_a_sin = math.sin(angle_a_rad)
            angle_b_sin = math.sin(angle_b_rad)
            E = (math.sin(angle_a_rad)) / (math.sin(angle_b_rad)) * (Y - X * (math.sin(angle_a_rad) / math.sin(angle_b_rad)))
            E = E / 1 - (math.sin(angle_a_rad) ** 2 / math.sin(angle_b_rad) ** 2)
            B = X - E
            A = (math.sin(angle_a_rad) / math.sin(angle_b_rad)) * B

            crop_img = image[int(round(A)):int(round(Y - A)),int(round(E)):int(round(X - E))]
            dim = (y,x)
            final = cv2.resize(crop_img,dim,interpolation = cv2.INTER_AREA)


        else:
            try:
                #checking image type just incase
                if isinstance(augimage.img, Image.Image):
                    x = augimage.img.size[0]
                    y = augimage.img.size[1]
                    image = augimage.img.rotate(angle, expand = True)
                    X = image.size[0]
                    Y = image.size[1]
                    angle_a = abs(angle)
                    angle_b = 90 - angle_a
                    angle_a_rad = math.radians(angle_a)
                    angle_b_rad = math.radians(angle_b)
                    angle_a_sin = math.sin(angle_a_rad)
                    angle_b_sin = math.sin(angle_b_rad)
                    E = (math.sin(angle_a_rad)) / (math.sin(angle_b_rad)) * (Y - X * (math.sin(angle_a_rad) / math.sin(angle_b_rad)))
                    E = E / 1 - (math.sin(angle_a_rad) ** 2 / math.sin(angle_b_rad) ** 2)
                    B = X - E
                    A = (math.sin(angle_a_rad) / math.sin(angle_b_rad)) * B
                    image = image.crop((int(round(E)), int(round(A)), int(round(X - E)), int(round(Y - A))))
                    final = image.resize((x, y), resample=Image.BICUBIC)

            except Exception as e:
                print(Fore.RED+"Error:"+Fore.RESET, end="")
                print(e)
                exit()

        name, ext = augimage.name.split(".")
        path = augimage.targPath+"/"+name+"_"+str(idx)+"."+ext
        final.save(path)
        
