from typed_lang.parser import parse
from typed_lang.types import TypedUnion, TypedAny, TypedTuple, TypedType, TypedNothing
from .utils import TypedTestCase

class TestTuple(TypedTestCase):
  pass
  #equality is broken somehow for tuples

  # def test_tuple(self):
  #   result = parse("""
  #     @A
  #     @B
  #     @C
  #
  #     (A, B, C)
  #
  #   """)
  #
  #   self.assertEqual(result[0], TypedTuple([
  #     TypedType("A"),
  #     TypedType("B"),
  #     TypedType("C"),
  #   ]))

  # def test_tuple_2(self):
  #   #TODO: this shouldnt pass
  #   result = parse("""
  #     @A
  #     @B
  #
  #     (A|B, B) & (A, A|B)
  #
  #   """)
  #
  #   print(result[0])
  #   print(TypedTuple([
  #     TypedType("A"),
  #     TypedType("A"),
  #   ]))
  #   #TODO: this shouldnt pass
  #   FAIL+KTHX
  #
  #   self.assertEqual(result[0], TypedTuple([
  #     TypedType("A"),
  #     TypedType("A"),
  #   ]))
