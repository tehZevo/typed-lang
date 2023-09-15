import unittest

from typed_lang.parser import parse

class TestDefinition(unittest.TestCase):

  def test_definition(self):
    result = parse("""
      @A

      X = A

      X
    """)

    self.assertEqual(result, [{"A"}])

  def test_unknown_type(self):
    #TODO: this should fail with a type error because A is not defined
    result = parse("""
      X = A
    """)

    self.assertEqual(result, [])
