
#represents any possible type
class TypedAny:
  def __init__(self):
    pass

  def __eq__(self, other): return type(other) == TypedAny

  def satisfied_by(self, other):
    return True
