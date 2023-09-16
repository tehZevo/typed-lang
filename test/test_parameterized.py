import unittest

from typed_lang.parser import parse

class TestParameterized(unittest.TestCase):

  def test_identity(self):
    result = parse("""
      @A

      Identity[X] = X

      Identity[A]
    """)

    self.assertEqual(result, [{"A"}])

  def test_wrap(self):
    result = parse("""
      @A
      @Box[T]

      Wrap[X] = Box[X]

      Wrap[A]
    """)

    self.assertEqual(result, [{"Box[A]"}])

  def test_apply(self):
    #TODO: why does this work even though X and F are flipped? this should fail
    result = parse("""
      @A
      @B

      Apply[F, X] = F[X]
      Identity[X] = X

      Apply[Identity, A]
    """)

    self.assertEqual(result, [{"A"}])
