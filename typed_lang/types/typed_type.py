from .typed_base import TypedBase

#TODO: when we get to extending types, what is the base superclass? TypedNothing?
#represents a single (possibly parameterized) type
class TypedType(TypedBase):
  def __init__(self, name, generics=None):
    self.name = name
    self.generics = generics if generics is not None else []

  #TODO: handle interitance
  def __eq__(self, other):
    if type(other) != TypedType:
      return False

    #TODO: handle generics
    return self.name == other.name

  def __repr__(self):
    if len(self.generics) == 0:
      return self.name

    return f"{self.name}[{', '.join([str(g) for g in self.generics])}]"

  def reduce(self, other):
    if type(other) == TypedIntersection:
      return other.reduce(self)
    if type(other) == TypedUnion:
      return other.reduce(self)
    
    #TODO: need a length check on generics somewhere during creation
    if type(other) == TypedType \
        and self.name == other.name \
        and len(self.generics) == len(other.generics):
      reduction = [a.reduce(b) for a, b in zip(self.generics, other.generics)]
      return TypedType(self.name, reduction)
    
    return TypedNothing()

  def satisfied_by(self, other):
    if type(other) == TypedType: return self.name == other.name
    #NOTE: all must satisfy this in a union (ie, A|B does not satisfy A, because it could be B)
    if type(other) == TypedUnion: return all([self.satisfied_by(t) for t in other.types])
    if type(other) == TypedIntersection: return any([self.satisfied_by(t) for t in other.types])

    return False

from .typed_union import TypedUnion
from .typed_intersection import TypedIntersection
from .typed_nothing import TypedNothing
