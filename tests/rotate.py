from src.modules import rotate
from src.utils import augImage


ai = augImage.AugImage("/home/pranjal/Pictures/test.jpg", targPath="/home/pranjal/Pictures", format="PIL")
mod = rotate.RotateImage()
mod.operate(ai,1)