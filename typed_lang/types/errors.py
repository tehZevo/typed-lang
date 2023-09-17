
class OperatorError(Exception):
  def __init__(self, op, a, b):
    message = f"{op} is not allowed for types {a.__class__.__name__} and {b.__class__.__name__}"
    super().__init__(message)
