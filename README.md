# Auglib
Software Project.

### Folders:

src : contains all the major files
modules: contains all the operational modules (flip, randomcrop etc)
utils: contains all the utility files. Primarily the wrapper class

### Case for AugImage (the wrapper class)

Dataset raw images may or may not have corressponding ground  truth images in different directories like masks in segmentation tasks. Plus there may be other params regarding image manipulation like keeping a track of number of ops performed on an image.
It just makes things easier

### Porposed rough structure of modules:

```

class <module name>:
  def __init__():
    probability: xxx #need to discuss
    #other module specific init
  
  ...module specific functions that you may need...
  
  def operate(augimage obj, idx):
      #obj is the augimage type object
      #idx is the index provided by the driver file(?) to append to image name to signify augmentation iteration
      
      #do shit here
      
```      
  
### some other stuff

Images can exist in two forms: cv2 (np array) and PIL (Image format). Save operations are performed with cv because ease of use. Incase of Image items, they are converted to cv format and then saved. 

Can check flip.py for reference.

### Todo:

1. Readme having modules to be implemented
2. TESTS (WEEK 3)

