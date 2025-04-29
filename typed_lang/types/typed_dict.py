from .typed_base import TypedBase

class TypedDict(TypedBase):
  def __init__(self, type_dict):
    self.types = type_dict

  def __eq__(self, other):
    if type(other) != TypedDict:
      return False

    if len(self.types) != len(other.types):
      return False

    return all([self.types[k] == other.types[k] for k in self.types.keys])

    return type(other) == TypedAny

  def key_satisfied_by(self, other, key):
    if type(other) != TypedDict or key not in other.types:
      return False

    return self.types[key].satisfied_by(other.types[key])

  def intersect(self, other):
    #TODO: allow intersections with unions
    if type(other) != TypedDict:
      return TypedNothing()

    intersection = {}
    for key in self.types.keys():
      if key not in other.types:
        continue
      a = self.types[key]
      b = other.types[key]
      intersection[key] = a.intersect(b)
    
    return TypedDict(intersection)

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

    if type(other) == TypedDict:
      return all([
        self.key_satisfied_by(other, key)
        for key in self.types.keys()
      ])

    return False
  
  def __repr__(self):
    return self.types.__repr__()

from .typed_intersection import TypedIntersection
from .typed_union import TypedUnion
