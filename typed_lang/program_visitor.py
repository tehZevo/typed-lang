import pprint

from .symbols import Terminal, Definition
from .evaluation_visitor import EvaluationVisitor

class ProgramVisitor:
  def __init__(self):
    self.context = {}

  def visit_terminal(self, terminal):
    assert terminal.identifier not in self.context
    self.context[terminal.identifier] = Terminal(terminal.identifier, terminal.params, terminal.supertypes)

  def visit_definition(self, definition):
    assert definition.identifier not in self.context
    #TODO: partially evaluate expression?
    self.context[definition.identifier] = Definition(definition.params, definition.expression)

  def visit_evaluate(self, eval_expr):
    #construct evaluation visitor with current context
    visitor = EvaluationVisitor(self.context)
    #evaluate expression with visitor
    type = eval_expr.expression.accept(visitor)

    return type
