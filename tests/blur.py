from src.utils import augImage

from src.modules import blur

ai = augImage.AugImage(r"C:\Users\Dhruv\Pictures\SRM_ID-Back.jpg", targPath=r"C:\Users\Dhruv\Pictures")
mod = blur.BlurImage()
mod.operate(ai,2)
