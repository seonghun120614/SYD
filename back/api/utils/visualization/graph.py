from abc import ABC, abstractmethod
from typing import Literal

PLOT_TYPE = Literal["barplot", "lineplot", "histplot", "scatterplot"]

class Graph(ABC):
    @abstractmethod
    def show(self, source_table): pass