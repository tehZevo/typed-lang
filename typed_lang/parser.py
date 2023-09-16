from lark import Lark, Tree, Transformer, v_args

from .nodes import Terminal, Evaluate, Program, Union, Intersection, Type, \
  Definition, Conditional
from .program_visitor import ProgramVisitor

grammar_file = "types.lark"
parser = Lark.open(grammar_file, start="program")

#TODO: maybe move parsing rules to nodes and visitor methods as well?
# yes that is an anti pattern for visitor

@v_args(inline=True)
class TypeLang(Transformer):
  def __init__(self):
    super().__init__()
    self.context = {}

  def program(self, *tokens):
    return Program(tokens)

  def terminal(self, *tokens):
    identifier = tokens[0]
    params = tokens[1]
    return Terminal(tokens, identifier.value, params)

  def definition(self, *tokens):
    (identifier, params, expression) = tokens
    return Definition(tokens, identifier.value, params, expression)

  #idk why this is needed to prevent params from being a tree but ok
  def params(self, *tokens):
    #TODO: for now, map to values as well
    return [t.value for t in tokens]

  def union(self, *tokens):
    (left, right) = tokens
    return Union(tokens, left, right)

  def intersection(self, *tokens):
    (left, right) = tokens
    return Intersection(tokens, left, right)

  def conditional(self, *tokens):
    (iv, den, elzz) = tokens
    return Conditional(tokens, iv, den, elzz)

  def evaluate(self, *tokens):
    (expression,) = tokens
    return Evaluate(tokens, expression)

  def type(self, *tokens):
    identifier = tokens[0]
    params = tokens[1:]

    return Type(tokens, identifier, params)

def parse(text, print_tree=False):
  tree = parser.parse(text)
  if print_tree:
    print(tree.pretty())

  program = TypeLang().transform(tree)

  visitor = ProgramVisitor()

  return program.accept(visitor)
