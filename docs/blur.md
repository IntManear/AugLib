### Module Name: Blur

**File**: src/modules/blur.py

**Task**: blur the given training images and their associated masks/label images.

**How to use?**

```
from src.utils import augImage
from src.modules import blur

ai = augImage.AugImage(r"tests/test.py", targPath=r"tests/")
mod = blur.BlurImage()
mod.operate(ai,2)

```
