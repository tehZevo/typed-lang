from .typed_nothing import TypedNothing

#TODO: make it so tuples arent "covariant"? that or just wait until we add variance modifiers

#a type composed of multiple types
class TypedTuple:
  def __init__(self, types):
    #TODO: is this where it should "blow up" combinatorially?
    # as in, create a set of each combination?
    self.types = tuple(types)

  def tuple_op(self, other, op, len_or_else=False):
    if len(self.types) != len(other.types):
      return len_or_else

    return TypedTuple([op(a, b) for a, b in zip(self.types, other.types)])

  def __and__(self, other): return self.tuple_op(other, lambda a, b: a & b, TypedNothing)
  def __or__(self, other): return self.tuple_op(other, lambda a, b: a | b, TypedNothing)

  def __gt__(self, other): return self.tuple_op(other, lambda a, b: a > b)
  def __ge__(self, other): return self.tuple_op(other, lambda a, b: a >= b)
  def __lt__(self, other): return self.tuple_op(other, lambda a, b: a < b)
  def __le__(self, other): return self.tuple_op(other, lambda a, b: a <= b)
  def __eq__(self, other): return self.tuple_op(other, lambda a, b: a == b)

  def __hash__(self): return hash(self.types)
  def __repr__(self): return str(self.types)
