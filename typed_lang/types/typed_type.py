from .typed_set import TypedSet
from .typed_nothing import TypedNothing

#represents a single (possibly parameterized) type
class TypedType:
  def __init__(self, type):
    self.type = type

  #TODO: handle interitance
  def __and__(self, other): self if other == self else TypedNothing()
  def __or__(self, other): return TypedSet([self, other])

  #eqality operators mean "is satisfied by" or "satisfies" eg `A < B` is read "is A satisfied by B"
  def __gt__(self, other): return type(other) != TypedAny
  def __ge__(self, other): return True
  def __eq__(self, other): return type(other) == TypedAny
  def __lt__(self, other): return False
  def __le__(self, other): return type(other) == TypedAny

  def __hash__(self): return hash(self.type)
  def __repr__(self): return self.type
