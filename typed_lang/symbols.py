import pprint

from .types import TypedUnion, TypedTuple, TypedAny, TypedType

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

      #grab arguments from context and evaluate each
      args = [context[param].value(context) for param in self.params]

      print("hello there", args)
      print(type(args[0]))
      #TODO: is this where the combinations should "blow up"?
      # ie should T[A|B, A|B] become {T[A, A], T[A, B], T[B, A], T[B, B]} ?

      args = self.identifier + ("[" + ", ".join([str(a) for a in args]) + "]" if len(args) > 0 else "")

      return TypedType(args)

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
