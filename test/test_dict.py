from typed_lang.parser import parse
from typed_lang.types import TypedUnion, TypedAny, TypedTuple, TypedType, TypedNothing, TypedDict
from .utils import TypedTestCase
from .types.types_for_testing import A, B, C, D, A_or_B, A_and_B, B_or_C, B_and_C

class TestDict(TypedTestCase):
  pass

  #TODO
  # def test_dict(self):
  #   result = parse("""
  #     @A
  #     @B
  #     @C
  #
  #     Z = {
  #       a: A,
  #       b: B,
  #     }
  #
  #     Z
  #   """)
  #
  #   self.assertEqual(result[0], TypedDict([
  #     ["a", A],
  #     ["b", B]
  #   ]))
