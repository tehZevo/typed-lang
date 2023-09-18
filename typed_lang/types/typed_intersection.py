
#represents a set of valid types, all of which must be satisfied
class TypedIntersection:
  def __init__(self, types=[]):
    self.types = types

  def __eq__(self, other):
    if type(other) != TypedIntersection:
      return False

    return self.types == other.types

  def satisfied_by(self, other):
    return all([t.satisfied_by(other) for t in self.types])
