from typed_lang.parser import parse
from typed_lang.types import TypedUnion, TypedAny, TypedTuple, TypedType, TypedNothing
from .utils import TypedTestCase

class TestOps(TypedTestCase):

  def test_union(self):
    result = parse("""
      @A
      @B
      A | B
    """)

    self.assertEqual(result[0], TypedUnion([
      TypedType("A"),
      TypedType("B"),
    ]))

  def test_union_2(self):
    result = parse("""
      @A
      @B
      @C

      (A | B) | (B | C)
    """)

    self.assertEqual(result[0], TypedUnion([
      TypedType("A"),
      TypedType("B"),
      TypedType("C"),
    ]))

  def test_intersection(self):
    result = parse("""
      @A
      @B
      A & B
    """)

    self.assertEqual(result[0], TypedNothing())

  def test_intersection_2(self):
    result = parse("""
      @A
      @B
      @C

      (A | B) & (B | C)
    """)

    self.assertEqual(result[0], TypedUnion([TypedType("B")]))

  def test_conditional(self):
    result = parse("""
      @A
      @B

      (A & B) ? A : B
    """)

    self.assertEqual(result[0], TypedType("B"))

  def test_conditional_2(self):
    result = parse("""
      @A
      @B

      (A | B) ? A : B
    """)

    self.assertEqual(result[0], TypedType("A"))
