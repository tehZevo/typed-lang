from typed_lang.parser import parse
from typed_lang.types import TypedUnion, TypedAny, TypedTuple, TypedType, TypedNothing, TypedIntersection
from .utils import TypedTestCase
from .types.types_for_testing import A, B, C, D, A_or_B, A_and_B, B_or_C, B_and_C

class TestOps(TypedTestCase):

  def test_union(self):
    result = parse("""
      @A
      @B
      A | B
    """)

    self.assertEqual(result[0], A_or_B)

  def test_union_2(self):
    result = parse("""
      @A
      @B
      @C

      (A | B) | (B | C)
    """)

    self.assertEqual(result[0], TypedUnion([A_or_B, B_or_C]))

  def test_intersection(self):
    result = parse("""
      @A
      @B
      A & B
    """)

    self.assertEqual(result[0], A_and_B)

  def test_intersection_2(self):
    result = parse("""
      @A
      @B
      @C

      (A | B) & (B | C)
    """)

    self.assertEqual(result[0], TypedIntersection([A_or_B, B_or_C]))

  #TODO: conditional doesnt make sense in "satisfied by" system
  # def test_conditional(self):
  #   result = parse("""
  #     @A
  #     @B
  #
  #     (A & B) ? A : B
  #   """)
  #
  #   self.assertEqual(result[0], TypedType("B"))
  #
  # def test_conditional_2(self):
  #   result = parse("""
  #     @A
  #     @B
  #
  #     (A | B) ? A : B
  #   """)
  #
  #   self.assertEqual(result[0], TypedType("A"))
