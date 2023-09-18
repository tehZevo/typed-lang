from unittest import TestCase
from typed_lang.types import TypedAny
from .types_for_testing import A, B, C, A_or_B, A_and_B, C_or_D, C_and_D

class TestTypedAny(TestCase):

  def test_with_type(self):
    self.assertTrue(TypedAny().satisfied_by(A))
