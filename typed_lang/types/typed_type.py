from .typed_base import TypedBase

#TODO: when we get to extending types, what is the base superclass? TypedNothing?
#represents a single (possibly parameterized) type
class TypedType(TypedBase):
  def __init__(self, type):
    self.type = type

  #TODO: handle interitance
  def __eq__(self, other):
    if type(other) != TypedType:
      return False

    return self.type == other.type

  def __repr__(self): return self.type

  def intersect(self, other):
    if self.type == other.type:
      return self
    
    return TypedNothing()

  def satisfied_by(self, other):
    if type(other) == TypedType: return self.type == other.type
    #NOTE: all must satisfy this in a union (ie, A|B does not satisfy A, because it could be B)
    if type(other) == TypedUnion: return all([self.satisfied_by(t) for t in other.types])
    if type(other) == TypedIntersection: return any([self.satisfied_by(t) for t in other.types])

    return False

from .typed_union import TypedUnion
from .typed_intersection import TypedIntersection
from .typed_nothing import TypedNothing
