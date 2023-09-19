
class Node:
  def __init__(self, tokens):
    #TODO: infer start/end line/column/pos from tokens, not just based on first token
    #TODO: filter to only lark token type
    self.line = tokens[0].line
    self.column = tokens[0].column

  def accept(self, visitor):
    raise NotImplementedError

class Program(Node):
  def __init__(self, tokens):
    super().__init__(tokens)
    self.statements = tokens

  def accept(self, visitor):
    #return a list of statement return values where not none
    results = [s.accept(visitor) for s in self.statements]
    return [r for r in results if r is not None]

class Definition(Node):
  def __init__(self, tokens, identifier, expression):
    super().__init__(tokens)
    self.identifier = identifier
    self.expression = expression

  def accept(self, visitor):
    return visitor.visit_definition(self)

class ParameterizedDefinition(Node):
  def __init__(self, tokens, identifier, params, expression):
    super().__init__(tokens)
    self.identifier = identifier
    self.params = params
    self.expression = expression

  def accept(self, visitor):
    return visitor.visit_parameterized_definition(self)

class Expression(Node):
  def __init__(self, tokens):
    super().__init__(tokens)

class Type(Expression):
  def __init__(self, tokens, identifier):
    super().__init__(tokens)
    self.identifier = identifier

  def __repr__(self):
    return f"Type node {self.identifier}"

  def accept(self, visitor):
    return visitor.visit_type(self)

class TypeCall(Expression):
  def __init__(self, tokens, identifier, params):
    super().__init__(tokens)
    #TODO: rename params to "args"?
    self.identifier = identifier
    self.params = params

  def __repr__(self):
    return f"TypeCall node {self.identifier}"

  def accept(self, visitor):
    return visitor.visit_typecall(self)

class Union(Expression):
  def __init__(self, tokens, left, right):
    super().__init__(tokens)
    self.left = left
    self.right = right

  def accept(self, visitor):
    return visitor.visit_union(self)

class Intersection(Expression):
  def __init__(self, tokens, left, right):
    super().__init__(tokens)
    self.left = left
    self.right = right

  def accept(self, visitor):
    return visitor.visit_intersection(self)

class Conditional(Expression):
  def __init__(self, tokens, iv, den, elzz):
    super().__init__(tokens)
    self.iv = iv
    self.den = den
    self.elzz = elzz

  def accept(self, visitor):
    return visitor.visit_conditional(self)

class Tuple(Expression):
  def __init__(self, tokens):
    super().__init__(tokens)
    self.types = tokens

  def accept(self, visitor):
    return visitor.visit_tuple(self)

class Dict(Expression):
  def __init__(self, tokens, key_value_pairs):
    super().__init__(tokens)
    self.key_value_pairs = key_value_pairs

  def accept(self, visitor):
    return visitor.visit_dict(self)

class Satisfaction(Expression):
  def __init__(self, tokens, left, right):
    super().__init__(tokens)
    self.left = left
    self.right = right

  def accept(self, visitor):
    return visitor.visit_satisfaction(self)

class Terminal(Node):
  def __init__(self, tokens, identifier):
    super().__init__(tokens)
    self.identifier = identifier

  def accept(self, visitor):
    return visitor.visit_terminal(self)

class ParameterizedTerminal(Node):
  def __init__(self, tokens, identifier, params):
    super().__init__(tokens)
    self.identifier = identifier
    self.params = params

  def __repr__(self):
    return f"ParameterizedTerminal {self.identifier}[{','.join(self.params)}]"

  def accept(self, visitor):
    return visitor.visit_parameterized_terminal(self)

#TODO: assumes an expression is always just an identifier
class Evaluate(Node):
  def __init__(self, tokens, expression):
    super().__init__(tokens)
    self.expression = expression

  def accept(self, visitor):
    return visitor.visit_evaluate(self)
