import unittest

from typed_lang.parser import parse

class TestOps(unittest.TestCase):

  def test_union(self):
    result = parse("""
      @A
      @B
      A | B
    """)

    self.assertEqual(result, [{"A", "B"}])

  def test_union_2(self):
    result = parse("""
      @A
      @B
      @C

      (A | B) | (B | C)
    """)

    self.assertEqual(result, [{"A", "B", "C"}])

  def test_intersection(self):
    result = parse("""
      @A
      @B
      A & B
    """)

    self.assertEqual(result, [set()])

  def test_intersection_2(self):
    result = parse("""
      @A
      @B
      @C

      (A | B) & (B | C)
    """)

    self.assertEqual(result, [{"B"}])

  def test_conditional(self):
    result = parse("""
      @A
      @B

      (A & B) ? A : B
    """)

    self.assertEqual(result, [{"B"}])

  def test_conditional_2(self):
    result = parse("""
      @A
      @B

      (A | B) ? A : B
    """)

    self.assertEqual(result, [{"A"}])
