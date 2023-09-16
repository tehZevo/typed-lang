from typed_lang.parser import parse
from .utils import TypedTestCase

class TestOps(TypedTestCase):

  def test_union(self):
    result = parse("""
      @A
      @B
      A | B
    """)

    self.assertEqual(result[0], {"A", "B"})

  def test_union_2(self):
    result = parse("""
      @A
      @B
      @C

      (A | B) | (B | C)
    """)

    self.assertEqual(result[0], {"A", "B", "C"})

  def test_intersection(self):
    result = parse("""
      @A
      @B
      A & B
    """)

    self.assertEqual(result[0], set())

  def test_intersection_2(self):
    result = parse("""
      @A
      @B
      @C

      (A | B) & (B | C)
    """)

    self.assertEqual(result[0], {"B"})

  def test_conditional(self):
    result = parse("""
      @A
      @B

      (A & B) ? A : B
    """)

    self.assertEqual(result[0], {"B"})

  def test_conditional_2(self):
    result = parse("""
      @A
      @B

      (A | B) ? A : B
    """)

    self.assertEqual(result[0], {"A"})

  def test_tuple(self):
    result = parse("""
      @A
      @B
      @C

      (A, B, C)

    """)

    self.assertEqual(result[0], {({"A"}, {"B"}, {"C"})})

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
