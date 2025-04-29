from .typed_base import TypedBase
from .typed_nothing import TypedNothing

#a type composed of multiple types
class TypedTuple(TypedBase):
  def __init__(self, types):
    self.types = tuple(types)

  def tuple_op(self, other, op, len_or_else=False):
    if len(self.types) != len(other.types):
      return len_or_else

    return TypedTuple([op(a, b) for a, b in zip(self.types, other.types)])

  def __eq__(self, other): return self.tuple_op(other, lambda a, b: a == b)

  def __repr__(self):
    return f"({', '.join(str(t) for t in self.types)})"

  def reduce(self, other):
    if type(other) != TypedTuple:
      return TypedNothing()
    
    if len(other.types) != len(self.types):
      return TypedNothing()
    
    intersection = []
    for a, b in zip(self.types, other.types):
      intersection.append(a.reduce(b))
    
    return TypedTuple(intersection)

  def satisfied_by(self, other):
    #TODO: how to ensure the order in a more elegant manner?
    if type(other) == TypedTuple:
      return all([a.satisfied_by(b) for a, b in zip(self.types, other.types)])
    #if ANY in the intersection satisfy us, then we're satisfied (think "A extends B and C" satisfies "B")
    if type(other) == TypedIntersection:
      return any([self.satisfied_by(t) for t in other.types])
    if type(other) == TypedUnion:
      return any([self.satisfied_by(t) for t in other.types])

    return False

from .typed_intersection import TypedIntersection
from .typed_union import TypedUnion
