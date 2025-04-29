#TODO: remove - intersections don't actually exist
from .typed_base import TypedBase

#represents a combination of types
class TypedIntersection(TypedBase):
  def __init__(self, types=[]): #TODO: this should probably take two types as a binary operator, not a list
    self.types = types

  def __eq__(self, other):
    if type(other) != TypedIntersection:
      return False

    return self.types == other.types

  def __repr__(self):
    return " & ".join([t.__repr__() for t in self.types])
  
  def reduce(self, other):
    reduced = [t.reduce(other) for t in self.types]
    reduced = [t for t in reduced if type(t) != TypedNothing]
    if len(reduced) == 0:
      return TypedNothing()
    if len(reduced) == 1:
      return reduced[0]
    return TypedIntersection(reduced)
  
  def satisfied_by(self, other):
    return all([t.satisfied_by(other) for t in self.types])

from .typed_nothing import TypedNothing