"""
add test with argparse and shit
"""
from src.modules import flip
from src.utils import augImage

ai = augImage.AugImage("tests/test.jpg", targPath="tests/")
mod = flip.FlipImage()
mod.operate(ai, 3)

