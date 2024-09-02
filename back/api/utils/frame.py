"""
Old Visualizing File
"""

import io
import base64

import matplotlib
matplotlib.use("Agg")  # Using 'Agg' backend to generate plots without GUI

import pandas as pd
import matplotlib.pyplot as plt

from .binary_string_generator import BinaryStringMethod


class Frame(BinaryStringMethod):
    """_summary_

    Args:
        BinaryStringMethod (_type_): _description_
    """

    def __init__(self, path):
        self.frame = pd.read_csv(path).dropna()

    def get_binary_strings(self):
        """
        Generate binary strings representing plots for each column in the DataFrame.

        Returns:
          list: List of binary strings representing plots for each column.
        """
        try:
            result = []

            for col in self.frame.columns:
                series = self.frame[col]

                if series.dtype == "float64":
                    result.append(Frame.image_to_binary(series, "hist", "box", "line"))
                    
                elif series.dtype == "object":
                    series = series.value_counts()
                    result.append(Frame.image_to_binary(series, "pie", "bar", "barh"))

            return result

        except Exception as e:
            print(e)
            return {}

    @classmethod
    def image_to_binary(self, series, *kinds):
        """
        Generate binary string representing a plot for the given series.

        Args:
          series (pd.Series): The series data for which plot is to be generated.
          *kinds (str): Variable number of plot kinds to be generated.

        Raises:
          TypeError: If the given series is not a Pandas Series.

        Returns:
          str: Binary string representing the plot.
        """
        if not isinstance(series, pd.Series):
            raise TypeError(
                "The wrong argument received. It must be the instance of pandas.Series"
            )

        with io.BytesIO() as buf:
            fig, axes = plt.subplots(1, 3, figsize=(15, 5))  # 1 row, 3 columns

            # Plot each series in the list with the corresponding kind
            for ax, kind in zip(axes, kinds):
                ax.set_title(series.name)
                series.plot(ax=ax, kind=kind, rot=45 if kind.startswith("bar") else 0)

            # Save the figure to the buffer
            plt.savefig(buf, format="png")
            plt.close(fig)

            buf.seek(0)
            binary_data = buf.getvalue()
            binary_string = base64.b64encode(binary_data).decode("utf-8")

        return binary_string
