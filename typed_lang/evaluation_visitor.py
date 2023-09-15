#TODO: track evaluation depth between here and symbols
import pprint

from .symbols import Terminal, Definition, Argument

class EvaluationVisitor:
  def __init__(self, context):
    self.context = context

  def visit_type(self, _type):
    print(_type.identifier)
    pprint.pprint(self.context)
    assert _type.identifier in self.context

    #grab symbol from table
    symbol = self.context[_type.identifier]
    print("handling symbol type", symbol.__class__.__name__)

    #if it's a terminal symbol, just return its value
    if type(symbol) == Terminal:
      return symbol.value()

    #same with argument
    if type(symbol) == Argument:
      return symbol.value(self.context)

    #if it's a definition...
    if type(symbol) == Definition:
      #interesting, so to evaluate P[Q[T]] we have to first evaluate Q[T]
      #visit all arg types
      #TODO: how to handle definitions passed as params?
      args = [Argument(arg) for arg in _type.params]
      print("args", args)

      #create context for definition to be evaluated
      context = self.context.copy()
      print(symbol.params)
      context.update({k: v for k, v in zip(symbol.params, args)})
      print("modified context:")
      pprint.pprint(context)

      #pass args to symbol (which better be a definition: todo assert/raise error)
      #TODO: raise error if type in context is not a definition
      #TODO: raise error if arg count mismatch
      definition = self.context[_type.identifier]
      return definition.value(context)

    raise TypeError(f"Unhandlable symbol type '{type(symbol).__name__}'")

    raise NotImplementedError

  def visit_union(self, union):
    left = union.left.accept(self)
    right = union.right.accept(self)
    return set([*left, *right])
