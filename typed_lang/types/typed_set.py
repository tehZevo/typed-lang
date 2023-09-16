#represents a set of valid types
class TypedSet:
  def __init__(self, types=[]):
    self.types = frozenset(types)

  def __and__(self, other): return TypedSet(self.types & other.type)
  def __or__(self, other): return TypedSet(self.types | other.type)

  def __gt__(self, other): return self.types > other.type
  def __ge__(self, other): return self.types >= other.type
  def __lt__(self, other): return self.types < other.type
  def __le__(self, other): return self.types <= other.type
  def __eq__(self, other): return self.types == other.type

  def __len__(self): return len(self.types)
  def __iter__(self): return self.types.__iter__()

  def __hash__(self): return hash(self.types)
  def __repr__(self): return str(set(self.types))
