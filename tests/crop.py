from src.utils import augImage

from src.modules import crop

ai = augImage.AugImage("/home/aayush/Pictures/hollow-knight-minimal-4k-6s-3840x2160.jpg", targPath="/home/aayush/Desktop")
mod = crop.CropImage(width=1000,height=2000)
mod.operate(ai,2)
