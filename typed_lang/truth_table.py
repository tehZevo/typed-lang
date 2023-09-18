import itertools

class TruthTable:

  #TODO: more elegant pls
  def num_inputs(self, stuff):
    counter = 0
    for thing in stuff:
      if thing is not None:
        break

      counter += 1

    return counter

  def table(self):
    stuff = [
      None,
      None,
      [(0, 1), lambda a, b: a & b]
    ]

    num_inputs = self.num_inputs(stuff)
    print(num_inputs)

    inputs = list(itertools.product([True,False], repeat=2))
    print(inputs)

    rows = []
    #skip inputs
    for op_idx, op_func in stuff[num_inputs:]:
      for combo in inputs:
        t = list(combo)
        #run op on values in row
        op_result = op_func(*[t[i] for i in op_idx])
        t.append(op_result)
        rows.append(t)

    print(rows)

if __name__ == "__main__":
  TruthTable().table()
