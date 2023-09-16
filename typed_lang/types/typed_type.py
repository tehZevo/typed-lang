from .typed_set import TypedSet
from .typed_nothing import TypedNothing
from .typed_any import TypedAny

#TODO: when we get to extending types, what is the base superclass? TypedNothing?
#represents a single (possibly parameterized) type
class TypedType:
  def __init__(self, type):
    self.type = type

  #TODO: handle interitance

  def __and__(self, other): return self if other == self else TypedNothing()
  def __or__(self, other): return TypedSet([self, other])

  #eqality operators mean "is satisfied by" or "satisfies"
  #eg `A < B` is read "is A satisfied by B"
  #and `A > B` is read "A satisfies B"
  #TODO: interactions with TypedSet
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
