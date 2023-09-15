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
