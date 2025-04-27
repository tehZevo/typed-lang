from unittest import TestCase

from typed_lang.parser import parse
from typed_lang.types import TypedUnion, TypedAny, TypedTuple, TypedType, TypedNothing, TypedIntersection
from .types.types_for_testing import A, B, C, D, A_or_B, A_and_B, B_or_C, B_and_C, Any, Nothing

class TestOps(TestCase):

  def test_union(self):
    result = parse("""
      @A
      @B

      A >= A | B
    """)

    self.assertEqual(result[0], Any)

  def test_union_2(self):
    result = parse("""
      @A
      @B
      @C

      Z = (A | B) | (B | C)

      A >= Z
      B >= Z
      C >= Z
    """)

    self.assertEqual(result, [Any, Any, Any])

  def test_intersection(self):
    result = parse("""
      @A
      @B

      A & B >= A
    """)

    self.assertEqual(result[0], Any)

  def test_intersection_2(self):
    result = parse("""
      @A
      @B
      @C

      Z = (A | B) & (B | C)

      A >= Z
      B >= Z #TODO: why this not satisfy
      C >= Z
    """)

    self.assertEqual(result, [Nothing, Any, Nothing])

  def test_conditional(self):
    result = parse("""
      @A
      @B

      A >= A ? A : B
      A >= B ? A : B
    """)

    self.assertEqual(result, [A, B])


  # def test_either(self):
  #   result = parse("""
  #     # @A
  #     # @B
  #     # @Some[T]
  #     # @None
  #     #
  #     # # Either[T] = Some[T] | None
  #     #
  #     # Some[A]
  #     #
  #     # # Either[A]
  #
  #     @A
  #     @X[T]
  #
  #     #this works
  #     Y[V] = X[V]
  #     #this is infinite recursion, probably need to copy context somewhere
  #     #Y[T] = X[T]
  #
  #     Y[A]
  #   """)
  #
  #   self.assertEqual(result, [A, B])
