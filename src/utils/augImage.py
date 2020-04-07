from PIL import Image
import cv2
import numpy as np   
import os
import sys
from colorama import Fore
import matplotlib.pyplot as plt


class AugImage:
    """
    A wrapper class around images to suit our purposes. Holds 
    information regarding the image, operations performed etc.

    Parameters: 
        -> path: path to original image
        -> truthPath: path to ground truth if any
        -> label: numerical label
        -> targPath: where to store the augemented image
        -> targTruthPath: where to store the augmented mask 
        -> format: format to read the images in 
    Properties:
        -> path: path to original image
        -> truthPath: path to ground truth if any
        -> label: numerical label
        -> targPath: where to store the augemented image
        -> targTruthPath: where to store the augmented mask         
        -> size : tuple containing the dimensions of the image
        -> img: the image either in PIL or numpy format
        -> format: PIL or Numpy
        -> tensor: boolean indicating tensor value (false as of now)
        -> groundTruth: stores the ground truth if any wrt to a image (masks etc)
        -> operations: list containing all the ops performed on the image
      
    """
    def __init__(self, path, format="array", truthPath=None, label=None, 
                targPath=None, targTruthPath=None
    ):
        self.path = path
        self.name = os.path.basename(path)
        self.format = format
        self.truthPath = truthPath
        self.label = label
        self.targPath = targPath #should be same as path. recheck later
        self.targTruthPath = targTruthPath #should be same as truthPath. recheck later
        self.img = None
        self.groundTruth = None
        self.tensor = False
        self.operations = []
        self.truthName = None #ideally it should be the same as name. but who knows

        try:
            if self.format == "array":
                pass
            elif self.format == "PIL":
                pass
            else:
                raise NotImplementedError
        except NotImplementedError:
            print(Fore.RED+"Error:"+Fore.RESET, end="")   
            print("NotImplementedError: Image format {} not supported. Can be "\
                   "only \"array\" or \"PIL\" ".format(self.format))
        
        try: 
            self.img = cv2.imread(self.path)
        except Exception as e:
            print(Fore.RED+"Exception:"+Fore.RESET, end="")
            print(e)
            exit()

        self.size = self.img.shape

        if self.truthPath is not None:
            try:
                self.groundTruth = cv2.imread(self.truthPath) 
                self.truthName = os.path.basename(self.truthPath)
            except:
                print(Fore.RED+"Exception:"+Fore.RESET, end="")
                print(e)
                exit()
        else:
            self.groundTruth = None                        

    def attrs(self):
        """
        Returns a dict containing the attributes of the current 
        image and their associated values
        """
        return self.__dict__

    def load_image(default=True):
        """
        Returns the image either in PIL format or opencv format 
        """
        if default:
            print("in heres")
            return self.img
        else:
            img = Image.fromarray(cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB))
            self.size = img.shape
            return img   

    def shape(self):
        return self.size


    