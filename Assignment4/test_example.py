"""Basic Unit testing for example.py"""

from random import randint
import pytest
from example import increment, COLORS


def increment():

    assert increment(3) == 3
