
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

  #TODO: rename intersect to reduce
  #TODO: once intersection/reduce is done, then we can remove >= i think
  def intersect(self, other):
    #TODO "distribute" the reduction
    #TODO: if A satisfies B but B doesn't satisfy A, then the reduction is B
    pass

  def satisfied_by(self, other):
    return any([t.satisfied_by(other) for t in self.types])
