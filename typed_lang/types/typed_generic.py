
#represents a type that can be evaluated given a context
class TypedGeneric:
  def __init__(self, params, expr):
    self.params = params
    self.expr = expr

  #TODO: generic pre-eval equality?
  def __eq__(self, other): return False

  def __repr__(self): return "Generic"

  def evaluate(self, context):
    print("dimension hopping...")
    #TODO: circular import
    from typed_lang.evaluation_visitor import EvaluationVisitor
    #use evaluation visitor to determine value of our expression :)
    #ding dong!
    return self.expr.accept(EvaluationVisitor(context))

  #TODO: generic pre-eval satisfaction?
  def satisfied_by(self, other):
    return False
