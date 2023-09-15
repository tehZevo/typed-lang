import unittest

from typed_lang.parser import parse

class TestBasic(unittest.TestCase):

  def test_terminal(self):
    result = parse("""
      @A
      A
    """)

    self.assertEqual(result, [{"A"}])
