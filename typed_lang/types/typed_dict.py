
class TypedDict:
  def __init__(self, key_value_pairs):
    self.types = dict(key_value_pairs)

  def __eq__(self, other):
    if type(other) != TypedDict:
      return False

    if len(self.types) != len(other.types):
      return False

    return all([self.types[k] == other.types[k] for k in self.types.keys])

    return type(other) == TypedAny

  def key_satisfied_by(self, other, key):
    if key not in other:
      return False

    return self[key].satisfied_by(other[key])

  def satisfied_by(self, other):
    #each key could be satisfied by either type in the intersection
    if type(other) == TypedIntersection:
      return all([
        any([self.key_satisfied_by(t, key) for t in other.types])
        for key in self.types.keys()
      ])

    if type(other) == TypedUnion:
      return all([
        all([self.key_satisfied_by(t, key) for t in other.types])
        for key in self.types.keys()
      ])

    return False
