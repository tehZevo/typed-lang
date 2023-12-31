
class TypedError(Exception):
  def __init__(self, msg):
    super().__init__(msg)

class UndefinedTypeError(TypedError):
  def __init__(self, type):
    super().__init__(f"Type '{type}' is not defined")

class AlreadyDefinedTypeError(TypedError):
  def __init__(self, type):
    super().__init__(f"Type '{type}' has already been defined")

class RequirementError(TypedError):
  def __init__(self, parameter, required, found):
    super().__init__(f"Parameter '{parameter}' requires '{required}', but found '{found}'")
