### Module Name: Flip

**File**: src/modules/flip.py

**Task**: Flip the given training images and their associated masks/label images.

**How to use?**

```
from src.modules import flip
from src.utils import augImage
ai = augImage.AugImage("tests/test.jpg", targPath="tests/")
mod = flip.FlipImage()
mod.operate(ai, 3)
```
