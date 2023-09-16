from typed_lang.parser import parse
from .utils import TypedTestCase

class TestTerminal(TypedTestCase):

  def test_terminal(self):
    result = parse("""
      @A
      A
    """)

    self.assertSetsEqual(result[0], {"A"})

  def test_parameterized(self):
    result = parse("""
      @A
      @Box[T]

      Box[A]
    """)

    self.assertSetsEqual(result[0], {"Box[A]"})

  def test_parameterized_2(self):
    result = parse("""
      @A
      @B
      @C
      @Triple[X, Y, Z]

      Triple[A, B, C]
    """)

    self.assertSetsEqual(result[0], {"Box[A]"})

  def test_parameterized_3(self):
    result = parse("""
      @A
      @Box[T]

      B = A

      (Box[A] & Box[B])
    """)

    self.assertSetsEqual(result[0], {"Box[A]"})
