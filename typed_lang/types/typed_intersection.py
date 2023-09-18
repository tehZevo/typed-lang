
#represents a set of valid types, all of which must be satisfied
class TypedIntersection:
  def __init__(self, types=[]):
    print(types)
    self.types = frozenset(types)
    print("after", self.types)

  #one typed set satisfies another if it contains everything needed to be the other set.
  #TODO: i think this doesnt necessarily hold true because python set logic has strict >/<
  def __eq__(self, other):
    if type(other) != TypedIntersection:
      return False

    return self.types == other.types

  #TODO: is this needed?
  def __len__(self): return len(self.types)
  #TODO: is this needed?
  def __iter__(self): return self.types.__iter__()
  def __hash__(self): return hash(self.types)
  def __repr__(self): return str(set(self.types))

  def satisfied_by(self, other):
    return all([t.satisfied_by(other) for t in self.types])
