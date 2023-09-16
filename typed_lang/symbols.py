import pprint

#base symbol class
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
    #TODO: get params like in definition
    return set(self.identifier)

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

#represents an argument in a parameterized type, could be a terminal or definition
#(or maybe another argument? idk)
class Argument(Symbol):
  def __init__(self, arg):
    self.arg = arg

  def value(self, context):
    #TODO: circular import
    from .evaluation_visitor import EvaluationVisitor
    #use evaluation visitor to determine value of our expression:)
    visitor = EvaluationVisitor(context)
    return self.arg.accept(visitor)
