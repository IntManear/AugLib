### Module Name: Rotate

**File**: src/modules/rotate.py

**Task**: rotate the given training images and their associated masks/label images.

**How to use?**

```
from src.modules import rotate
from src.utils import augImage

ai = augImage.AugImage("tests/test.jpg", targPath="tests/", format="PIL")
mod = rotate.RotateImage()
mod.operate(ai,1)

```
