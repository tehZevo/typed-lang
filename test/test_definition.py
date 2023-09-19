from typed_lang.parser import parse
from typed_lang.types import TypedUnion, TypedType
from .utils import TypedTestCase
from .types.types_for_testing import Any, Nothing

class TestDefinition(TypedTestCase):

  def test_definition(self):
    result = parse("""
      @A

      X = A

      X
    """)

    self.assertEqual(result[0], TypedType("A"))

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

  #TODO: a parameterized type, you can get the value of given a context
  # (which will modify the context and then evaluate its expression)
  #TODO: an unparameterized type can be immediately evaluated
  #TODO: name the parameterized symbols "functions" and the unparameterized "values"
  #TODO: all symbols will either be a function type or a non-function type
  # function types can be evaluated given a context
  #TODO: this will reduce the symbol types to only one (instead of argument/definition/terminal)
  #TODO: need to differentiate between generic definition and generic evaluation

  #TODO: to fix, i think we have to evaluate types upon passing in
  #TODO: this could get difficult when (not) evaluating parameterized types ie Apply[F, X]
  # as we should not try to call F
  # def test_scope2(self):
  #   result = parse("""
  #     @Cup[T]
  #     @A
  #
  #     #even though this parameter T clashes with the parameter in Cup, we should still be able to construct a Cup[Something]
  #     X[T] = Cup[T]
  #
  #     X = Cup[A]
  #
  #     X[A]
  #   """)
  #
  #   self.assertEqual(result, [Any, Nothing])

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
