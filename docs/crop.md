### Module Name: Crop

**File**: src/modules/crop.py

**Task**: crop the given training images and their associated masks/label images.

**How to use?**

```
from src.utils import augImage
from src.modules import crop

ai = augImage.AugImage("tests/test.jpg", targPath="tests/")
mod = crop.CropImage(width=1000,height=2000)
mod.operate(ai,2)

```
