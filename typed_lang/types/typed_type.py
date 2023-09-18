
#TODO: when we get to extending types, what is the base superclass? TypedNothing?
#represents a single (possibly parameterized) type
class TypedType:
  def __init__(self, type):
    self.type = type

  #TODO: handle interitance

  def __and__(self, other):
    if type(other) == TypedUnion:
      return TypedUnion([self]) & other

    return self if other == self else TypedNothing()

  def __or__(self, other):
    if type(other) == TypedUnion:
      return TypedUnion([self]) | other

    return TypedUnion([self, other])

  #eqality operators mean "is satisfied by" or "satisfies"
  #eg `A < B` is read "is A satisfied by B"
  #and `A > B` is read "A satisfies B"
  #TODO: interactions with TypedUnion
  def __eq__(self, other):
    if type(other) != TypedType:
      return False

    return self.type == other.type

  def __gt__(self, other): return type(other) == TypedNothing
  def __lt__(self, other): return type(other) == TypedAny
  def __ge__(self, other): return self > other or self == other
  def __le__(self, other): return self < other or self == other

  def __hash__(self): return hash(self.type)
  def __repr__(self): return self.type

  def satisfied_by(self, other):
    if type(other) == TypedType: return self.type == other.type
    #NOTE: all must satisfy this in a union (ie, A|B does not satisfy A, because it could be B)
    if type(other) == TypedUnion: return all([self.satisfied_by(t) for t in other.types])
    if type(other) == TypedIntersection: return any([self.satisfied_by(t) for t in other.types])

    return False

from .typed_union import TypedUnion
from .typed_nothing import TypedNothing
from .typed_any import TypedAny
from .typed_intersection import TypedIntersection
