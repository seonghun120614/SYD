import pandas as pd

from .graphs import Graph
from .binary_string_generator import BinaryStringMethod


class Frame(BinaryStringMethod):
  
  def __init__(self, csv: str):
    super().__init__()
    self.df = pd.read_csv(csv)


  def get_binary_strings(self):
    try:
      return {_ : Graph(_).get_binary_string() for _ in self.df.columns}
    except TypeError:
      print("Type Error!")
