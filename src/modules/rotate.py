from PIL import Image
import cv2
import math
from random import randint



class rotateImage:
    def __init__(self):
        self.probability = 0.8
       
    def probs(self):
        return self._probability


    def operate(self,augimage):
        angle = random.randint(0,360)

        if augimage.format == "array":
            pass


        else:
            try:
                #checking image type just incase
                if isinstance(augimage.img, Image.Image):
                    x = augimage.img.size[0]
                    y = augimage.img.size[1]
                    image = augimage.img.rotate(rotation, expand = True)
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

                else:
                    raise TypeError
            except Exception as e:
                print(Fore.RED+"Error:"+Fore.RESET, end="")
                print(e)
                exit()