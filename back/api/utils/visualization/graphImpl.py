from .graph import Graph, PLOT_TYPE
from matplotlib.axes import Axes
import seaborn as sns # type: ignore
sns.set_theme(style="whitegrid")


class GraphImpl(Graph):
    
    def __init__(
        self,
        axis: Axes,
        x: str = None,
        y: str = None
    ):
        self.x = x
        self.y = y
        self.axis = axis

    
    def get_x(self) -> str:
        return self.x
    
    def get_y(self) -> str:
        return self.y
        
    def get_axis(self):
        return self.axis
        
    def get_plot_type(self) -> PLOT_TYPE:
        return PLOT_TYPE
    
    
    def set_x(self, variable: str):
        self.x = variable
    
    def set_y(self, variable: str):
        self.y = variable
        
    def set_axis(self, axis: Axes):
        self.axis = axis

    def set_plot_type(self, plot_type: PLOT_TYPE):
        self.plot_type = plot_type
    
    
    def show(self, source_table):
        if self.x == None: return
        
        if self.plot_type == 'barplot':
            key_params = {
                'data': source_table[self.x].value_counts()
                        if self.y is None else
                        source_table,
                'x': self.x,
                'y': self.y,
                'ax': self.axis,
                'errorbar': 'sd',
            }
            
            design_params = {
                'width': 0.5,
                'linewidth': 1.5,
                'err_kws': {
                    'color': '.5',
                    'linewidth': 2.5
                },
                'edgecolor': '.5',
                'facecolor': (0, 0, 0, 0)
            }
            
            sns.barplot(**(key_params | design_params))
            
            self.axis.bar_label(
                self.axis.containers[0],
                fontsize=12
            )