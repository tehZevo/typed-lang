#TODO: for now, we'll use `>=`/`<=` to mean "satisfies" and "is satisfied by"

#types here is the set of types that would satisfy this type
class TypedType:
  def __init__(self, types):
    self.type = frozenset(types)

  def __and__(self, other): return TypedType(self.type & other.type)
  def __or__(self, other): return TypedType(self.type | other.type)

  def __gt__(self, other): return self.type > other.type
  def __ge__(self, other): return self.type >= other.type
  def __lt__(self, other): return self.type < other.type
  def __le__(self, other): return self.type <= other.type
  def __eq__(self, other): return self.type == other.type

  def __hash__(self): return hash(self.type)
  def __repr__(self): return str(sorted(set(self.type)))

#represents any possible type
class TypedAny:
  def __init__(self):
    pass

  def __and__(self, other): return other
  def __or__(self, other): return TypedAny()

  def __gt__(self, other): return type(other) != TypedAny
  def __ge__(self, other): return True
  def __eq__(self, other): return type(other) == TypedAny
  def __lt__(self, other): return False
  def __le__(self, other): return type(other) == TypedAny

  def __hash__(self): return hash("Any")
  def __repr__(self): return "any"


class TypedTuple:
  def __init__(self, types):
    self.types = tuple(types)

  def tuple_op(self, other, op):
    return TypedTuple(tuple([op(a, b) for a, b in zip(self.types, other.types)]))

  def __and__(self, other): return self.tuple_op(other, lambda a, b: a & b)
  def __or__(self, other): return self.tuple_op(other, lambda a, b: a | b)

  def __gt__(self, other): return self.tuple_op(other, lambda a, b: a > b)
  def __ge__(self, other): return self.tuple_op(other, lambda a, b: a >= b)
  def __lt__(self, other): return self.tuple_op(other, lambda a, b: a < b)
  def __le__(self, other): return self.tuple_op(other, lambda a, b: a <= b)
  def __eq__(self, other): return self.tuple_op(other, lambda a, b: a == b)

  def __hash__(self): return hash(self.types)
  def __repr__(self): return str(self.types)


###

if __name__ == "__main__":
  A = TypedType(["A"])
  B = TypedType(["B"])

  AB = A | B

  a_ab = TypedTuple([A, AB])
  ab_b = TypedTuple([AB, B])

  a_a = TypedTuple([A, A])
  b_b = TypedTuple([B, B])

  # (A, A|B) | (A|B, B) -> (A|B, A|B)
  print(a_ab | ab_b)

  # (A, A|B) & (A|B, B) -> (A, B)
  print(a_ab & ab_b)

  # (A, A) & (B, B) -> (A|B, A|B)
  print(a_a | b_b)

  any = TypedAny()

  print("does any equal any?", any == any)

  print("is any less than A?", any < A)

  print("is any greater than A?", any > A)

  print("any or A", any | A)

  print("any and A", any & A)
