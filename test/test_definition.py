from typed_lang.parser import parse
from typed_lang.types import TypedSet, TypedType
from .utils import TypedTestCase

class TestDefinition(TypedTestCase):

  def test_definition(self):
    result = parse("""
      @A

      X = A

      X
    """)

    self.assertEqual(result[0], TypedType("A"))

  # def test_unknown_type(self):
  #   #TODO: this should fail with a type error because A is not defined
  #   result = parse("""
  #     X = A
  #   """)
  #
  #   self.assertSetsEqual(result[0], [])

  def test_identity(self):
    result = parse("""
      @A

      Identity[X] = X

      Identity[A]
    """)

    self.assertEqual(result[0], TypedType("A"))

  def test_wrap(self):
    result = parse("""
      @A
      @Box[T]

      Wrap[X] = Box[X]

      Wrap[A]
    """)

    self.assertEqual(result[0], TypedType("Box[A]"))

  def test_apply(self):
    #TODO: why does this work even though X and F are flipped? this should fail
    result = parse("""
      @A
      @B

      Apply[F, X] = F[X]
      Identity[X] = X

      Apply[Identity, A]
    """)

    self.assertEqual(result[0], TypedType("A"))
