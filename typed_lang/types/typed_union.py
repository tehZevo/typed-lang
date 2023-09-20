
#represents a set of valid types, any of which would satisfy
class TypedUnion:
  def __init__(self, types=[]):
    self.types = types

  def __eq__(self, other):
    if type(other) != TypedUnion:
      return False

    return self.types == other.types

  def __repr__(self):
    return f"({' | '.join(str(t) for t in self.types)})"

  def satisfied_by(self, other):
    return any([t.satisfied_by(other) for t in self.types])
