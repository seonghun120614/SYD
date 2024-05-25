from abc import ABC, abstractmethod


class BinaryStringMethod(ABC):
  @abstractmethod
  def get_binary_strings(self):
    pass