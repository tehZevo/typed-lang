from .typed_base import TypedBase

class TypedNothing(TypedBase):
  def __init__(self):
    pass

  def __eq__(self, other): return type(other) == TypedNothing
  def __repr__(self): return "Nothing"

  #TODO: is this correct?
  def satisfied_by(self, other):
    return False
