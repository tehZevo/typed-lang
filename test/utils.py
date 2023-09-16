import unittest

def sets_equal(a, b):
  return set(a) == set(b)

from .utils import sets_equal

class TypedTestCase(unittest.TestCase):

  def assertSetsEqual(self, a, b):
    self.assertEqual(set(a), set(b))
