from abc import ABC, abstractmethod


class BinaryString(ABC):
    """
    An abstract base class defining a method for getting binary strings.

    This class is intended to be subclassed to provide implementation for
    generating binary strings.
    
    Methods:
        get_binary_strings: Abstract method to be implemented by subclasses
            for generating binary strings.
    """

    @abstractmethod
    def get_binary_string(self):
        """
        Abstract method to generate binary string.

        This method must be implemented by subclasses to provide functionality
        for generating binary string.

        Returns:
            str: The generated binary string.

        Raises:
            NotImplementedError: If this method is not implemented by a subclass.
        """
        pass
