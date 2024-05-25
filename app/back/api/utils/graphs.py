from abc import ABC, abstractmethod

import base64
import io

import matplotlib.pyplot as plt
import pandas as pd

from .binary_string_generator import BinaryStringMethod


class Graph(ABC, BinaryStringMethod):

  def __init__(self, Graph):
    if not isinstance(Graph, pd.Series):
      raise TypeError("The Graph parameter must be a pandas Series")
    super().__init__()
    self.graph = Graph


  def get_binary_strings(self):
    return {
      _: self.image_to_binary(self.graph, _)
      for _ in self.kinds
    }

  
  @staticmethod
  def image_to_binary(series, kind):
    if not isinstance(series, pd.Series):
      raise TypeError("The wrong argument received. It must be the instance of pandas.Series")
    
    fig, ax = plt.subplots()
    series.plot(ax = ax, kind=kind)
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)
    
    binary_data = buf.getvalue()
    binary_string = base64.b64encode(binary_data).encode('utf-8')
    return binary_string