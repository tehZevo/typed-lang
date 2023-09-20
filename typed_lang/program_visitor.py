import pprint

from .evaluation_visitor import EvaluationVisitor
from .types import TypedGeneric, TypedType, TypedAny
from .errors import AlreadyDefinedTypeError

class ProgramVisitor:
  def __init__(self):
    self.context = {}

  def evaluate_reqs(self, params):
    new_params = []
    for (name, expr) in params:
      #nones mean any type satisfies
      if expr is None:
        new_params.append((name, TypedAny()))
        continue

      val = expr.accept(EvaluationVisitor(self.context))

      new_params.append((name, val))

    return new_params

  def visit_terminal(self, terminal):
    if terminal.identifier in self.context:
      raise AlreadyDefinedTypeError(terminal.identifier)

    self.context[terminal.identifier] = TypedType(terminal.identifier)

  def visit_parameterized_terminal(self, terminal):
    if terminal.identifier in self.context:
      raise AlreadyDefinedTypeError(terminal.identifier)

    #put the terminal in a generic for evaluation later
    #evaluate param requirements
    params = self.evaluate_reqs(terminal.params)
    self.context[terminal.identifier] = TypedGeneric(params, terminal)

  def visit_definition(self, definition):
    if definition.identifier in self.context:
      raise AlreadyDefinedTypeError(definition.identifier)

    self.context[definition.identifier] = definition.expression.accept(EvaluationVisitor(self.context))

  def visit_parameterized_definition(self, definition):
    if definition.identifier in self.context:
      raise AlreadyDefinedTypeError(definition.identifier)

    #TODO: partially evaluate expression?
    #evaluate param requirements
    params = self.evaluate_reqs(definition.params)
    self.context[definition.identifier] = TypedGeneric(params, definition.expression)

  def visit_evaluate(self, eval_expr):
    #construct evaluation visitor with current context and evaluate expression with visitor
    return eval_expr.expression.accept(EvaluationVisitor(self.context))
