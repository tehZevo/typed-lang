import pprint

from .types import TypedSet, TypedTuple, TypedAny, TypedType

#base symbol class, symbols can be evaluated given a context
class Symbol:
  def __init__(self):
    pass

  #symbols have a value function to evaluate their value
  def value(self, context):
    raise NotImplementedError

#represents a terminal type
class Terminal(Symbol):
  def __init__(self, identifier, params):
    self.identifier = identifier
    self.params = params

  def value(self, context):
    #if parameterized:
    if len(self.params) > 0:

      #grab arguments from context
      print("params", self.params)
      args = [context[p] for p in self.params]
      #evaluate each arg
      vals = [arg.value(context) for arg in args]

      print("hello there", vals)
      print(type(vals[0]))
      #TODO: is this where the combinations should "blow up"?
      # ie should T[A|B, A|B] become {T[A, A], T[A, B], T[B, A], T[B, B]} ?
      vals = [
        [self.identifier + ("[" + ", ".join(v) + "]" if len(v) > 0 else "") for v in vals]
      ]

      print(vals)
      return TypedSet(vals)

    #otherwise just a single type
    return TypedType(self.identifier)

#represents a type definition (can be parameterized)
class Definition(Symbol):
  def __init__(self, params, expression):
    self.params = params
    self.expression = expression

  #TODO: modify context before so we dont have to pass args?
  def value(self, context):
    #TODO: circular import
    from .evaluation_visitor import EvaluationVisitor
    #use evaluation visitor to determine value of our expression:)
    visitor = EvaluationVisitor(context)
    print("dimension hopping...")
    #ding dong!
    return self.expression.accept(visitor)

#represents an argument in a parameterized terminal or definition, could itself be a terminal or definition
class Argument(Symbol):
  def __init__(self, arg):
    self.arg = arg

  def value(self, context):
    #TODO: circular import
    from .evaluation_visitor import EvaluationVisitor
    #use evaluation visitor to determine value of our expression:)
    visitor = EvaluationVisitor(context)
    return self.arg.accept(visitor)
