from typed_lang.parser import parse
import argparse

parser = argparse.ArgumentParser(prog="typed")
parser.add_argument("program", help="the typed file to run")
args = parser.parse_args()

with open(args.program, "r") as f:
  result = parse(f.read(), True)
  print(result)
