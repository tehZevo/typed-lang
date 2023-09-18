from unittest import TestCase
from typed_lang.types import TypedUnion, TypedTuple, TypedIntersection

from .types_for_testing import A, B, C, A_or_B, A_and_B, C_or_D, C_and_D, AB, BA

class TestTypedTuple(TestCase):

  def test_neg_with_type(self):
    self.assertFalse(AB.satisfied_by(A))

  def test_with_union(self):
    self.assertTrue(AB.satisfied_by(TypedUnion([AB, TypedTuple([
      A_and_B,
      A_and_B
    ])])))

  def test_neg_with_union(self):
    self.assertFalse(AB.satisfied_by(A_or_B))

  def test_with_intersection(self):
    self.assertTrue(AB.satisfied_by(TypedIntersection([AB, C])))

  def test_neg_with_intersection(self):
    self.assertFalse(AB.satisfied_by(A_and_B))
