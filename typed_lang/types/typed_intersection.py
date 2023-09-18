from .errors import OperatorError

#represents a set of valid types, all of which must be satisfied
class TypedIntersection:
  def __init__(self, types=[]):
    print(types)
    self.types = frozenset(types)
    print("after", self.types)

  def __and__(self, other):
    if type(other) == TypedUnion: return TypedUnion(self.types & other.types)
    elif type(other) == TypedType: return self & TypedUnion([other])

    raise OperatorError("&", self, other)

  def __or__(self, other):
    if type(other) == TypedUnion: return TypedUnion(self.types | other.types)
    elif type(other) == TypedType: return self | TypedUnion([other])

    raise OperatorError("&", self, other)

  #one typed set satisfies another if it contains everything needed to be the other set.
  #TODO: i think this doesnt necessarily hold true because python set logic has strict >/<
  def __eq__(self, other):
    if type(other) != TypedIntersection:
      return False

    return self.types == other.types

  #TODO: these maybe should be n^2 where we ensure that all of our types are satisfied by at least one of the other types
  def __gt__(self, other): return self.types > other.types
  def __lt__(self, other): return self.types < other.types
  def __ge__(self, other): return self > other or self == other
  def __le__(self, other): return self < other or self == other

  def __len__(self): return len(self.types)
  def __iter__(self): return self.types.__iter__()

  def __hash__(self): return hash(self.types)
  def __repr__(self): return str(set(self.types))

  def satisfied_by(self, other):
    return all([t.satisfied_by(other) for t in self.types])

#TODO: circular import
from .typed_type import TypedType
from .typed_union import TypedUnion
