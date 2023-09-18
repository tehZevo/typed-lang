
#represents any possible type
class TypedAny:
  def __init__(self):
    pass

  def __eq__(self, other): return type(other) == TypedAny
  def __hash__(self): return hash("Any")
  def __repr__(self): return "any"

  def satisfied_by(self, other):
    return True
