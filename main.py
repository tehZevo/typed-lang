
from typed_lang.parser import parse

program_file = "example.types"

with open(program_file, "r") as f:
  result = parse(f.read(), True)
  print(result)
