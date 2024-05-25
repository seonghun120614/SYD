import io
import base64

import matplotlib
matplotlib.use('Agg')
import pandas as pd
import matplotlib.pyplot as plt

from .binary_string_generator import BinaryStringMethod


class Frame(BinaryStringMethod):
  def __init__(self, path):
    self.frame = pd.read_csv(path).dropna()
  
  def get_binary_strings(self):
    try:
      result = dict()
      columns = self.frame.columns
      
      for col in columns:
        series = self.frame[col].dropna()
        
        if series.dtype == "float64":
          result[col] = Frame.image_to_binary(series, 'hist')
        
        elif series.dtype == 'object':
          series = series.value_counts()
          result[col] = Frame.image_to_binary(series, 'pie')
      
      return result
  
    except Exception as e:
      print(e)
  
  
  @classmethod
  def image_to_binary(self, series, kind):
    
    if not isinstance(series, pd.Series):
      raise TypeError("The wrong argument received. It must be the instance of pandas.Series")
    
    fig, ax = plt.subplots()
    series.plot(ax=ax, kind=kind)
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)
    
    binary_data = buf.getvalue()
    binary_string = base64.b64encode(binary_data).decode('utf-8')
    return binary_string