from abc import ABC, abstractmethod


class Board(ABC):
    @abstractmethod
    def choose(self, plot_type: str, row: int, col: int): pass
    
    @abstractmethod
    def draw(self): pass
    
    @abstractmethod
    def set(self, row: int, col: int, x: str, y: str): pass
    
    @abstractmethod
    def resize(self, width: int, height: int): pass