#TODO: track evaluation depth between here and symbols
import pprint

from .symbols import Terminal, Definition, Argument
from .types import TypedTuple, TypedNothing, TypedIntersection, TypedUnion, TypedDict, TypedAny

class EvaluationVisitor:
  def __init__(self, context):
    self.context = context.copy()
    # print("Beginning evaluation with context:")
    # pprint.pprint(context)

  def visit_type(self, _type):
    assert _type.identifier in self.context

    #grab symbol from table
    symbol = self.context[_type.identifier]
    print("handling symbol type", symbol.__class__.__name__)

    #TODO: try to unify signatures of each symbol's value
    # ie can we give each symbol type params (even if they dont use them),
    # then modify context, and pass the new context to the symbols?
    # this would dedupe the similarity between terminal and definition

    #handle terminal
    if type(symbol) == Terminal:

      #create arguments for the type we're evaluating
      args = [Argument(arg) for arg in _type.params]
      #create context for definition to be evaluated
      context = self.context.copy()
      #TODO: right here is where the recursive T -> T happens
      print(_type.identifier)
      print(list(zip(symbol.params, _type.params)))
      print("context before")
      pprint.pprint(context)
      context.update({k: v for k, v in zip(symbol.params, args)})
      print("context after")
      pprint.pprint(context)
      # if "T" in context and type(context["T"]) == Argument:
      #   a

      #pass args to symbol (which better be a definition: todo assert/raise error)
      #TODO: raise error if type in context is not a definition
      #TODO: raise error if arg count mismatch
      v = symbol.value(context)
      return v

    #handle argument
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

  def visit_dict(self, _dict):
    #send more help
    return TypedDict(dict([(k, v.accept(self)) for k, v in _dict.key_value_pairs]))

  def visit_satisfaction(self, satisfaction):
    #eval left and right
    left = satisfaction.left.accept(self)
    right = satisfaction.right.accept(self)

    #if left satisfies right, then return any, else return nothing
    if right.satisfied_by(left):
      return TypedAny()

    return TypedNothing()
