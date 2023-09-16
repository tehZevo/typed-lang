
class TypedNothing:
  def __init__(self):
    pass

  def __and__(self, other): return TypedNothing()
  def __or__(self, other): return other

  def __gt__(self, other): return False
  def __ge__(self, other): return type(other) == TypedNothing
  def __eq__(self, other): return type(other) == TypedNothing
  def __lt__(self, other): return type(other) != TypedNothing
  def __le__(self, other): return True

  def __hash__(self): return hash("Nothing")
  def __repr__(self): return "nothing"
