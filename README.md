# Auglib
Software Project.

### Folders:

src : contains all the major files
modules: contains all the operational modules (flip, randomcrop etc)
utils: contains all the utility files. Primarily the wrapper class

### Case for AugImage (the wrapper class)

Dataset raw images may or may not have corresponding ground  truth images in different directories like masks in segmentation tasks. Plus there may be other params regarding image manipulation like keeping a track of number of ops performed on an image.
It just makes things easier

### Proposed rough structure of modules:

```

class <module name>:
  def __init__():
    probability: xxx     
    /// Plan is to assign higher weights to more relvant augmentations. 
    /// For instance, Flipping the image is more valuable augmentation over let's say, random erase.
    /// Now, If for instance W1(x1) + W2(x2) is the weight dependence, even for random probabilities x1,x2, W1 has to ensure it leads to higher number.
    /// We will have to think how to implement this.
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

