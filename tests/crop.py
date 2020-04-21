from src.utils import augImage

from src.modules import crop

ai = augImage.AugImage("tests/test.jpg", targPath="tests/")
mod = crop.CropImage(width=1000,height=2000)
mod.operate(ai,2)
