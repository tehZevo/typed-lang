#TODO: track evaluation depth between here and symbols
import pprint

from .symbols import Terminal, Definition, Argument
from .types import TypedTuple, TypedNothing, TypedIntersection, TypedUnion

class EvaluationVisitor:
  def __init__(self, context):
    self.context = context
    print("Beginning evaluation with context:")
    pprint.pprint(context)

  def visit_type(self, _type):
    print(_type.identifier)
    assert _type.identifier in self.context

    #grab symbol from table
    symbol = self.context[_type.identifier]
    print("handling symbol type", symbol.__class__.__name__)

    #TODO: try to unify signatures of each symbol's value
    # ie can we give each symbol type params (even if they dont use them),
    # then modify context, and pass the new context to the symbols?
    # this would dedupe the similarity between terminal and definition

    #if it's a terminal symbol, just return its value
    if type(symbol) == Terminal:
      #create arguments for the type we're evaluating
      args = [Argument(arg) for arg in _type.params]
      #create context for definition to be evaluated
      context = self.context.copy()
      context.update({k: v for k, v in zip(symbol.params, args)})

      #pass args to symbol (which better be a definition: todo assert/raise error)
      #TODO: raise error if type in context is not a definition
      #TODO: raise error if arg count mismatch
      v = symbol.value(context)
      return v

    #same with argument
    if type(symbol) == Argument:
      return symbol.value(self.context)

    #if it's a definition...
    if type(symbol) == Definition:
      #create arguments for the type we're evaluating
      args = [Argument(arg) for arg in _type.params]
      #create context for definition to be evaluated
      context = self.context.copy()
      context.update({k: v for k, v in zip(symbol.params, args)})

      #pass args to symbol (which better be a definition: todo assert/raise error)
      #TODO: raise error if type in context is not a definition
      #TODO: raise error if arg count mismatch
      v = symbol.value(context)
      return v

    raise TypeError(f"Unhandlable symbol type '{type(symbol).__name__}'")

    raise NotImplementedError

  def visit_union(self, union):
    left = union.left.accept(self)
    right = union.right.accept(self)
    return TypedUnion([left, right])

  def visit_intersection(self, intersection):
    left = intersection.left.accept(self)
    right = intersection.right.accept(self)
    return TypedIntersection([left, right])

  def visit_conditional(self, conditional):
    #if the result of the "iv" expression is not the empty set, return den
    print("hello", conditional.iv.accept(self))
    if conditional.iv.accept(self) != TypedNothing():
      return conditional.den.accept(self)

    #else return elzz
    return conditional.elzz.accept(self)

  def visit_tuple(self, _tuple):
    #send help
    return TypedTuple([t.accept(self) for t in _tuple.types])
