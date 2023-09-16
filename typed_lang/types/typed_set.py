
#TODO: should operations that otherwise produce an empty typed set
# instead produce a TypedNothing?

#represents a set of valid types
class TypedSet:
  def __init__(self, types=[]):
    self.types = frozenset(types)

  def __and__(self, other): return TypedSet(self.types & other.types)
  def __or__(self, other): return TypedSet(self.types | other.types)

  #one typed set satisfies another if it contains everything needed to be the other set.
  #TODO: i think this doesnt necessarily hold true because python set logic has strict >/<
  def __eq__(self, other):
    if type(other) != TypedSet:
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
