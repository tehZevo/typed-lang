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

  def satisfied_by(self, other):
    return True
