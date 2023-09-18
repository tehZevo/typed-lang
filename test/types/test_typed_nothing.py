from unittest import TestCase
from typed_lang.types import TypedNothing

from .types_for_testing import A, B, C, A_or_B, A_and_B, C_or_D, C_and_D

class TestTypedNothing(TestCase):

  def test_neg_with_type(self):
    self.assertFalse(TypedNothing().satisfied_by(A))
