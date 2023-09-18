from unittest import TestCase
from typed_lang.types import TypedUnion

from .types_for_testing import A, B, C, A_or_B, A_and_B, C_or_D, C_and_D

class TestTypedUnion(TestCase):

  def test_with_type(self):
    self.assertTrue(A_or_B.satisfied_by(A))

  def test_neg_with_type(self):
    self.assertFalse(A_or_B.satisfied_by(C))

  def test_with_union(self):
    self.assertTrue(A_or_B.satisfied_by(TypedUnion([A, A_and_B])))

  def test_neg_with_union(self):
    self.assertFalse(A_or_B.satisfied_by(C_or_D))

  def test_with_intersection(self):
    self.assertTrue(A_or_B.satisfied_by(A_and_B))

  def test_neg_with_intersection(self):
    self.assertFalse(A_or_B.satisfied_by(C_and_D))
