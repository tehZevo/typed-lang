import unittest

from typed_lang.parser import parse

class TestTerminal(unittest.TestCase):

  def test_terminal(self):
    result = parse("""
      @A
      A
    """)

    self.assertEqual(result, [{"A"}])

  def test_parameterized(self):
    result = parse("""
      @A
      @Box[T]

      Box[A]
    """)

    self.assertEqual(result, [{"Box[A]"}])

  def test_parameterized_2(self):
    result = parse("""
      @A
      @Box[T]

      B = A

      (Box[A] & Box[B])
    """)

    self.assertEqual(result, [{"Box[A]"}])
