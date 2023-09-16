from typed_lang.parser import parse
from typed_lang.types import TypedSet, TypedAny, TypedTuple
from .utils import TypedTestCase

class TestOps(TypedTestCase):

  def test_union(self):
    result = parse("""
      @A
      @B
      A | B
    """)

    self.assertEqual(result[0], TypedSet({"A", "B"}))

  def test_union_2(self):
    result = parse("""
      @A
      @B
      @C

      (A | B) | (B | C)
    """)

    self.assertEqual(result[0], TypedSet({"A", "B", "C"}))

  def test_intersection(self):
    result = parse("""
      @A
      @B
      A & B
    """)

    self.assertEqual(result[0], TypedSet())

  def test_intersection_2(self):
    result = parse("""
      @A
      @B
      @C

      (A | B) & (B | C)
    """)

    self.assertEqual(result[0], TypedSet({"B"}))

  def test_conditional(self):
    result = parse("""
      @A
      @B

      (A & B) ? A : B
    """)

    self.assertEqual(result[0], TypedSet({"B"}))

  def test_conditional_2(self):
    result = parse("""
      @A
      @B

      (A | B) ? A : B
    """)

    self.assertEqual(result[0], TypedSet({"A"}))

  #TODO: reenable and fix tuple tests
  # def test_tuple(self):
  #   result = parse("""
  #     @A
  #     @B
  #     @C
  #
  #     (A, B, C)
  #
  #   """)
  #
  #   self.assertEqual(result[0], {({"A"}, {"B"}, {"C"})})

  # def test_tuple_2(self):
  #   result = parse("""
  #     @A
  #     @B
  #     @C
  #
  #     (A|B, B) & (A, A|B)
  #
  #   """)
  #
  #   self.assertEqual(result[0], {("A", "B")})
