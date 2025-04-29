
#represents a set of types where the value could be any of the types
class TypedUnion:
  def __init__(self, types=[]):
    self.types = types

  def __eq__(self, other):
    if type(other) != TypedUnion:
      return False

    return self.types == other.types

  def __repr__(self):
    return f"({' | '.join(str(t) for t in self.types)})"

  def reduce(self, other):
    #TODO: is this really how reduction works for unions? i think if any are nothing, then it should fail entirely right...?
    reduced = [t.reduce(other) for t in self.types]
    reduced = [t for t in reduced if type(t) != TypedNothing]
    if len(reduced) == 0:
      return TypedNothing()
    if len(reduced) == 1:
      return reduced[0]
    return TypedUnion(reduced)

  def satisfied_by(self, other):
    return any([t.satisfied_by(other) for t in self.types])

from .typed_nothing import TypedNothing