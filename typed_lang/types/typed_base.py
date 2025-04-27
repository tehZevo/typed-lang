

class TypedBase:
  def __init__(self):
    pass

  def __eq__(self, other): raise NotImplementedError
  def __repr__(self): raise NotImplementedError
  def intersect(self, other): raise NotImplementedError
  def satisfied_by(self, other): raise NotImplementedError
