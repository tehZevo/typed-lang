import unittest

from typed_lang.parser import parse
from typed_lang.types import TypedSet, TypedAny, TypedTuple

def py_to_typed(py):
  if type(py) == str:
    #any maps to the TypedAny type, otherwise just return the string
    if py.lower() == "any":
      return TypedAny()

    return py

  if type(py) == set:
    return TypedSet([py_to_typed(e) for e in py])

  if type(py) == tuple or type(py) == list:
    return TypedTuple([py_to_typed(e) for e in py])

  raise ValueError(f"Not sure how to handle {type(py)}: {py}")

def sets_equal(a, b):
  return set(a) == set(b)

class TypedTestCase(unittest.TestCase):

  def assertSetsEqual(self, a, b):
    self.assertEqual(set(a), set(b))

if __name__ == "__main__":
  x = py_to_typed("any")
  print(type(x), x)

  x = py_to_typed(("any",))
  print(type(x), x)

  x = py_to_typed({"A"})
  print(type(x), x)
