from lark import Lark, Tree, Transformer, v_args

from .nodes import Terminal, Evaluate, Program, Union, Intersection, Type, \
  Definition, Conditional, Tuple, Dict, Satisfaction, ParameterizedTerminal, \
  ParameterizedDefinition, TypeCall, AnyLiteral, NothingLiteral
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
    (identifier,) = tokens
    return Terminal(tokens, identifier.value)

  def parameterized_terminal(self, *tokens):
    identifier, params = tokens
    return ParameterizedTerminal(tokens, identifier.value, params)

  def definition(self, *tokens):
    identifier, expression = tokens
    return Definition(tokens, identifier.value, expression)

  def parameterized_definition(self, *tokens):
    identifier, params, expression = tokens
    return ParameterizedDefinition(tokens, identifier.value, params, expression)

  #idk why this is needed to prevent params from being a tree but ok
  def params(self, *tokens):
    #TODO: for now, map to values as well
    return [(id.value, req) for (id, req) in tokens]

  def param(self, *tokens):
    (identifier,) = tokens
    #map requirement to None
    return (identifier, None)

  def param_with_req(self, *tokens):
    (identifier, expr) = tokens
    return (identifier, expr)

  #idk why this is needed to prevent params from being a tree but ok
  def types(self, *tokens):
    #TODO: for now, map to values as well
    return [t for t in tokens]

  def union(self, *tokens):
    (left, right) = tokens
    return Union(tokens, left, right)

  def intersection(self, *tokens):
    (left, right) = tokens
    return Intersection(tokens, left, right)

  def conditional(self, *tokens):
    (iv, den, elzz) = tokens
    return Conditional(tokens, iv, den, elzz)

  def tuple(self, *tokens):
    return Tuple(tokens)

  def dict(self, *tokens):
    key_value_pairs = tokens[1:-1]
    return Dict(tokens, key_value_pairs)

  def key_value(self, *tokens):
    key, value = tokens
    return (key.value, value)

  def evaluate(self, *tokens):
    (expression,) = tokens
    print(tokens)
    return Evaluate(tokens, expression)

  def satisfaction(self, *tokens):
    (left, right) = tokens
    return Satisfaction(tokens, left, right)

  def type(self, *tokens):
    t = tokens[0]

    if t.type == "ANY":
      return AnyLiteral(tokens)
    if t.type == "NOTHING":
      return NothingLiteral(tokens)

    return Type(tokens, t)

  def typecall(self, *tokens):
    identifier, args = tokens
    return TypeCall(tokens, identifier.value, args)

def parse(text, print_tree=False):
  tree = parser.parse(text)
  if print_tree:
    print(tree.pretty())

  program = TypeLang().transform(tree)

  visitor = ProgramVisitor()

  return program.accept(visitor)
