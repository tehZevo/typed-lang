from typed_lang.parser import parse
from .utils import TypedTestCase

class TestDefinition(TypedTestCase):

  def test_definition(self):
    result = parse("""
      @A

      X = A

      X
    """)

    self.assertSetsEqual(result[0], {"A"})

  # def test_unknown_type(self):
  #   #TODO: this should fail with a type error because A is not defined
  #   result = parse("""
  #     X = A
  #   """)
  #
  #   self.assertSetsEqual(result[0], [])
