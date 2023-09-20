from unittest import TestCase

from typed_lang.parser import parse
from typed_lang.types import TypedUnion, TypedType
from typed_lang.errors import RequirementError
from .types.types_for_testing import Any, Nothing

class TestDefinition(TestCase):

  def test_definition(self):
    result = parse("""
      @A

      X = A

      X
    """)

    self.assertEqual(result[0], TypedType("A"))

  def test_requirement(self):
    result = parse("""
      @A

      X[T: A] = A

      X[A]
    """)

    self.assertEqual(result[0], TypedType("A"))

  def test_neg_requirement(self):
    self.assertRaises(RequirementError, parse, """
      @A
      @B

      X[T: A] = A

      X[B]
    """)

  #TODO: requires covariance
  # def test_option(self):
  #   result = parse("""
  #     @Some[T]
  #     @None
  #     @A
  #
  #     Option[T] = Some[T] | None
  #
  #     #TODO: i think this requires covariance
  #     UnboxOption[O: Option[any], T] = T #Option[T] >= O ? T : nothing
  #
  #     UnboxOption[Some[A], A]
  #   """)
  #
  #   self.assertEqual(result[0], TypedType("Box[A]"))

  def test_scope(self):
    result = parse("""
      @Box[T]
      @A
      @B

      #the type "B" here is a parameter, so this should not return Box[B] unless B was passed to X
      X[B] = Box[B]

      X[A] >= Box[A]
      X[A] >= Box[B]
    """)

    self.assertEqual(result, [Any, Nothing])

  def test_scope2(self):
    print("---BEGIN TEST SCOPE 2---")
    result = parse("""
      @Cup[X]
      @T

      Brew[X] = Cup[X]

      Brew[T]
    """)

    self.assertEqual(result[0], TypedType("Cup[T]"))

  #TODO: super/sub types
  # def test_subtype(self):
  #   result = parse("""
  #     @A
  #
  #     @Option[T]
  #     @Some[T] extends Option[T]
  #     @None extends Option[Nothing]
  #
  #     @F extends A, B, C, D
  #
  #     X = A
  #
  #     Some[A]
  #   """)
  #
  #   self.assertEqual(result[0], TypedType("A"))

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
