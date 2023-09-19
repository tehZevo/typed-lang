#TODO: track evaluation depth between here and symbols
import pprint

from .types import TypedTuple, TypedNothing, TypedIntersection, TypedUnion, TypedDict, TypedAny, TypedGeneric, TypedType
from .nodes import ParameterizedTerminal

class EvaluationVisitor:
  def __init__(self, context):
    self.context = context.copy()
    # print("Beginning evaluation with context:")
    # pprint.pprint(context)

  def create_context(self, generic):
    print("generic", generic)
    print(generic.identifier, generic.params)
    #extract param names
    param_names = self.context[generic.identifier].params
    #create arguments for the generic we're evaluating
    #pull from symbol table
    #TODO: handle this more smoothly
    if type(generic) == ParameterizedTerminal:
      args = [self.context[k] for k in generic.params]
    else:
      args = [self.context[k.identifier] for k in generic.params]
    #put them into the copied context
    context = self.context.copy()
    print("context before")
    pprint.pprint(context)
    context.update({k: v for k, v in zip(param_names, args)})
    print("context after")
    pprint.pprint(context)
    #evaluate
    return context

  def visit_terminal(self, terminal):
    #TODO: is this needed?
    raise NotImplementedError

  def visit_definition(self, definition):
    #TODO: is this needed?
    raise NotImplementedError

  def visit_typecall(self, typecall):
    print("handling typecall")
    #create context and evaluate
    symbol = self.context[typecall.identifier]
    return symbol.evaluate(self.create_context(typecall))

  def visit_parameterized_terminal(self, terminal):
    print("handling parameterized terminal")
    #create context and evaluate
    symbol = self.context[terminal.identifier]
    context = self.create_context(terminal)
    #TODO: kinda jank, just create the type here...
    #TODO: need some way to store complex types inside of a terminal (/typedtype)?
    return TypedType(f"{terminal.identifier}[{', '.join([context[p].type for p in symbol.params])}]")

  def visit_type(self, _type):
    assert _type.identifier in self.context
    #just return the symbol in our context
    print("handling specified")
    return self.context[_type.identifier]

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
