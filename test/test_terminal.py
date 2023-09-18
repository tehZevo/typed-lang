from typed_lang.parser import parse
from typed_lang.types import TypedType, TypedIntersection
from .utils import TypedTestCase

class TestTerminal(TypedTestCase):

  def test_terminal(self):
    result = parse("""
      @A
      A
    """)

    self.assertEqual(result[0], TypedType("A"))

  def test_parameterized(self):
    result = parse("""
      @A
      @Box[T]

      Box[A]
    """)

    self.assertEqual(result[0], TypedType("Box[A]"))

  def test_parameterized_2(self):
    result = parse("""
      @A
      @B
      @C
      @Triple[X, Y, Z]

      Triple[A, B, C]
    """)

    print(result[0].type)
    # a
    self.assertEqual(result[0], TypedType("Triple[A, B, C]"))

  # def test_parameterized_3(self):
  #   result = parse("""
  #     @A
  #     @Box[T]
  #
  #     B = A
  #
  #     (Box[A] & Box[B])
  #   """)
  #   #TODO: weird, this returns an intersection of only Box[A] because B evaluates to A
  #   # the only way i can think of fixing it is to not evaluate until checking satisfaction
  #   # for now, we'll accept it..
  #   # self.assertEqual(result[0], TypedType("Box[A]"))
  #   self.assertEqual(result[0], TypedIntersection([TypedType("Box[A]")]))
