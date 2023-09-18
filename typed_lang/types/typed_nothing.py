
class TypedNothing:
  def __init__(self):
    pass

  def __eq__(self, other): return type(other) == TypedNothing
  def __hash__(self): return hash("Nothing")
  def __repr__(self): return "nothing"

  #TODO: is this correct?
  def satisfied_by(self, other):
    return False
