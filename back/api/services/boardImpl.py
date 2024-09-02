from api.utils.visualization.graphImpl import GraphImpl
from api.utils.exceptions import BoardException

import matplotlib.pyplot as plt
import pandas as pd


class Board():
    
    def __init__(
        self,
        row: int,
        col: int,
        path: str
    ):
        
        self.fig, self.axs = plt.subplots(row, col, figsize=(10, 10))
        
        if col * row == 1:
            self.graphs = [[GraphImpl(self.axs)]]
        else:
            self.graphs = [[GraphImpl(self.axs[j][i]) for i in range(row)] for j in range(col)]
        
        if path.endswith(".csv"):
            self.source_table = pd.read_csv(path)
        elif path.endswith(".xls", "xls", "xlsx", "xlsm", "xlsb", "odf", "ods", "odt"):
            self.source_table = pd.read_excel(path)
        
        self.numerical_variables = self.source_table.select_dtypes(include=['int64', 'float64']).columns
        self.categorical_variables = self.source_table.select_dtypes(include=['object', 'category']).columns
        self.datetime_variables = self.source_table.select_dtypes(include=['datetime']).columns
    
    
    def get_categorical_variables(self) -> list[str]:
        return self.categorical_variables
    
    def get_numerical_variables(self) -> list[str]:
        return self.numerical_variables
    
    def get_datetime_variables(self) -> list[str]:
        return self.datetime_variables
    
    def set_categorical_variables(self, *categorical_variables: str):
        self.categorical_variables = categorical_variables
    
    def set_numerical_variables(self, *numerical_variables: str):
        self.numerical_variables = numerical_variables
    
    def set_datetime_variables(self, *datetime_variables: str):
        self.datetime_variables = datetime_variables
    
    def draw(self):
        for _ in self.graphs:
            for graph in _: graph.show(self.source_table)
    
    def choose(self, plot_type: str, row: int, col: int):
        self.graphs[row-1][col-1].set_plot_type(plot_type)

    def set(self, row: int, col: int, x: str, y: str | None = None):
        graph = self.graphs[row-1][col-1]
        
        if graph.plot_type.startswith('bar'):
            if not (x in self.categorical_variables and y in self.numerical_variables):
                raise BoardException("""The variables are invalid.
                                     Barplot requires one categorical variable and one numerical variable.""")
            
        elif graph.plot_type.startswith('hist'):
            if not (x in self.numerical_variables and y is None):
                raise BoardException("""The variables are invalid.
                                     Histogram requires only one numerical discrete variable.""")
            
        elif graph.plot_type.startswith('scatter'):
            if x in self.categorical_variables or y in self.categorical_variables:
                raise BoardException("""The variables are invalid.
                                     Scatterplot requires two numerical variables.""")
        
        elif graph.plot_type.startswith('line'):
            if x in self.categorical_variables or y in self.categorical_variables:
                raise BoardException("""The variables are invalid.
                                     Lineplot requires two numerical variables.""")
        
        graph.set_x(x)
        graph.set_y(y)
    
    def resize(self, width: int, height: int):
        plt.rcParams["figure.figsize"] = (width, height)
    
    # For Test
    def __save(self, path="media/test.png"):
        plt.tight_layout()
        plt.savefig(path)