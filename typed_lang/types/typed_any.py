
#represents any possible type
#TODO: idk maybe this should be Unit?
class TypedAny:
  def __init__(self):
    pass

  def __eq__(self, other): return type(other) == TypedAny

  def __repr__(self): return "Any"

  def intersect(self, other):
    return other

  def satisfied_by(self, other):
    from . import TypedNothing #TODO: import
    if type(other) == TypedNothing:
      return False
    return True
