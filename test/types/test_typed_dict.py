from unittest import TestCase
from typed_lang.types import TypedUnion, TypedIntersection

from .types_for_testing import A, B, C, A_or_B, A_and_B, C_or_D, C_and_D, DICT_A, DICT_B, DICT_AB

class TestTypedDict(TestCase):

  def test_neg_with_type(self):
    self.assertFalse(DICT_A.satisfied_by(A))

  def test_with_union(self):
    self.assertTrue(DICT_A.satisfied_by(TypedUnion([DICT_A, DICT_AB])))

  def test_neg_with_union(self):
    self.assertFalse(DICT_AB.satisfied_by(TypedUnion([DICT_A, DICT_B])))

  def test_with_intersection(self):
    self.assertTrue(DICT_AB.satisfied_by(TypedIntersection([DICT_A, DICT_B])))

  def test_neg_with_intersection(self):
    #TODO: naive test
    self.assertFalse(DICT_A.satisfied_by(TypedIntersection([DICT_B])))
