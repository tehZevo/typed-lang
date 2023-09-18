from typed_lang.parser import parse
from typed_lang.types import TypedUnion, TypedAny, TypedTuple, TypedType, TypedNothing, TypedDict
from .utils import TypedTestCase
from .types.types_for_testing import Any, Nothing

class TestSatisfaction(TypedTestCase):

  def test_satisfaction(self):
    result = parse("""
      @A
      @B

      A >= A
      A >= B
      B >= A
      B >= B
    """)

    self.assertEqual(result, [Any, Nothing, Nothing, Any])
