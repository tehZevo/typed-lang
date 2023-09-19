import pprint

from .evaluation_visitor import EvaluationVisitor
from .types import TypedGeneric, TypedType

#TODO: just collapse this and evaluation into one visitor?
class ProgramVisitor:
  def __init__(self):
    self.context = {}

  def visit_terminal(self, terminal):
    assert terminal.identifier not in self.context
    self.context[terminal.identifier] = TypedType(terminal.identifier)

  def visit_parameterized_terminal(self, terminal):
    assert terminal.identifier not in self.context
    #put the terminal in a generic for evaluation later
    self.context[terminal.identifier] = TypedGeneric(terminal.params, terminal)

  def visit_definition(self, definition):
    assert definition.identifier not in self.context
    self.context[definition.identifier] = definition.expression.accept(EvaluationVisitor(self.context))

  def visit_parameterized_definition(self, definition):
    assert definition.identifier not in self.context
    #TODO: partially evaluate expression?
    self.context[definition.identifier] = TypedGeneric(definition.params, definition.expression)

  def visit_evaluate(self, eval_expr):
    #construct evaluation visitor with current context and evaluate expression with visitor
    return eval_expr.expression.accept(EvaluationVisitor(self.context))
